from django.db import models


# Create your models here.
class HistopathologicalSample(models.Model):
    # django automatically adds a primary key
    # id = models.BigAutoField(primary_key=True)
    CHARFIELD_MAXLEN = 50
    recruiting_site = models.CharField(max_length=CHARFIELD_MAXLEN)
    patient_identifier = models.CharField(max_length=CHARFIELD_MAXLEN)
    patient = models.CharField(max_length=CHARFIELD_MAXLEN)
    died = models.BooleanField()
    tissue_name = models.CharField(max_length=CHARFIELD_MAXLEN)
    used_in = models.CharField(max_length=CHARFIELD_MAXLEN)
    date = models.DateField()
    tissue_type = models.CharField(max_length=CHARFIELD_MAXLEN)
    type_intervention = models.CharField(max_length=CHARFIELD_MAXLEN)
    localisation = models.CharField(max_length=CHARFIELD_MAXLEN)
    grading = models.CharField(max_length=CHARFIELD_MAXLEN)
    histology_subtype = models.CharField(max_length=CHARFIELD_MAXLEN)
    tumor_cell_content = models.CharField(max_length=CHARFIELD_MAXLEN)
    reviewed_and_processed_by = models.CharField(max_length=CHARFIELD_MAXLEN)
    identifier = models.CharField(max_length=CHARFIELD_MAXLEN)
    spl_status = models.CharField(max_length=CHARFIELD_MAXLEN)
    sequencing_type = models.CharField(max_length=CHARFIELD_MAXLEN)
    data_sequencing_data_release = models.CharField(max_length=CHARFIELD_MAXLEN)
    tumor_cell_content_bioinf = models.CharField(max_length=CHARFIELD_MAXLEN)
    reviewed_and_processed_by_sequencing = models.CharField(max_length=CHARFIELD_MAXLEN)
