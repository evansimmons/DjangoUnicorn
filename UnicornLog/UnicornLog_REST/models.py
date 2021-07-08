from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
#from django_countries.fields import CountryField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.

class Location(models.Model):
    """the location of a sighting"""
    name = models.CharField(max_length=255)
#    country = CountryField()
    def __str__(self):
        """returns thy self as text"""
        return self.text    

class Unicorn(models.Model):
    """this is a Unicorn"""
    name = models.CharField(max_length=255)
    class Color(models.TextChoices):
        white = "White"
        gray = "Gray"
        black = "black"
        Sparkle= "Sparkle"
        rainbow = "Rainbow"
    color = Color.choices
    RainbowPoop = models.BooleanField(default=False)
    description = models.TextField()
    def __str__(self):
        """returns thy self as text"""
        return self.text

class Sighting(models.Model):
    """an individual sighting of a unicorn"""
    location = models.ForeignKey(Location, on_delete=CASCADE)
    description = models.TextField()
    unicorn = models.ForeignKey(Unicorn, on_delete=CASCADE)
    date = models.DateField(("%m/%d/%Y"), auto_now=False, auto_now_add=False)
    def __str__(self):
        """returns thy self as text"""
        return self.text
