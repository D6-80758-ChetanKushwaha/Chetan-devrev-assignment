from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    descrip = models.TextField()
    imdb_rate = models.DecimalField(max_digits=4,decimal_places=2)
    date = models.DateField() # launch date...
    tic_no = models.IntegerField() #No of tickets left..
    threater = models.CharField(max_length=100,default="Alka Threater")

    def __str__(self):
        return self.title

class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    m_id = models.ForeignKey(Movie, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.m_id)

