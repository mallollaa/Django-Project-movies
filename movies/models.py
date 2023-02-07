from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model 
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

User = get_user_model()

class Genre(models.Model):
    genre_type = models.CharField(max_length=50)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genres  = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies_genra')
    release_date = models.DateField()
    
    
    # def average_rating(self) -> float: # double check this 
    #     return {self.movie_rating_review}.objects.filter(post=self).aggregate(Avg("rating"))["ratingavg"] or 0

    # def str__(self):
    #     return f"{self.name}: {self.average_rating()}"

class RatingReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rating_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rating_review')
    # rating = models.IntegerField(default=0)
    rating_range = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    review = models.TextField(max_length=150)

class Watchlist(models.Model):
    watchList = models.BooleanField(default=False)
    movies = models.ForeignKey(Movie, on_delete= models.CASCADE , related_name="watchList")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



    

