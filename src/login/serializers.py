from django.contrib.auth.password_validation import validate_password
from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from login.models import Auth


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'username', 'email', 'role')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Auth.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Auth
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True},
        }

        def create(self, validated_data):
            user = Auth.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
            )
            user.save()
            return user
