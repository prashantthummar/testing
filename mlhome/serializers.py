from rest_framework import serializers
from . import models


class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAdd
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password', 'base_template': 'textarea.html'}
    )
    remember_me = serializers.BooleanField()
    