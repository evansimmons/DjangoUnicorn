from django.contrib import admin
from .models import Location, Sighting, Unicorn
# Register your models here.
admin.site.register(Location)
admin.site.register(Sighting)
admin.site.register(Unicorn)