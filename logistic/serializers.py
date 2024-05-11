from rest_framework import serializers

from .models import Commodity, StorageCondition


class StorageConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageCondition
        fields = "__all__"

    def __str__(self):
        return self.title


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = "__all__"

    def __str__(self):
        return self.article_number
