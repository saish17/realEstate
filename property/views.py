from django.shortcuts import render

from rest_framework import viewsets 
from property.models import Property
from property.serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
