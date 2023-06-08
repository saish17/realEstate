from django.contrib import admin
from . models import Subscriber,UserProfile
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','name','date_created']
admin.site.register(Subscriber,SubscriberAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','registration_type',]
admin.site.register(UserProfile,UserProfileAdmin)