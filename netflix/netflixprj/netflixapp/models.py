from pydoc import describe
from random import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICE = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')

class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(max_length=1000, choices=AGE_CHOICE)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=1000, choices=MOVIE_CHOICES)
    video = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to="flyers")
    age_limit = models.CharField(max_length=1000, choices=AGE_CHOICE)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to="flyers")

    def __str__(self):
        return self.title