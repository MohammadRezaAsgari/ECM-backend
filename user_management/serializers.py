from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True,required=True,max_length=50)
    password = serializers.CharField(write_only=True,required=True,max_length=50)
