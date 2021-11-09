from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    long = models.URLField(max_length=1000)
    short = models.CharField(max_length=20)
    author = models.ManyToManyField(User)
