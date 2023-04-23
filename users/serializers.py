from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

"""
Serializers are used for converting instances into native datatypes which can be rendered easily by JSON,\
XML content types.

"""

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user