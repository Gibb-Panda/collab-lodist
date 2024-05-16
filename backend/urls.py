"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from system.views import UserViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("disposition/", include("disposition.urls")),
    path("logistics/", include("logistic.urls")),
    path("management/", include("management.urls")),
    path("system/", include("system.urls")),
    path("login/", UserViewSet.as_view({"post": "login"}), name="login"),
    path("signup/", UserViewSet.as_view({"post": "signup"}), name="signup"),
    path("logout/", UserViewSet.as_view({"post": "logout"}), name="logout"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
