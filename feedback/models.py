from django.core.validators import EmailValidator
from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=50, blank=False)
    user_email = models.EmailField(blank=False)
    content = models.CharField(max_length=250, blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name
