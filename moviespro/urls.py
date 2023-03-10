"""moviespro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_view
from movies import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', user_view.RegisterView.as_view(), name='register'),
    path('api/login/', user_view.LoginView.as_view(), name='login'),
    path('api/movie/create/',views.CreateMovieView.as_view(), name='movie_create'),
    path('api/genre/create/', views.CreateGenresView.as_view(), name='genre'),
    path('api/movie/detail/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('api/rate/view', views.CreateRatingReviewView.as_view(), name='review'),
    path('api/watchlist/add/<int:movie_id>/', views.WatchListView.as_view(), name='watchlist_add'),
    ]

