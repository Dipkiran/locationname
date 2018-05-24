from django import forms
from .models import *

class LocationForm(forms.ModelForm):
    location = forms.CharField(max_length=120)
    death = forms.CharField(max_length=120)

    class Meta:
        model = information
        fields = ('location','death' )
