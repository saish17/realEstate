from django import forms

class ExcelFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.xlsx, .xls'}))
