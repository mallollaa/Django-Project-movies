from rest_framework import serializers
from movies.models import Movie ,Genre, RatingReview

class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name', 'genres' ,'release_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name', 'genres' ,'release_date']
        

class CreateGenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_type']

class RatingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingReview
        fields = ['id', 'rating_range', 'review', 'movie', 'user'] # ask about id and its relations (user, movie)

