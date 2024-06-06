from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from rest_framework import serializers, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from backend.permissions import (
    HasCreatePermissionPermission,
    HasCreateRolePermission,
    HasDeletePermissionPermission,
    HasDeleteRolePermission,
    HasReadPermissionPermission,
    HasReadRolePermission,
    HasSystemPermission,
    HasUpdatePermissionPermission,
    HasUpdateRolePermission,
)

from .models import CustomPermission, Role
from .serializers import (
    CustomPermissionSerializer,
    LoginSerializer,
    RoleSerializer,
    SignupSerializer,
    UserSerializer,
)

User = get_user_model()


class CustomPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomPermission.objects.all()
    serializer_class = CustomPermissionSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreatePermissionPermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadPermissionPermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdatePermissionPermission]
        elif self.action == "destroy":
            permission_classes = [HasDeletePermissionPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [HasCreateRolePermission]
        elif self.action == "retrieve" or self.action == "list":
            permission_classes = [HasReadRolePermission]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [HasUpdateRolePermission]
        elif self.action == "destroy":
            permission_classes = [HasDeleteRolePermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "signup":
            return SignupSerializer
        elif self.action == "login":
            return LoginSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ["signup", "login"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, HasSystemPermission]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                # Speichern des Tokens in der Sitzung
                request.session["access_token"] = access_token
                request.session["refresh_token"] = refresh_token
                return Response(
                    {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request):
        # Entfernen des Tokens aus der Sitzung
        request.session.pop("access_token", None)
        request.session.pop("refresh_token", None)
        return Response(
            {"message": "User logged out successfully"}, status=status.HTTP_200_OK
        )
