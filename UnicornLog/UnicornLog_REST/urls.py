"""defines url patters for UnicornLog_REST"""
from django.urls import path
from . import views

app_name = 'UnicornLog_REST'
urlpatterns = [
    #home page
    path('', views.index, name= 'index'),
    path('index/', views.index, name = 'index'),
    path('Index/', views.index, name= 'index'),
   
    #Unicorns page
    path('unicorns/', views.Unicorns, name = 'Unicorns'),
    path('Unicorns/', views.Unicorns, name = 'Unicorns'),
    
    #Sightings page
    path('Sightings/', views.Sightings, name = 'Sightings'),
    path('sightings/', views.Sightings, name = 'Sightings'),
    
    #Locations page
    path('Locations/', views.Locations, name='Locations'),
    path('locations/', views.Locations, name = 'Locations'),
    
    #overview page
]
