from django.shortcuts import render
from .serializers import CreateMovieSerializer ,CreateGenresSerializer, MovieDetailSerializer, RatingReviewSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from movies import models

class CreateMovieView(CreateAPIView):
    #everytime we are deling with database we use queryset 
    queryset = models.Movie.objects.all()
    serializer_class = CreateMovieSerializer
    permission_classes = [IsAdminUser]

class CreateGenresView(CreateAPIView):
    queryset = models.Genre.objects.all()
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
    
 

