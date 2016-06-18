from __future__ import unicode_literals

from django.contrib.gis.db import models
# from django.contrib.auth.models import User


class SpotFix(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    about_event = models.TextField()
    planned_date = models.DateTimeField()
    gear = models.TextField()
    point = models.PointField(default=None)
    contact_number = models.CharField(max_length=18)
    address = models.TextField()
    html = models.TextField()

    def __str__(self):
        spot_fix = '%s: %s --- %s'
        spot_fix = spot_fix % (self.owner, self.title, self.contact_number)
        return spot_fix


class SpotFixReview(models.Model):
    applaud = models.IntegerField()


class Location(models.Model):
    """
    A model which holds information about a particular location
    """
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = models.PointField()
