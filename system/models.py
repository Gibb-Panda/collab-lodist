from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.


class CustomPermission(models.Model):
    value = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.value


class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(
        CustomPermission, related_name="roles", blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class ConfigUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="config")
    role = models.OneToOneField(
        Role, on_delete=models.SET_NULL, related_name="config", null=True, blank=True
    )
