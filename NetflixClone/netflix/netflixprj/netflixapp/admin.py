from django.contrib import admin
from . models import Video, Movie, Profile, CustomUser

admin.site.register(CustomUser)
admin.site.register(Video)
admin.site.register(Movie)
admin.site.register(Profile)