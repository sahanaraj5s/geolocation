from django.db import models


class Geolocation(models.Model):
    address = models.CharField(max_length=256)
    output_format = models.CharField(max_length=20)

    class Meta:
        db_table = "geolocation"

