from django.contrib import admin
from .models import Location
from django.contrib.gis.admin import OSMGeoAdmin

admin.site.register(Location)


class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'geom')