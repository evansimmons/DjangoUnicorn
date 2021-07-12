"""defines url patters for UnicornLog_REST"""
from django.urls import path
from . import views

app_name = 'UnicornLog_REST'
urlpatterns = [
    #home page
    path('', views.index, name= 'index'),
    path('index/', views.index, name = 'index'),
    path('Index/', views.index, name = 'index'),
   
    #Unicorns page
    path('unicorns/', views.unicorns, name = 'unicorns'),
    path('Unicorns/', views.unicorns, name = 'unicorns'),
    #path('unicorns/<int:unicorn_id>', views.Unicorns, name= 'Unicorns'),
    #Sightings page
    path('Sightings/', views.sightings, name = 'sightings'),
    path('sightings/', views.sightings, name = 'sightings'),
    #path('sightings/<int:sighting_id>', views.Sightings, name= 'Sightings'),
    #Locations page
    path('Locations/', views.locations, name='locations'),
    path('locations/', views.locations, name = 'locations'),
    
    #view location_id
    path('location/<int:location_id>', views.location, name= 'location'),
    path('Location/<int:location_id>', views.location, name= 'location'),
    
    #overview page
]
