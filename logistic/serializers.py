from rest_framework import serializers

from .models import Commodity, GoodHazardClass, StorageCondition, Warehouse


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


class GoodHazardClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodHazardClass
        fields = "__all__"


class CommoditySerializer(serializers.ModelSerializer):
    storage_conditions = StorageConditionSerializer(many=True, read_only=True)
    good_hazard_class = GoodHazardClassSerializer(many=True, read_only=True)

    class Meta:
        model = Commodity
        fields = "__all__"

    def __str__(self):
        return self.article_number


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
