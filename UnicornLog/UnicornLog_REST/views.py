from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User, Group


#views 
def index(request):
    """home page for UnicornLog_REST"""
    return render(request, 'std/index.html')

def Locations(request):
    """view the locations page"""
    return render(request, 'std/Locations.html')

def Unicorns(request):
    """view the Unicorns page"""
    return render(request, 'std/Unicorns.html')

def Sightings(request):
    """view the sightings page"""
    return render(request, 'std/Sightings.html')

    
    