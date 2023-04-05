from django.shortcuts import render

from rest_framework import viewsets 
from enquiry.models import Enquiry
from enquiry.serializers import EnquirySerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

