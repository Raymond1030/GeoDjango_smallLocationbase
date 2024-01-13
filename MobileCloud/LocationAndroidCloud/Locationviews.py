# LocationAndroidCloud/Locationviews.py

from rest_framework import viewsets
from .models import Location  # 替换为你的模型
from .serializers import LocationSerializer  # 替换为你的序列化器

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class LocationModelViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
