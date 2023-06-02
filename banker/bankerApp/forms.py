# forms.py
from django import forms
from .models import Country, City

class MyForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
