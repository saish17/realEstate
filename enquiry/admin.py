from django.contrib import admin

# Register your models here.
from enquiry.models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    
  list_display = ('id', 'name', 'email', 'phone', 'subject', 'message', 'added_date')
  list_display_links = ('id', 'name', 'subject')
  list_filter = ('name', 'subject',)
  list_editable = ('email', 'phone')
  search_fields = ('name', 'email', 'subject')
  list_per_page = 25
  
admin.site.register(Enquiry, EnquiryAdmin)