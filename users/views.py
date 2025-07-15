from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
