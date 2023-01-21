from rest_framework import serializers

from unlimited_parts.models import Part


class PartSerializer(serializers.ModelSerializer):
    weightOunces = serializers.IntegerField(source="weight_ounces")
    isActive = serializers.IntegerField(source="is_active")

    class Meta:
        model = Part
        fields = ["id", "name", "sku", "description", "weightOunces", "isActive"]
