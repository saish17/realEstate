from django.contrib import admin
from property.models import Property,City,State,Country
from broker.models import Broker


# class PropertyAdmin(admin.ModelAdmin):
    
#   list_display = ('id', 'title', 'address', 'city', 'state', 'description', 'price')
#   list_display_links = ('id', 'title')
#   list_filter = ('title',)
#   list_editable = ('address', 'city', 'state', 'description', 'price')
#   search_fields = ('title', 'address', 'description')
#   list_per_page = 25
    
# admin.site.register(Property, PropertyAdmin)



from import_export.admin import ImportExportModelAdmin
from .resources import BrokerResource, PropertyResource
@admin.register(Broker)
class BrokerAdmin(ImportExportModelAdmin):
    resource_class = BrokerResource

@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):
    list_display = ('title', 'address', 'city','is_published', 'price')
    list_display_links = ('title',)
    resource_class = PropertyResource
    class Media:
        js = ('assets/js/ajax.js',)







admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)