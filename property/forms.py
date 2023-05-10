from django import forms
from .models import Property, Country, State, City

class ExcelFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.xlsx, .xls'}))


