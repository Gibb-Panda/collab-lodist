from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Commodity, StorageCondition,GoodHazardClass
from .serializers import CommoditySerializer, StorageConditionSerializer, GoodHazardClassSerializer


class StorageConditionViewSet(viewsets.ModelViewSet):
    queryset = StorageCondition.objects.all()
    serializer_class = StorageConditionSerializer

class GoodHazardClassViewSet(viewsets.ModelViewSet):
    queryset = GoodHazardClass.objects.all()
    serializer_class = GoodHazardClassSerializer

class CommoditiesViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
