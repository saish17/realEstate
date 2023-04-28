# from django import forms
# from django.core import validators

# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     subject = forms.CharField()
#     message = forms.CharField()
#     email = forms.EmailField()
#     sender = forms.EmailField()
#     recipient = forms.EmailField()

#     def clean(self):
#         total_cleaned_data=super().clean()

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class PropertyForm(forms.Form):
    file = forms.FileField()

 
