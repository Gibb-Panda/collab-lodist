from rest_framework import serializers

from .models import Commodity, StorageCondition, GoodHazardClass, WareHouse


class StorageConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCondition
        fields = "__all__"

    def __str__(self):
        return self.title

class GoodHazardClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodHazardClass
        fields = "__all__"

    def __str__(self):
        return self.class_name


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = "__all__"

    def __str__(self):
        return self.article_number

class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouse
        fields = "__all__"

    def __str__(self):
        return self.name_of_location
