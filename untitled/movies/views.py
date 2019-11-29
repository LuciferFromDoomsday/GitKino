from django.shortcuts import render , redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Movie, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

def index(request):
    latest_movies_list = Movie.objects.order_by('movie_published_date')[:12]
    print(latest_movies_list[0].movie_title)
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
            movie_description = request.POST.get("input")
            print(movie_description)
            if len(movie_description) > 0:
                search_res = Movie.objects.filter(movie_title__contains=movie_description)
                print(search_res)
            return render(request, "movies/search.html",
                        {"search_res" : search_res ,  "empty_res":"There is no such movie"})
    except:
        return render(request, "movies/search.html",{ "empty_res":"There is no such movie"})


def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    username = form.cleaned_data.get('username')
    my_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=my_password)
    login(request, user)
    return redirect('home.html')
  else:
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



