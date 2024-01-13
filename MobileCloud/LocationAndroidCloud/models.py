from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField()
