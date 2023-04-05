from django import forms
from .models import Subscriber
from property.models import Property

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email','name',]

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['broker','title','address','city','state','zipcode','description','price','bedrooms','bathrooms','garage','sqft','plot_size','status','photo_main']
        widgets = {
            'photo_main': forms.ClearableFileInput(attrs={'multiple': True}),
        }