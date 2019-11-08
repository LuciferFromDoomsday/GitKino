from django.shortcuts import render
from movies.models import Movie, Comment


def index(request):
    list_of_latest_movies = Movie.objects.order_by('-')
    return render(request, 'movies/list.html')