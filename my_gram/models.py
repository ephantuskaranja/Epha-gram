from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profileimages/')
    bio = models.TextField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User)
    email=models.EmailField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.bio

    def save_bio(self):
        self.save()



class Pictures(models.Model):
    picture = models.ImageField(upload_to='profileimages/')
    user = models.ForeignKey(User)
    gram_name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    @classmethod
    def get_pictures(cls):
       pics = cls.objects.all()
       return pics

    def __str__(self):
        return self.gram_name

    def save_photo(self):
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(User)
    picture = models.ForeignKey(Pictures)
    comment_text = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_text

    def save_comment(self):
        self.save()
