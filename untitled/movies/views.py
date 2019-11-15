from django.shortcuts import render , redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Movie, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import TrueUser


def index(request):
    latest_movies_list = Movie.objects.order_by('movie_published_date')[:5]
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




def movie(request, movie_id):
    art = get_object_or_404(Article, pk=movie_id)
    art.numberOfClicks += 1
    art.save()
    comments = showComments(request, movie_id)

    if request.method == 'POST':
        try:
            txt = request.POST.get("comments_text")
            print(request.POST)
            comment = Comments(comments_text=txt,
                                movie=Movie.objects.get(pk=movie_id))
            comment.save()
        except:
            print('the comments cannot be added')
    return render(request, "myFirstApp/article.html", {"article":art,
                                                        "comments":comments})

def search(request):
    try:
        if request.method == "POST":
            print("Post worked ")
            movie_description = request.POST.get("search_field")
            if len(movie_description) > 0:
                search_res = Movie.objects.filter(movie_title__contains=movie_description)
                print(search_res)
                for a in search_res:
                    print(a.movie_title)
                    print(a.movie_description)
            return render(request, "movies/search.html",
                        {"search_res": search_res, "empty_res": "There is no such movie"})
    except:
        return render(request, "movies/search.html",{"empty_res":"There is no such movie"})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} was Born! ')
            redirect('index.html')
    else:
        UserCreationForm(request.POST)
    return render(request, 'registration/register.html', {'form': form})

