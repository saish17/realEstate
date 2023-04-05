from django.db import models

from datetime import datetime

# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    broker_img = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    mobile = models.CharField(max_length=13)
    hire_date = models.DateField()
    
    
    def __str__(self):
    
        return self.name