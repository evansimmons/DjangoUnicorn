from django import forms
from django.db.models import fields
from .models import *

class LocationsForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        label ={'name': ''}

class SightingsForm(forms.ModelForm):
    class Meta:
        model = Sighting
    pass
        
        

class UnicornsForm(forms.ModelForm):
    class Meta:
        model = Unicorn
        fields = ['name', 'Color', 'description']
        label = {'name': Unicorn.name, 'Color': str(Unicorn.color), 'description' : Unicorn.description}