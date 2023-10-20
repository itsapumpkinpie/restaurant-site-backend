from django.contrib import admin
from django.urls import path
from menu.views import *
from feedback.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/menulist', MenuAPIList.as_view()),
    path('api/v1/menulist/<int:pk>/', MenuAPIUpdate.as_view()),
    path('api/v1/menudel/<int:pk>/', MenuAPIDel.as_view()),
    path('api/v1/feedbacklist', FeedbackAPIList.as_view()),
    path('api/v1/feedbacklist/<int:pk>/', FeedbackAPIUpdate.as_view()),
    path('api/v1/feedbackdel/<int:pk>/', FeedbackAPIDel.as_view())
]
