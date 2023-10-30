from django import forms
from django.forms import ModelForm
from .models import HistopathologicalSample


# MODEL_CHOICES = [
#     ('ViT', 'ViT'),
#     ('ResNet-50', 'ResNet-50'),
# ]
# DR_METHODS = [
#     ('HNNE', 'HNNE'),
#     ('T-SNE', 'T-SNE'),
#     ('MDS', 'MDS'),
#     ('PCA', 'PCA'),
#     ('ISOMAP', 'ISOMAP'),
#
# ]
# DIMENSIONS = [
#     (3, 3),
#     (2, 2),
# ]
#
#
# # SHAPE_ADJUSTMENT_METHOD = [
# #     ('None', 'None (assumes 1024 x 1024 RGB)'),
# #     ('Resize', 'Resize'),
# #     ('Pad', 'Pad'),
# # ]
#
# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True
#
#
# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)
#
#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result
#
#
# class ConfigurationForm(forms.Form):
#     project_name = forms.CharField(
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         label='Project Recruiting_site',
#         required=True
#     )
#
#     input_path = MultipleFileField(
#         required=False,
#         label='Add / upload files to project',
#     )
#
#     model = forms.ChoiceField(
#         choices=MODEL_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         label='Model'
#     )
#
#     dr_method = forms.ChoiceField(
#         choices=DR_METHODS,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         label='Dimensionality reduction method'
#     )
#
#     desired_dims = forms.ChoiceField(
#         choices=DIMENSIONS,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         label='Output dimensions'
#     )

class SampleForm(ModelForm):
    class Meta:
        model = HistopathologicalSample
        fields = [
            'recruiting_site',
            'patient_identifier',
            'patient',
            'died',
            'tissue_name',
            'used_in',
            'date',
            'tissue_type',
            'type_intervention',
            'localisation',
            'grading',
            'histology_subtype',
            'tumor_cell_content',
            'reviewed_and_processed_by',
            'identifier',
            'spl_status',
            'sequencing_type',
            'data_sequencing_data_release',
            'tumor_cell_content_bioinf',
            'reviewed_and_processed_by_sequencing',
        ]
