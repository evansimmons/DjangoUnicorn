#from django.db import models
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Location, Unicorn, Sighting
from .forms import *

#TODO: add new/edit views & forms for Sightings & Unicorn types

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

@login_required
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

@login_required
def new_unicorn(request):
    pass

@login_required
def edit_unicorn(request):
    pass
    
def sightings(request):
    """view the sightings page"""
    sightings = Sighting.objects.all()
    context = {'sightings': sightings}
    return render(request, 'std/Sightings.html', context)

def sighting(request, sighting_id):
    pass

@login_required
def new_sighting(request):
    '''adds a new sighting'''
    if(request.method != 'POST'):
        #form= SightingForm()
        pass
    else:
        form = None
        #form = SightingForm(data=request.POST)
        if form.is_valid():
            new_sighting =form.save(commit = False)
            new_sighting.witness = request.user
            new_sighting.save()
            return redirect('UnicornLog_REST:index')
    context = {'form': form}
    return render(request, 'std/new_sighting.html', context)

@login_required
def edit_sighting(request, sighting_id):
    '''shows a single sighting'''
    sighting = Sighting.objects.get(id = sighting_id)
    if sighting.witness != request.user:
        raise Http404
    
    pass

    
    