from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu
from .serializers import MenuSerializer


class MenuAPIView(APIView):
    def get(self, request):
        menu_data = Menu.objects.all()
        return Response({
            'menu': MenuSerializer(menu_data, many=True).data
        })
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'menu': serializer.data
        })

