from django.urls import path,include
from property.views import PropertyViewSet
from enquiry.views import EnquiryViewSet
from broker.views import BrokerViewSet
from pages.views import SubscriberViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'property',PropertyViewSet)
router.register(r'broker',BrokerViewSet)
router.register(r'enquiry',EnquiryViewSet)
router.register(r'subscriber',SubscriberViewSet)



urlpatterns = [
    path('', include(router.urls)),
  
]