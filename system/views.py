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


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


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
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

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
