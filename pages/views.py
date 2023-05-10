from django.shortcuts import render, redirect

from django.http import HttpResponse

from contact.models import Contact

from enquiry.models import Enquiry

from property.models import Property

from django.contrib.auth.models import User

from django.contrib import messages, auth

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):

    properties = Property.objects.all()
    return render(request, 'pages/index.html', {'properties':properties});
    
def detail(request, property_id):
    
    property = Property.objects.get(pk=property_id)
    properties = Property.objects.all()
    
    return render(request, 'pages/detail.html', {'property':property});

def enquiry(request):
    
    if request.method == 'POST':
        
        enquiry = Enquiry(user_id=request.POST['user_id'], property_id=request.POST['property_id'], name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], subject=request.POST['subject'], message=request.POST['message'], added_date=request.POST['added_date'])
        enquiry.save()
        return HttpResponse('saved')


def dashboard(request):
    
    enquiries = Enquiry.objects.filter(user_id=request.user.id)
    properties = Property.objects.all()   
    return render(request, 'pages/dashboard.html', {'enquiries':enquiries,'properties':properties});

def search(request):

    properties = Property.objects.filter(title__iexact=request.GET['keywords']) | Property.objects.filter(city__state__country__name__iexact=request.GET['keywords']) | Property.objects.filter(address__iexact=request.GET['keywords']) | Property.objects.filter(status__iexact=request.GET['keywords'])

    return render(request, 'pages/search.html', {'properties':properties})
    
def about(request):
    
    #return HttpResponse('this is about page')
    return render(request, 'pages/about.html');
    
def contact(request):

    if request.method == 'POST':
        
        contact = Contact(fullname=request.POST['fullname'], email=request.POST['email'], mobile=request.POST['mobile'], message=request.POST['message'])
        contact.save()
    
    return render(request, 'pages/contact.html');



def login(request):

    if request.method == 'POST':
    
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'pages/login.html');


def logout(request):
    
    auth.logout(request)
    return redirect('index')

        
   
def register(request):

    if request.method == 'POST':
        
        user = User.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        
        user.save()
        
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
        
    return render(request, 'pages/register.html')

# view for send_email functionality
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from realEstate.forms import ContactForm

def email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email to admin
            send_mail(
                f'{subject} ({name})',
                f'From: {name} <{email}>\n\n{message}',
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'pages/email.html', {'form': form})

#view for subscribe_us functionality
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubscriberForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            send_mail(
                'Thank you for subscribing!',
                'Thanks for subscribing to Estate Agent, We will in contact with you',
                "Estate Agent",
                [subscriber.email],
                fail_silently=False,
            )
            return redirect('index')
    else:
        form = SubscriberForm()
    return render(request, 'pages/subscribe.html', {'form': form})

#api_view
from rest_framework import viewsets 
from pages.models import Subscriber
from pages.serializers import SubscriberSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

#add new property by User's end
from .forms import PropertyForm
from property.models import Property,State,City
def addproperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user  
            property.save()
            return redirect('index')
    else:
        form = PropertyForm()

    return render(request, 'pages/addproperty.html',{'form': form})

def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).all()
    return render(request, 'pages/state_dropdown_list_options.html', {'states': states})

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'pages/city_dropdown_list_options.html', {'cities': cities})