from django.http import HttpResponse, JsonResponse
from bankruptcy import extract_all, extract_official_form_106_a_b, extract_official_form_106_d, extract_official_form_106_e_f, extract_official_form_106_sum
from .forms import DocumentForm
from .utils import cleanup_form

def heartbeat(request):
    """Heartbeat endpoint

    :param request:
    :return:
    """

    return HttpResponse(f"Heartbeat detected.")


def extract_bankruptcy_form(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_all(form.cleaned_data["fp"])
    cleanup_form(form)
    if not output:
        output = {"success": False}
    return JsonResponse(output)

def extract_106_AB(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_official_form_106_a_b(form.cleaned_data["fp"])
    cleanup_form(form)
    if not output:
        output = {"success": False}
    return JsonResponse(output)

def extract_106_D(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_official_form_106_d(form.cleaned_data["fp"])
    cleanup_form(form)
    if not output:
        output = {"success": False}
    return JsonResponse(output)

def extract_106_EF(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_official_form_106_e_f(form.cleaned_data["fp"])
    cleanup_form(form)
    if not output:
        output = {"success": False}
    return JsonResponse(output)

def extract_106_SUM(request):
    """"""
    form = DocumentForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False})
    output = extract_official_form_106_sum(form.cleaned_data["fp"])
    cleanup_form(form)
    if not output:
        output = {"success": False}
    return JsonResponse(output)
