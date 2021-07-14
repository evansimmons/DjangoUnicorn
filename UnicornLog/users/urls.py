'''defines url patters for the users app'''

from django.urls import path, include
from . import views
app_name= 'users'
urlpatterns = [
    #default auth urls
    path('', include('django.contrib.auth.urls')),
    #regitration page
    path('register/', views.register, name='register'),
]
