from django.urls import path

from logistic.views import CommoditiesViewSet

urlpatterns = [
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
