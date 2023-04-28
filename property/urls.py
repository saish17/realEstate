from django.urls import path,include
from property.views import PropertyViewSet
from enquiry.views import EnquiryViewSet
from broker.views import BrokerViewSet
from pages.views import SubscriberViewSet
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'property',PropertyViewSet)
router.register(r'broker',BrokerViewSet)
router.register(r'enquiry',EnquiryViewSet)
router.register(r'subscriber',SubscriberViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('excel/', views.export_data_to_excel, name='excel'),
    path('fromexcel/', views.import_data_from_excel, name='fromexcel'),

  
]