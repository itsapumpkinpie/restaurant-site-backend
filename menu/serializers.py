from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.Serializer):
    dish_name = serializers.CharField(max_length=50)
    photo_path = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)
