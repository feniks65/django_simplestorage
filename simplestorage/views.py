#from django.shortcuts import render

# Create your views here.

import os
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import File
from .serializers import UserSerializer, FileSerializer, FileSystemFileSerializer

class UserViewSet(viewsets.ViewSet):
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Logged In"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def list(self, request):
        directory_path = './uploads'
        file_list = []

        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                file_info = {
                    'name': filename,
                    'path': os.path.join(directory_path, filename),
                    'size': os.path.getsize(os.path.join(directory_path, filename))
                }
                file_list.append(file_info)

        serializer = FileSystemFileSerializer(file_list, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        return File.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

