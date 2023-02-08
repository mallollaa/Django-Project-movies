from django.shortcuts import render
from .serializers import CreateMovieSerializer ,CreateGenresSerializer, MovieDetailSerializer, RatingReviewSerializer, WatchListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView ,UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from movies import models
from rest_framework import serializers

class CreateMovieView(CreateAPIView):
    #everytime we are deling with database we use queryset 
    queryset = models.Movie.objects.all()
    serializer_class = CreateMovieSerializer
    permission_classes = [IsAdminUser]

class CreateGenresView(CreateAPIView):
    serializer_class = CreateGenresSerializer
    # Only admins can create genres, so we use IsAdminUser for the required permission
    permission_classes = [IsAdminUser] 



class MovieDetailView(ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = MovieDetailSerializer
    # Only authenticed users can view details of movie, so we use IsAuthenticated for the required permission
    permission_classes = [IsAuthenticated]


class CreateRatingReviewView(CreateAPIView):
    queryset = models.RatingReview.objects.all()
    serializer_class = RatingReviewSerializer
    # Only admins can create genres, so we use IsAdminUser for the required permission
    permission_classes = [IsAuthenticated] 

class WatchListView(CreateAPIView):
    serializer_class = WatchListSerializer
    # Only admins can create genres, so we use IsAdminUser for the required permission
    def perform_create(self, serializer):
        movie = models.Movie.objects.get(id=self.kwargs["movie_id"])
        serializer.save(user=self.request.user,movies=movie) #grabbing user from token by accessing it from user that's within the request object in self 
        
    
    
   