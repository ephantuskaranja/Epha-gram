from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profileimages/')
    bio = models.TextField(max_length=100)
    user = models.ForeignKey(User)


    def __str__(self):
        return self.gram_name

class Pictures(models.Model):
    picture = models.ImageField(upload_to='profileimages/')
    user = models.ForeignKey(User)
    gram_name = models.CharField(max_length=30)
