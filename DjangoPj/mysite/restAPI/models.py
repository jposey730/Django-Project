from __future__ import unicode_literals

from django.db import models

class Place(models.Model):
    zipcode=models.CharField(max_length=15)
    state=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    def __unicode__(self):
        return self.state



