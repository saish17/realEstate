from django.contrib import admin

# Register your models here.
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):

  list_display = ('id', 'fullname', 'email', 'subject', 'mobile')
  list_display_links = ('id', 'fullname')
  list_filter = ('fullname',)
  list_editable = ('email', 'mobile')
  search_fields = ('fullname', 'subject', 'email')
  list_per_page = 25
    
    
admin.site.register(Contact, ContactAdmin)