from rest_framework import serializers
from movies.models import Movie ,Genre, RatingReview, Watchlist

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

class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) #specifying here that user field is going to be read only and not inputted through postman
    watched = serializers.BooleanField(read_only=True) #specifying here that user field is going to be read only and not inputted through postman
    class Meta:
        model = Watchlist
        fields = ['watched', 'movies', 'user']