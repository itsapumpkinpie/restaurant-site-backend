from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
