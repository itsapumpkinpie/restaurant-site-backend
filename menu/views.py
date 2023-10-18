from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu
from .serializers import MenuSerializer

# Вернёт по get-запросу данные и добавит новые по post-запросу
class MenuAPIList(generics.ListCreateAPIView):
    pagination_class = None
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuAPIUpdate(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuAPIDel(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# class MenuAPIView(APIView):
#     def get(self, request):
#         menu_data = Menu.objects.all()
#         return Response({
#             'menu': MenuSerializer(menu_data, many=True).data
#         })
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             'menu': serializer.data
#         })

