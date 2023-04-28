from django.contrib import admin

# Register your models here.
from broker.models import Broker

class BrokerAdmin(admin.ModelAdmin):
    
  list_display = ('id', 'name', 'email', 'description', 'mobile', 'broker_img', 'photo_1', 'photo_2', 'photo_3')
  list_display_links = ('id', 'name')
  list_filter = ('name',)
  list_editable = ('email', 'mobile')
  search_fields = ('name', 'description', 'email')
  list_per_page = 25
    
# admin.site.register(Broker, BrokerAdmin)