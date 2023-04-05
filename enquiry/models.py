from django.db import models

from datetime import datetime

from property.models import Property

from django.contrib.auth.models import User


# Create your models here.
class Enquiry(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    property = models.ForeignKey(Property, on_delete= models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    
    subject = models.CharField(max_length=30,)
    message = models.TextField(max_length=100,)
    added_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    