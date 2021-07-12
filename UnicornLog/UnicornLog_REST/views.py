#from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Location, Unicorn, Sighting


#views 
def index(request):
    """home page for UnicornLog_REST"""
    return render(request, 'std/index.html')

#TODO .objects method throws error. no idea why
def Locations(request):
    """view the locations page"""
    locations = Locations.
    context = {'locations': locations}
    return render(request, 'std/Locations.html', context)

def Location(request, location_id):
    location = Location.objects.get(id=location_id)
    context = {'Location': location}
    return render(request, 'std/Location.html', context)

def Unicorns(request):
    """view the Unicorns page"""
    unicorns = Unicorn.objects.all()
    context = {'Unicorns': unicorns}
    return render(request, 'std/Unicorns.html', context)

def Unicorn(request, Unicorn_id):
    Unicorn = Unicorns.objects.get(id=Unicorn_id)
    #add sightings foriegn Key
    #sightingsList = Sightings.objects.get(Unicorn_id)
    context = {'Unicorn': Unicorn}
    return render(request, 'std/Unicorn.html', context)    
    
def Sightings(request):
    """view the sightings page"""
    sightings = Sightings.objects.all()
    context = {'sightings': sightings}
    return render(request, 'std/Sightings.html', context)

    
    