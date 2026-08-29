from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ("id", "email", "full_name", "phone", "role", "is_active", "created_at")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model  = User
        fields = ("email", "full_name", "phone", "role", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)