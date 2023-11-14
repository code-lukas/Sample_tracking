from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import requires_csrf_token

from .forms import SampleForm
from typing import Any
from .models import HistopathologicalSample


# Create your views here.

class SampleTrackingView(TemplateView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        template_name = 'gui/index.html'
        context = {
            'form': SampleForm()
        }
        return render(request, template_name, context=context)

    @method_decorator(requires_csrf_token)
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form: SampleForm = SampleForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Submission successful!')
        else:
            messages.error(request, 'Submission unsuccessful!')
        return HttpResponseRedirect(request.path_info)


class AllSamplesView(TemplateView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        template_name = 'gui/all_samples.html'
        samples = HistopathologicalSample.objects.all()
        fields_and_values_list = [
            [(field.name, getattr(instance, field.name)) for field in instance._meta.fields]
            for instance in samples
        ]
        context = {
            'samples': fields_and_values_list,
        }
        return render(request, template_name, context=context)
