from django.db import models
from django.utils import timezone
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Film Adı')
    description = models.TextField(verbose_name='Film Açıklaması')
    image = models.CharField(max_length=50, verbose_name='Film Resmi')
    created_date = models.DateTimeField(default=timezone.now,input_formats=['%d/%m/%Y'], verbose_name='Eklenme Tarihi')
    isPublished = models.BooleanField(default= True) 

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image