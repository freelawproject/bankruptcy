import unittest
from typing import Any

import requests


def make_file(filename) -> Any:
    filepath = f"/opt/app/bankruptcy-docker/test_assets/{filename}"
    with open(filepath, "rb") as f:
        return {"file": (filename, f.read())}


class BankruptcyTests(unittest.TestCase):

    def test_heartbeat(self):
        """"""
        response = requests.post("http://cl-bankruptcy:5050/")
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertEqual(response.text, "Heartbeat detected.", msg="Failed response.")

    def test_bankruptcy(self):
        """"""
        files = make_file(filename="gov.uscourts.ganb.1125040.35.0.pdf")
        response = requests.post("http://cl-bankruptcy:5050/extract/form/all/", files=files)
        self.assertEqual(response.status_code, 200, msg="Failed status code.")
        self.assertTrue(response.json()['form_106_sum']['consumer_debts'], msg="Failed response.")


    def test_scanned_pdfs(self):
        """Can we gracefully fail on scans?"""

        files = make_file(filename="gov.uscourts.orb.507503.11.0.pdf")
        response = requests.post("http://cl-bankruptcy:5050/extract/form/all/", files=files).json()
        self.assertFalse(response['success'])

    def test_can_we_handle_missing_checkboxes(self):
        """Can we handle partially bad PDF can still return content?"""

        # filepath = f"{self.assets}/gov.uscourts.ganb.1125040.35.0.pdf"
        # results = extract_all(filepath=filepath)
        files = make_file(filename="gov.uscourts.ganb.1125040.35.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/all/", files=files).json()
        self.assertEqual(results["form_106_d"]["error"], "Failed to find document.")
        self.assertEqual(len(results["form_106_ef"]["creditors"]), 22)

    def test_offical_form_106_sum(self):
        """Can we extract content from Official Form 106 Sum"""

        files = make_file(filename="gov.uscourts.orb.473342.1.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/106-SUM/", files=files).json()

        self.assertTrue(results["7/11/13"])
        self.assertTrue(results["non_consumer_debts"])
        self.assertEqual(results["3_total"], "863,842.00")
        self.assertEqual(results["9g"], "142,500.00")

    def test_official_form_106_e_f(self):
        """Can we extract content for unsecured creditors"""

        files = make_file(filename="gov.uscourts.orb.473342.1.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/106-EF/",
                                files=files).json()
        self.assertEqual(
            len(results["creditors"]), 19, msg="Failed to extract creditors"
        )
        self.assertEqual(
            results["creditors"][-1]["debtor"],
            ["At least one of the debtors and another"],
        )

    def test_official_form_106_d(self):
        """Can we extract secured creditors from form 106D"""

        files = make_file(filename="gov.uscourts.orb.473342.1.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/106-D/",
                                files=files).json()
        self.assertEqual(
            len(results["creditors"]), 9, msg="Failed to extract creditors"
        )

    def test_official_form_106_a_b(self):
        """Can we extract content from Form 106 A/B"""

        files = make_file(filename="gov.uscourts.orb.473342.1.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/106-AB/",
                                files=files).json()
        auto = results["cars_land_and_crafts"][3]
        self.assertEqual(
            len(results["cars_land_and_crafts"]),
            4,
            msg="Failed to extract cars_land_and_crafts",
        )
        self.assertEqual(
            auto["make"], "Skido", msg="Failed to extract cars_land_and_crafts"
        )
        self.assertEqual(
            auto["model"], "SM", msg="Failed to extract cars_land_and_crafts"
        )

    def test_all_methods(self):
        """Can we extract content from all four documents?"""

        files = make_file(filename="gov.uscourts.orb.473342.1.0.pdf")
        results = requests.post("http://cl-bankruptcy:5050/extract/form/all/", files=files).json()

        self.assertIn("Jr.", results["info"]["debtor_1"])
        self.assertEqual(results["form_106_sum"]["1a"], "325,882.00")
        self.assertEqual(results["form_106_sum"]["9g"], "142,500.00")
        self.assertEqual(
            results["form_106_ef"]["creditors"][0]["name"],
            "Internal Revenue Service",
        )
        self.assertEqual(
            results["form_106_d"]["creditors"][0]["name"], "Ally Financial"
        )
        self.assertEqual(
            results["form_106_ab"]["cars_land_and_crafts"][1]["make"],
            "Chevrolet",
        )
