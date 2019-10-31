from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Movie, Comment


def index(request):
    latest_movies_list = Movie.objects.order_by('movie_published_date')[:2]
    return render(request, 'movies/list.html', {'latest_movies_list': latest_movies_list})


def detail(request, movie_id):
    try:
        m = Movie.objects.get(id=movie_id)
    except:
        raise Http404("No such movie")

    latest_comment_list = m.comment_set.order_by('-id')[:10]

    return render(request, 'movies/detail.html', {'movie': m , 'latest_comment_list': latest_comment_list})


def leave_comment(request, movie_id):
    try:
        m = Movie.objects.get(id=movie_id)
    except:
        raise Http404("No such movie")

    m.comment_set.create(author_name= request.POST['name'] , comment_text=request.POST['text'])

    return HttpResponseRedirect( reverse('movies:detail' , args =(m.id,)))

