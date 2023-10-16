from rest_framework import generics
from .models import Review
from .serializers import MenuSerializer

# Вернёт по get-запросу данные и добавит новые по post-запросу
class FeedbackAPIList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = MenuSerializer

class FeedbackAPIUpdate(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = MenuSerializer

class FeedbackAPIDel(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = MenuSerializer
