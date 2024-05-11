from django.urls import path

from logistic.views import CommodityViewSet, StorageConditionViewSet, GoodHazardClassViewSet, WareHouseViewSet

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
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="commodity_api_detail",
    ),
    path(
        "ware_houses",
        WareHouseViewSet.as_view({"get": "list", "post": "create"}),
        name="ware_houses_api",
    ),
    path(
        "ware_houses/<int:pk>",
        WareHouseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="ware_houses_api_detail",
    ),
]
