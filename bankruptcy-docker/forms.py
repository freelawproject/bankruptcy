import json
import tempfile
import uuid

from django import forms


class AudioForm(forms.Form):

    file = forms.FileField(label="document", required=True)
    audio_data = forms.JSONField(label="audio-data", required=True)

    def clean(self):
        self.cleaned_data["fp"] = f"/tmp/audio_{uuid.uuid4().hex}.mp3"
        return self.cleaned_data


class ImagePdfForm(forms.Form):

    sorted_urls = forms.CharField(required=True, label="sorted-urls")

    def clean(self):
        self.cleaned_data["sorted_urls"] = json.loads(self.cleaned_data["sorted_urls"])
        return self.cleaned_data


class DocumentForm(forms.Form):

    file = forms.FileField(label="document", required=False)

    def temp_save_file(self, fp):
        with open(fp, "wb") as f:
            for chunk in self.cleaned_data["file"].chunks():
                f.write(chunk)

    def clean(self):
        """"""
        fp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        self.cleaned_data["fp"] = fp.name
        self.temp_save_file(fp.name)
        return self.cleaned_data
