from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50,blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

from django.contrib.auth.models import User
from django.db import models
from broker.models import Broker

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    registration_type = models.CharField(max_length=255, default='')

    broker = models.OneToOneField(Broker, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

