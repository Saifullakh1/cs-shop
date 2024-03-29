from rest_framework import serializers
from ..models import Clothes


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = [
            "id", "title", "description",
            "image", "size", "price", "old_price",
            "currency", "is_active", "category"

        ]

