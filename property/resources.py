from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from property.models import Property
from broker.models import Broker

class BrokerResource(resources.ModelResource):
    class Meta:
        model = Broker
        fields = ('id','name')

class PropertyResource(resources.ModelResource):
    broker = fields.Field(
        column_name='broker',
        attribute='broker',
        widget=ForeignKeyWidget(Broker,'name')
    )

    class Meta:
        model = Property
        fields = ('id','broker','title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'plot_size', 'status','photo_main','photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published')
