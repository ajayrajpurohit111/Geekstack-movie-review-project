from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime
class Movie(models.Model):

    name=models.CharField(max_length=300)
    director=models.CharField(max_length=300)
    cast=models.CharField(max_length=300)
    plot=models.CharField(max_length=400)
    description=models.TextField(max_length=5000)
    date=models.DateField(default=datetime.now, blank=True)
    averageRating=models.FloatField(default=0)
    image=models.URLField( default=None,null=True,max_length=400)
    video=EmbedVideoField(null=True,blank=True)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=1000)
    rating=models.FloatField(default=0)

    def __str__(self):
        return self.user.username
