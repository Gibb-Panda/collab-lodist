from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from backend.permissions import (
    HasCreateCommodityPermission,
    HasCreateGoodHazardClassPermission,
    HasCreateStorageConditionPermission,
    HasCreateWarehousePermission,
    HasDeleteCommodityPermission,
    HasDeleteGoodHazardClassPermission,
    HasDeleteStorageConditionPermission,
    HasDeleteWarehousePermission,
    HasReadCommodityPermission,
    HasReadGoodHazardClassPermission,
    HasReadStorageConditionPermission,
    HasReadWarehousePermission,
    HasUpdateCommodityPermission,
    HasUpdateGoodHazardClassPermission,
    HasUpdateStorageConditionPermission,
    HasUpdateWarehousePermission,
)

from .models import Commodity, GoodHazardClass, StorageCondition, Warehouse
from .serializers import (
    CommoditySerializer,
    GoodHazardClassSerializer,
    StorageConditionSerializer,
    WarehouseSerializer,
)


class StorageConditionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StorageCondition.objects.all()
    serializer_class = StorageConditionSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreateStorageConditionPermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadStorageConditionPermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdateStorageConditionPermission]
        elif self.action == "destroy":
            permission_classes = [HasDeleteStorageConditionPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class CommodityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreateCommodityPermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadCommodityPermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdateCommodityPermission]
        elif self.action == "destroy":
            permission_classes = [HasDeleteCommodityPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class WarehouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreateWarehousePermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadWarehousePermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdateWarehousePermission]
        elif self.action == "destroy":
            permission_classes = [HasDeleteWarehousePermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class GoodHazardClassViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GoodHazardClass.objects.all()
    serializer_class = GoodHazardClassSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreateGoodHazardClassPermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadGoodHazardClassPermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdateWarehousePermission]
        elif self.action == "destroy":
            permission_classes = [HasDeleteWarehousePermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]
