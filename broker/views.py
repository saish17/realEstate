from django.shortcuts import render

from django.http import HttpResponse

from broker.models import Broker
# Create your views here.

def index(request):
    
    # return HttpResponse('hello all');
    return render(request, 'broker/index.html')
    
    
def about(request):
    
    # return HttpResponse('this is about page');
    return render(request, 'broker/about.html')
    
    
def contact(request):
    
    if request.method == 'POST':
        
        contact = Contact(name=request.POST['name'],email=request.POST['email'],mobile=request.POST['mobile'],description=request.POST['description'])
        contact.save()
    
    # return HttpResponse('contact page here');
    return render(request, 'broker/contact.html')
    
    
def login(request):

    return render(request, 'broker/login.html')
        
        
def register(request):

    return render(request, 'broker/register.html')

from rest_framework import viewsets 
from broker.models import Broker
from broker.serializers import BrokerSerializer

class BrokerViewSet(viewsets.ModelViewSet):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer