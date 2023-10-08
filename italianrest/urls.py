from django.contrib import admin
from django.urls import path
from menu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/menulist', MenuAPIList.as_view()),
    path('api/v1/menulist/<int:pk>/', MenuAPIUpdate.as_view()),
    path('api/v1/menudel/<int:pk>/', MenuAPIDel.as_view())
]
