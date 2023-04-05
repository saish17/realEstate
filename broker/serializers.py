from rest_framework import serializers 
from broker.models import Broker

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'