from rest_framework import serializers

from unlimited_parts.models import Part
from unlimited_parts.models import DescriptionWordCount


class PartSerializer(serializers.ModelSerializer):
    weightOunces = serializers.IntegerField(source="weight_ounces")
    isActive = serializers.IntegerField(source="is_active")

    class Meta:
        model = Part
        fields = ["id", "name", "sku", "description", "weightOunces", "isActive"]


class DescriptionWordCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionWordCount
        fields = "__all__"
