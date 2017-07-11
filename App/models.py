from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Movie(models.Model):
    actor=models.CharField(max_length=30)
    movie_name=models.CharField(max_length=20)
    Praducer = models.CharField(max_length=30,default=False)
    Director = models.CharField(max_length=30,default=False)
    Catagory = models.CharField(max_length=30,default=False)
    movie_logo=models.FileField()

    def get_absolute_url(self):
	    return reverse('detail', kwargs={'pk':self.pk})
    def __str__(self):
    	return self.actor+ " >>> " + self.movie_name
    
  

class Song(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    song_name = models.CharField(max_length=20)	
    
    def __str__(self):
    	return self.song_name