from django.urls import path

from logistic.views import CommoditiesViewSet, StorageConditionViewSet

urlpatterns = [
    path(
        "storage_conditions",
        StorageConditionViewSet.as_view({"get": "list", "post": "create"}),
        name="storage_conditoon_api",
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
        CommoditiesViewSet.as_view({"get": "list", "post": "create"}),
        name="commodity_api",
    ),
    path(
        "commodities/<int:pk>",
        CommoditiesViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="commodity_api_detail",
    ),
]
