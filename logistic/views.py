from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Commodity, StorageCondition
from .serializers import CommoditySerializer, StorageConditionSerializer


class StorageConditionViewSet(viewsets.ModelViewSet):
    queryset = StorageCondition.objects.all()
    serializer_class = StorageConditionSerializer


class CommoditiesViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
