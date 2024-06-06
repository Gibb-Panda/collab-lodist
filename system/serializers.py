from django.contrib.auth import get_user_model
from rest_framework import serializers

from backend.permissions import HasUpdateRolePermission

from .models import ConfigUser, CustomPermission, Role

User = get_user_model()


class CustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    permissions = CustomPermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = "__all__"


class SimpleRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = [
            "permissions",
        ]


class ConfigUserSerializer(serializers.ModelSerializer):
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True
    )
    role = SimpleRoleSerializer(read_only=True)

    class Meta:
        model = ConfigUser
        fields = ["role_id", "role"]


class UserSerializer(serializers.ModelSerializer):
    config = ConfigUserSerializer()

    class Meta:
        model = User
        exclude = [
            "groups",
            "user_permissions",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and not HasUpdateRolePermission().has_permission(request, self):
            self.fields["config"].fields.pop("role", None)
            self.fields["config"].fields.pop("role_id", None)

    def update(self, instance, validated_data):
        config_data = validated_data.pop("config", None)
        instance = super().update(instance, validated_data)

        if config_data:
            role = config_data.get("role")
            if role:
                config_user, created = ConfigUser.objects.get_or_create(user=instance)
                config_user.role = role
                config_user.save()

        return instance


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        ConfigUser.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
