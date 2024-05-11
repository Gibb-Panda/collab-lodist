from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Commodity
from .serializers import CommoditySerializer


class CommoditiesViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
