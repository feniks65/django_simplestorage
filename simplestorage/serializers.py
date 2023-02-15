from django.contrib.auth.models import User
from rest_framework import serializers
from .models import File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'file')

class FileSystemFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=255)
    size = serializers.IntegerField()

