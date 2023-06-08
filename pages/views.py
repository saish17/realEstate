from django.shortcuts import render, redirect

from django.http import HttpResponse

from contact.models import Contact

from enquiry.models import Enquiry

from property.models import Property

from django.contrib.auth.models import User

from django.contrib import messages, auth

from django.core.mail import send_mail
from django.conf import settings
import logging
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





from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Subscriber


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            # Check if the user is already a subscriber
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'message': 'You are already a subscriber.'})
            else:
                subscriber = Subscriber(email=email, name=request.user.username if request.user.is_authenticated else '')
                subscriber.save()

                send_mail(
                    'Thank you for subscribing!',
                    'Thanks for subscribing to Estate Agent. We will be in contact with you.',
                    "Estate Agent",
                    [subscriber.email],
                    fail_silently=False,
                )
                return JsonResponse({'message': 'You have successfully subscribed!'})
        else:
            return JsonResponse({'message': 'Invalid form data.'}, status=400)

    return JsonResponse({'message': 'Invalid request'}, status=400)



def dashboard(request):
    
    enquiries = Enquiry.objects.filter(user_id=request.user.id)
    properties = Property.objects.all()   
    return render(request, 'pages/dashboard.html', {'enquiries':enquiries,'properties':properties});

# def search(request):

#     properties = Property.objects.filter(title__icontains=request.GET['keywords']) | Property.objects.filter(city__state__country__name__icontains=request.GET['keywords']) | Property.objects.filter(address__icontains=request.GET['keywords']) | Property.objects.filter(status__icontains=request.GET['keywords'])

#     return render(request, 'pages/search.html', {'properties':properties})
from django.db.models import Q
def search(request):
    keyword = request.GET.get('keywords', '')

    properties = Property.objects.filter(
        Q(title__icontains=keyword) | 
        Q(city__name__icontains=keyword) |
        Q(state__name__icontains=keyword) |
        Q(country__name__icontains=keyword) | 
        Q(address__icontains=keyword) | 
        Q(status__icontains=keyword)
    )
    
    related_properties = Property.objects.filter(city__in=properties.values('city')).exclude(id__in=properties.values('id'))

    return render(request, 'pages/search.html', {'properties': properties,'related_properties': related_properties})


    
def about(request):
    
    #return HttpResponse('this is about page')
    return render(request, 'pages/about.html');
    
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        if not fullname:
            messages.error(request, 'Please enter your fullname')
            return redirect('contact')

        if not email:
            messages.error(request, 'Please enter your email')
            return redirect('contact')

        if not mobile:
            messages.error(request, 'Please enter your mobile number')
            return redirect('contact')

        if not message:
            messages.error(request, 'Please enter your message')
            return redirect('contact')

        contact = Contact(fullname=fullname, email=email, mobile=mobile, message=message)
        contact.save()
        messages.success(request, 'Thank you for your message. We will get back to you soon.')
        return redirect('contact')

    return render(request, 'pages/contact.html')




# def login(request):

#     if request.method == 'POST':
    
#         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             return redirect('login')

#     return render(request, 'pages/login.html');
import logging
logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username:
            messages.error(request, 'Please enter your username')
            return redirect('login')

        if not password:
            messages.error(request, 'Please enter your password')
            return redirect('login')

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            logger.error(f"Login failed for username: {username}")
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    
    return render(request, 'pages/login.html')


def logout(request):
    
    auth.logout(request)
    return redirect('index')

         
from django.contrib import messages
from .models import UserProfile, Broker
import re

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        registration_type = request.POST.get('registration_type')

        print(f"Registration Type: {registration_type}")

        if not username:
            messages.error(request, 'Please enter your username')
            return redirect('register')
        
        if not email:
            messages.error(request, 'Please enter your email')
            return redirect('register')
        
        if not password:
            messages.error(request, 'Please enter your password')
            return redirect('register')
        
        password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]{6,15}$'
        if not re.match(password_pattern, password):
            messages.error(request, 'Password must be 6 to 15 characters long and contain at least one symbol, one numeric character, and one capital letter')
            return redirect('register')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        profile = UserProfile(registration_type=registration_type)

        if registration_type == 'broker':
            name = request.POST.get('name')
            description = request.POST.get('description')
            broker_img = request.FILES.get('broker_img')
            mobile = request.POST.get('mobile')
            hire_date = request.POST.get('hire_date')
            
            if not name:
                messages.error(request, 'Please enter your full name')
                return redirect('register')
            
            if not description:
                messages.error(request, 'Please enter description')
                return redirect('register')
            
            if not broker_img:
                messages.error(request, 'Please upload broker image')
                return redirect('register')
            
            if not mobile:
                messages.error(request, 'Please enter mobile number')
                return redirect('register')
            
            if not hire_date:
                messages.error(request, 'Please select hire date')
                return redirect('register')
            
            broker = Broker(name=name, email=email, description=description, broker_img=broker_img,
                            mobile=mobile, hire_date=hire_date)
            broker.save()
            
            profile.broker = broker

        profile.save()

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        profile.user = user
        profile.save()
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
        
    return render(request, 'pages/register.html')




from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        if not name:
            messages.error(request, 'Please enter name')
            return redirect('email')
        
        if not email:
            messages.error(request, 'Please enter your email')
            return redirect('email')
        
        if not subject:
            messages.error(request, 'Please enter a subject')
            return redirect('email')

        if not message:
            messages.error(request, 'Please enter a message')
            return redirect('email')

        

        send_mail(
                f'{subject} ({name})',
                f'From: {name} <{email}>\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

        messages.success(request, 'Email sent successfully')
        return redirect('email')

    return render(request, 'pages/email.html')

# view for send_email functionality
# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from realEstate.forms import ContactForm

# def email_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Send email to admin
            # send_mail(
            #     f'{subject} ({name})',
            #     f'From: {name} <{email}>\n\n{message}',
            #     email,
            #     [settings.DEFAULT_FROM_EMAIL],
            #     fail_silently=False,
            # )

#             messages.success(request, 'Thank you for your message. We will get back to you soon.')
#             return redirect('email')
#     else:
#         form = ContactForm()

#     return render(request, 'pages/email.html', {'form': form})

#view for subscribe_us functionality
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.conf import settings
# from .forms import SubscriberForm
# from django.contrib import messages
# from .models import Subscriber

# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscriberForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']

#             # Check if the user is already a subscriber
#             if Subscriber.objects.filter(email=email).exists():
#                 messages.error(request, 'You are already a subscriber.')
#             else:
#                 subscriber = form.save()
#                 send_mail(
#                     'Thank you for subscribing!',
#                     'Thanks for subscribing to Estate Agent. We will be in contact with you.',
#                     "Estate Agent",
#                     [subscriber.email],
#                     fail_silently=False,
#                 )
#                 messages.success(request, 'You have successfully subscribed!')
#             return redirect('subscribe')
#     else:
#         form = SubscriberForm()
#     return render(request, 'pages/subscribe.html', {'form': form})

#api_view
from rest_framework import viewsets 
from pages.models import Subscriber
from pages.serializers import SubscriberSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

#add new property by User's end
from django.shortcuts import render, redirect
from .forms import PropertyForm
from property.models import Property, State, City
from django.contrib import messages

def addproperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            return redirect('index')
    else:
        form = PropertyForm()

    # Auto-select broker for broker user
    if request.user.is_authenticated and request.user.userprofile.registration_type == 'broker':
        form.fields['broker'].initial = request.user.userprofile.broker
        
        # Disable the broker dropdown
        form.fields['broker'].widget.attrs['disabled'] = True

    return render(request, 'pages/addproperty.html', {'form': form})


def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).all()
    return render(request, 'pages/state_dropdown_list_options.html', {'states': states})

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'pages/city_dropdown_list_options.html', {'cities': cities})



