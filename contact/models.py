from django.db import models

from datetime import datetime

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=13)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    contact_date = models.DateField(default=datetime.now, blank=True)
    
def __str__(self):
    
        return self.name