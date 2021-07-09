from django import urls
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from UnicornLog_REST import views #TODO: need views for the API.

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
