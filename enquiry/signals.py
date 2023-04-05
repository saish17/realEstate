from .models import Enquiry
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Enquiry)
def send_inquiry_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Enquiry for Property'
        message = f'A new inquiry has been submitted for the property "{instance.property.title}".\n\n'
        message += f'Name: {instance.name}\n'
        message += f'Email: {instance.email}\n'
        message += f'Message: {instance.message}\n'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['saishyeole1707@gmail.com']  
        send_mail(subject, message, from_email, recipient_list)