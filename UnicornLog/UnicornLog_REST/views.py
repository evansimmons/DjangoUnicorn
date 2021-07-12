#from django.db import models
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from .models import Location, Unicorn, Sighting
from .forms import *


#views 
def index(request):
    """home page for UnicornLog_REST"""
    return render(request, 'std/index.html')

#TODO does not print the location name, needs fix
def locations(request):
    """view the locations page"""
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'std/Locations.html', context)

def location(request, location_id):
    location = Location.objects.get(id=location_id)
    context = {'Location': location.name}
    return render(request, 'std/Location.html', context)

def new_location(request):
    '''add a new location'''
    if request.method != 'POST':
        form = locationForm()
    else:
        #POST data is submitted, time to process
        form = locationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('UnicornLog_REST:locations')
    context = {'form': form}
    return render(request, 'std/new_location.html', context)
        
def unicorns(request):
    """view the Unicorns page"""
    unicorns = Unicorn.objects.all()
    context = {'Unicorns': unicorns}
    return render(request, 'std/Unicorns.html', context)

def unicorn(request, Unicorn_id):
    unicorn = Unicorn.objects.get(id=Unicorn_id)
    #add sightings foriegn Key
    #sightingsList = Sightings.objects.get(Unicorn_id)
    context = {'Unicorn': unicorn}
    return render(request, 'std/Unicorn.html', context)    
    
def sightings(request):
    """view the sightings page"""
    sightings = Sighting.objects.all()
    context = {'sightings': sightings}
    return render(request, 'std/Sightings.html', context)

    
    