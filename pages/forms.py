from django import forms
from .models import Subscriber
from property.models import Property,City,State

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email','name',]

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['broker','title','address','country','state','city','zipcode','description','price','bedrooms','bathrooms','sqft','plot_size','status','photo_main']
        widgets = {
            'photo_main': forms.ClearableFileInput(attrs={'multiple': True}),
            'country': forms.Select(attrs={ 'class': 'form-select' }),
            'state': forms.Select(attrs={ 'class': 'form-select' }),
            'city': forms.Select(attrs={ 'class': 'form-select' }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

    
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.city_set.order_by('name')