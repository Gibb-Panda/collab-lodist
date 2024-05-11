from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Commodity, StorageCondition,GoodHazardClass, WareHouse
from .serializers import CommoditySerializer, StorageConditionSerializer, GoodHazardClassSerializer, WareHouseSerializer


class StorageConditionViewSet(viewsets.ModelViewSet):
    queryset = StorageCondition.objects.all()
    serializer_class = StorageConditionSerializer

class GoodHazardClassViewSet(viewsets.ModelViewSet):
    queryset = GoodHazardClass.objects.all()
    serializer_class = GoodHazardClassSerializer

class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

class WareHouseViewSet(viewsets.ModelViewSet):
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
