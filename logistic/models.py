import datetime

from django.db import models


# Create your models here.
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
