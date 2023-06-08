from django.db import models

from datetime import datetime

from broker.models import Broker
from django.core.mail import send_mail
from pages.models import Subscriber
from django.conf import settings

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name='states')
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, related_name='cities')
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name


class Property(models.Model):
    broker = models.ForeignKey(Broker, on_delete= models.CASCADE)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    zipcode = models.CharField(max_length=13)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField() 
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    plot_size = models.DecimalField(max_digits=5, decimal_places=1)
    status = models.CharField(max_length=10,choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')],default='DEFAULT VALUE')
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 = models.ImageField(upload_to='photos/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        subscribers = Subscriber.objects.all()
        
        if is_new:
            for subscriber in subscribers:
                send_mail(
                    'New properties on our website',
                    f'There is a new property on our website: {self.title}.',
                    "Estate Agent <settings.DEFAULT_FROM_EMAIL>",
                    [subscriber.email],
                    fail_silently=False,
                )
