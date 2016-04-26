from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class SpotFix(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='spotfix')
    title = models.CharField(max_length=100)
    about_event = models.TextField()
    planned_date = models.DateTimeField()
    gear = models.TextField()
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=18)
    address = models.TextField()
    html = models.TextField()

    def __str__(self):
        spot_fix = '%s: %s --- %s'
        spot_fix = spot_fix % (self.owner, self.title, self.contact_number)
        return spot_fix


class SpotFixReview(models.Model):
    applaud = models.IntegerField()
