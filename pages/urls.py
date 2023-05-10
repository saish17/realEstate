from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('email', views.email_view, name='email'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('detail/<int:property_id>', views.detail, name='detail'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('addproperty/', views.addproperty, name='addproperty'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('', include('property.urls')),
    path('admindrop/',include('property.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)