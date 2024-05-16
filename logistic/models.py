import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.


class StorageCondition(models.Model):
    title = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class GoodHazardClass(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name


class GoodHazardClass(models.Model):
    class_name = models.CharField(max_length=50)


class Commodity(models.Model):
    article_number = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    weight = models.IntegerField()
    length_dimension = models.IntegerField()
    height_dimension = models.IntegerField()
    country_of_origin = models.CharField(max_length=50)
    expiry_date = models.DateField(default=datetime.date.today)
    customs_tariff_number = models.CharField(max_length=20)
    packagin_information = models.TextField(null=True, blank=True)
    insurance_value = models.IntegerField(null=True)
    storage_condition = models.ForeignKey(
        StorageCondition,
        models.SET_NULL,
        null=True,
        related_name="commodities",
        blank=True,
    )
    good_hazard_class = models.OneToOneField(
        GoodHazardClass,
        models.CASCADE,
        related_name="good_hazard_class",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.article_number


class Warehouse(models.Model):
    name_of_location = models.CharField(max_length=100)
    address = models.TextField(max_length=100, null=True, blank=True)
    contact_information = models.TextField(max_length=100, null=True, blank=True)
    storage_capacity = models.IntegerField()
    horse_power = models.IntegerField()
    capacity = models.IntegerField()
    load_capacity = models.IntegerField()
    insurance_information = models.TextField(max_length=50, null=True, blank=True)
    responsible = models.ForeignKey(User, models.CASCADE, related_name="warehouses")
