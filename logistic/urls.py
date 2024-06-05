from django.urls import path

from logistic.views import (
    CommodityViewSet,
    GoodHazardClassViewSet,
    StorageConditionViewSet,
    WarehouseViewSet,
)

urlpatterns = [
    path(
        "good_hazard_classes",
        GoodHazardClassViewSet.as_view({"get": "list", "post": "create"}),
        name="good_hazard_classes_api",
    ),
    path(
        "good_hazard_classes/<int:pk>",
        GoodHazardClassViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="good_hazard_classes_api_detail",
    ),
    path(
        "storage_conditions",
        StorageConditionViewSet.as_view({"get": "list", "post": "create"}),
        name="storage_condition_api",
    ),
    path(
        "storage_conditions/<int:pk>",
        StorageConditionViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="storage_condition_api_detail",
    ),
    path(
        "commodities",
        CommodityViewSet.as_view({"get": "list", "post": "create"}),
        name="commodity_api",
    ),
    path(
        "commodities/<int:pk>",
        CommodityViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="commodity_api_detail",
    ),
    path(
        "warehouses",
        WarehouseViewSet.as_view({"get": "list", "post": "create"}),
        name="warehouses_api",
    ),
    path(
        "warehouses/<int:pk>",
        WarehouseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="warehouses_api_detail",
    ),
    path(
        "good_hazard_class",
        GoodHazardClassViewSet.as_view({"get": "list", "post": "create"}),
        name="users_api",
    ),
    path(
        "good_hazard_class/<int:pk>",
        GoodHazardClassViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="good_hazard_class_api_detail",
    ),
]
