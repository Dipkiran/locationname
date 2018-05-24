from django.conf import settings
from django.db import models
from django.urls import reverse


#image table
class tree(models.Model):
    mainlocation = models.CharField(max_length=120)
    othername = models.CharField(max_length=120)


class information(models.Model):
    location = models.CharField(max_length=120)
    death = models.CharField(max_length=120)
