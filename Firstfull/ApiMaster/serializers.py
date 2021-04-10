from rest_framework import serializers
from .models import UserProfile, Crop


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = [
            'id',
            'name_of_crop',
            'type',
            'price', 'quantity',
            'qaulity',
            'date_of_import',
            'date_before_used'
        ]
