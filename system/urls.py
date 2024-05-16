from django.urls import path

from system.views import CustomPermissionViewSet, RoleViewSet, UserViewSet

urlpatterns = [
    path(
        "permissions",
        CustomPermissionViewSet.as_view({"get": "list", "post": "create"}),
        name="custom_permission_api",
    ),
    path(
        "permissions/<int:pk>",
        CustomPermissionViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="custom_permission_api_detail",
    ),
    path(
        "roles",
        RoleViewSet.as_view({"get": "list", "post": "create"}),
        name="role_api",
    ),
    path(
        "roles/<int:pk>",
        RoleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="role_api_detail",
    ),
    path(
        "users",
        UserViewSet.as_view({"get": "list"}),
        name="users_api",
    ),
    path(
        "users/<int:pk>",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="user_api",
    ),
]
