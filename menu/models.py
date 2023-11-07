from django.db import models

class Menu(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_description = models.CharField(max_length=60, default='описание')
    photo_path = models.CharField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.dish_name

class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    def __str__(self):
        return self.cat_name
