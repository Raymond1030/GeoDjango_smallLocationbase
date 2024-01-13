from django.contrib import admin
from .models import Location
from django.contrib.gis.admin import OSMGeoAdmin




class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'geom')


admin.site.register(Location, LocationAdmin)
