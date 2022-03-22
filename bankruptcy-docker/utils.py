import os


def cleanup_form(form):
    """Clean up a form object"""
    os.remove(form.cleaned_data["fp"])
