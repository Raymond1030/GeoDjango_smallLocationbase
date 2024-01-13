from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location  # 你的 POI 模型
from .serializers import LocationSerializer  # 你的 POI 序列化器
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class NearbyFriendPOIView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取经纬度参数
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        user_location = Point(float(longitude), float(latitude), srid=4326)

        # 查询 500 米范围内的 POI
        nearby_pois = Location.objects.annotate(distance=Distance('location', user_location)).filter(
            distance__lte=500).order_by('distance')

        # 序列化查询结果
        serializer = LocationSerializer(nearby_pois, many=True)
        return Response(serializer.data)
