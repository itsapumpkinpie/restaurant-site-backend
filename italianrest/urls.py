from django.contrib import admin
from django.urls import path
from menu.views import MenuAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/menulist', MenuAPIView.as_view())
]
