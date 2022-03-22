from django.urls import path

from .views import (
    heartbeat,
    extract_bankruptcy_form,
    extract_106_AB,
    extract_106_D,
    extract_106_EF,
    extract_106_SUM,
)

urlpatterns = [
    path(
        "",
        heartbeat,
        name="heartbeat-disclosure",
    ),
    path(
        "extract/form/all/",
        extract_bankruptcy_form,
        name="extract-all-available-forms",
    ),
    path(
        "extract/form/106-SUM/",
        extract_106_SUM,
        name="extract-all-available-forms",
    ),
    path(
        "extract/form/106-EF/",
        extract_106_EF,
        name="extract-all-available-forms",
    ),
    path(
        "extract/form/106-D/",
        extract_106_D,
        name="extract-all-available-forms",
    ),
    path(
        "extract/form/106-AB/",
        extract_106_AB,
        name="extract-all-available-forms",
    ),
]
