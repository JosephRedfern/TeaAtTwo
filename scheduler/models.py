from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Event(models.Model):
    baker = models.ForeignKey(User, null=True)
    date = models.DateTimeField()
    location = models.ForeignKey('Location')
    confectionary = models.ForeignKey('Confectionary', null=True)

class Confectionary(models.Model):
    variety = models.ForeignKey('ConfectionaryType', null=True)
    flavour = models.ForeignKey('ConfectionaryFlavour', null=True)
    gluten_free = models.BooleanField(default=False)
    lactose_free = models.BooleanField(default=False)

    
class ConfectionaryType(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class ConfectionaryFlavour(models.Model):
    name = models.TextField()

class Location(models.Model):
    name = models.TextField(null=False)

class Review(models.Model):
    user = models.ForeignKey(User, null=True)
    event = models.ForeignKey('Event')
    rating = models.FloatField()
