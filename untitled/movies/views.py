from django.shortcuts import render , redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Movie, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings

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

    m.comment_set.create(author_name= user.username , comment_text=request.POST['text'])

    return HttpResponseRedirect( reverse('movies:detail' , args =(m.id,)))






def search(request):
    
        search_res = []
        if request.method == "POST":
            print("Post worked ")
            movie_description = request.POST.get("input")
            print(movie_description)
            if len(movie_description) > 0:
                search_res = Movie.objects.filter(movie_title__contains=movie_description)
                print(search_res)
                print(search_res[0].movie_imdb)
            return render(request, "movies/search.html",
                        {"search_res" : search_res , "empty_res":"There is no such movie1"})



def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():

        form.save()
    username = form.cleaned_data.get('username')
    my_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=my_password)
    login(request, user)
    return render(request, 'home.html', {'user':user})
  else:
    form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
  
  

def log_in(request):
        print("LOGED")

        username = request.POST.get("username")
        my_password = request.POST.get("pass")
        print(username)
        print(my_password)
        user = authenticate(username=username, password=my_password)
        if user is not None:
            print("cond 1")
            if user.is_active:
                login(request,user)
                print("cond 2")
                return redirect('home.html')
            else:
                print("else 2")
                return render(request, 'registration/login.html')
        else:
              print("else 1")
              return render(request , 'registration/login.html' )


def profile(request):
    return render(request, "registration/user_profile.html")


def my_logout(request):
    redirect('home.html')
    return auth_views.logout(request)