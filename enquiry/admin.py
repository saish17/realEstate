from django.contrib import admin
from enquiry.models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
  
  list_display = ('id', 'name', 'email', 'phone', 'subject', 'message', 'added_date')
  list_display_links = ('id', 'name', 'subject')
  list_filter = ('name', 'subject','added_date')
  list_editable = ('email', 'phone')
  search_fields = ('name', 'email', 'subject','added_date')
  list_per_page = 25
  date_hierarchy = 'added_date'

       
admin.site.register(Enquiry, EnquiryAdmin)