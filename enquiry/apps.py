from django.apps import AppConfig


class EnquiryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enquiry'

    def ready(self):
        import enquiry.signals
