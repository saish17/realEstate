from django.contrib import admin

# Register your models here.
from property.models import Property

class PropertyAdmin(admin.ModelAdmin):
    
  list_display = ('id', 'title', 'address', 'city', 'state', 'description', 'price')
  list_display_links = ('id', 'title')
  list_filter = ('title',)
  list_editable = ('address', 'city', 'state', 'description', 'price')
  search_fields = ('title', 'address', 'description')
  list_per_page = 25
    
admin.site.register(Property, PropertyAdmin)