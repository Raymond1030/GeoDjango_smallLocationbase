from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import Location
import logging
# 获取一个logger对象
logger = logging.getLogger(__name__)
class LocationSerializer(serializers.ModelSerializer):
    # class Meta:
    #     fields = '__all__'
    #     models = Location
    # name = serializers.CharField(max_length=100)
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    # latitude = serializers.FloatField()
    # longitude = serializers.FloatField()

    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['latitude'] = instance.geom.y if instance.geom else None
        representation['longitude'] = instance.geom.x if instance.geom else None
        return representation

    def create(self, validated_data):
        logger.error(validated_data)
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        geom = Point(longitude, latitude, srid=4326) if latitude is not None and longitude is not None else None
        return Location.objects.create(geom=geom, **validated_data)

    def update(self, instance, validated_data):
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        if latitude and longitude:
            instance.geom = Point(longitude, latitude, srid=4326)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    # def get_latitude(self, obj):
    #     return obj.geom.y if obj.geom else None
    #
    # def get_longitude(self, obj):
    #     return obj.geom.x if obj.geom else None
    # def create(self, validated_data):
    #     latitude = validated_data.pop('latitude')
    #     longitude = validated_data.pop('longitude')
    #     geom = Point(longitude, latitude)
    #     return Location.objects.create(geom=geom, **validated_data)
