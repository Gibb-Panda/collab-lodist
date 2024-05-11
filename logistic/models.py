import datetime

from django.db import models

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
    storage_conditions = models.ManyToManyField(StorageCondition, blank=True, null=True)

    def __str__(self):
        return self.article_number

class WareHouse(models.Model):
    name_of_location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    storage_conditions = models.ManyToManyField(StorageCondition, blank=True, null=True)
    contact_information = models.CharField(max_length=100)
    storage_capacity = models.IntegerField()
    insurance_information = models.CharField(max_length=14)

    def __str__(self):
        return self.name_of_location
