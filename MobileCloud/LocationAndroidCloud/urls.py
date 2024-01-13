# LocationAndroidCloud/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Locationviews import LocationModelViewSet  # 引入视图集
from .NearByFriendPOIView import NearbyFriendPOIView
router = DefaultRouter()
router.register(r'', LocationModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
