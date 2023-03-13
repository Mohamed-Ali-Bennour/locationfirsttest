from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=50)
    is_online = models.BooleanField(default=False)


class Locations (models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='location')


    latitude = models.FloatField()
    longitude = models.FloatField()


