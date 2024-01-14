from django.db import models

class BuildingIFC(models.Model):
    ref_bag_id = models.IntegerField(primary_key=True)
    ifc_file = models.FileField(upload_to='ifc_files/')