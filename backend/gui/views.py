from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import requires_csrf_token

from .forms import SampleForm
from typing import Any
from .models import HistopathologicalSample
import csv


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

    @method_decorator(requires_csrf_token)
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        delete_id = int(request.POST['id'])
        delete_instance = HistopathologicalSample.objects.get(id=delete_id)
        delete_instance.delete()
        return HttpResponseRedirect(request.path_info)


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    @staticmethod
    def write(value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def some_streaming_csv_view(request):
    """A view that streams a large CSV file."""
    samples = HistopathologicalSample.objects.all()
    fields_and_values_list = [
        [(field.name, getattr(instance, field.name)) for field in instance._meta.fields]
        for instance in samples
    ]
    rows = []
    headers = [i[0] for i in fields_and_values_list[0]]
    rows.append(headers)
    data = [[i[1] for i in sublist] for sublist in fields_and_values_list]
    data.insert(0, headers)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow(row) for row in data),
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="saturn3samples.csv"'},
    )
