from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Advisor(models.Model):
    name = models.CharField(max_length=50)
    photo_url = models.URLField()