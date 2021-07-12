from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
#TODO: add 'create' functions for sightings & unicorns

class locationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        label ={'name': ''}

class sightingsForm(forms.ModelForm):
    class Meta:
        model = Sighting
        #need to add the unicorn and the location
        fields = ['description', 'date']
        label = {'description' : Sighting.description, 'date' : ''}

class unicornsForm(forms.ModelForm):
    class Meta:
        pass
        #model = Unicorn
        #fields = ['name', 'color', 'description']
        #label = {'name': Unicorn.name, 'description' : Unicorn.description}
        #widgets = {''}