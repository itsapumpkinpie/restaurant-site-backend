from rest_framework import serializers
from .models import Review


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("user_name", "content", "time_create")