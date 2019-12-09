from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Movie, Comment, Cities, Cinema, Ticket, Sessions
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import smtplib

def home(request):

    needed_cinemas = None
    needed_movies = []
    movies_list = Movie.objects.order_by("movie_published_date")[:6]

    cities_list = Cities.objects.all()
    cinemas = Cinema.objects.all()
    if request.method == "POST":
        cities_list = Cities.objects.all()
        cinemas = Cinema.objects.all()
        city = request.POST.get('city')
        print(city)
        # city = "Алматы"
        needed_city = Cities.objects.filter(name=city)
        print(needed_city)
        city_id=needed_city[0].id
        print(city_id)
        if needed_city is not None:
            print("found needed city")

            needed_cinemas = Cinema.objects.filter(city_id=city_id)
            for i in range(len(needed_cinemas)):
                print(needed_cinemas[i].cinema_name)

            cinema = request.POST.get('cinema')
            chosen_cinema = Cinema.objects.filter(cinema_name=cinema)
            chosen_cinema_id = chosen_cinema[0].theatre_id
            print(chosen_cinema_id)
            needed_sessions = Sessions.objects.filter(cinema_id=chosen_cinema_id)


            print(needed_sessions)
            for i in range(len(needed_sessions)):
                needed_movies += Movie.objects.filter(film_id=needed_sessions[i].film_id)


            print(needed_movies)


            return render(request,'home.html', {'cinemas': needed_cinemas , 'cities' : cities_list, 'sessions' : needed_sessions, 'movies':needed_movies})

    return  render(request,'home.html', {'cities' : cities_list , 'cinemas': cinemas , 'movies_list': movies_list})




def index(request):
    latest_movies_list = Movie.objects.order_by('movie_published_date')[:12]
    cities_list = Cities.objects.all()
    print(latest_movies_list[0].movie_title)
    return render(request, 'movies/list.html', {'latest_movies_list': latest_movies_list, 'cities_list' : cities_list})


def detail(request, movie_id):
    try:
        m = Movie.objects.get(id=movie_id)
    except:
        raise Http404("No such movie")

    latest_comment_list = m.comment_set.order_by('-id')[:10]

    return render(request, 'movies/detail.html', {'movie': m, 'latest_comment_list': latest_comment_list})


def leave_comment(request, movie_id):
    try:
        user = request.user
        m = Movie.objects.get(id=movie_id)
    except:
        raise Http404("No such movie")

    m.comment_set.create(author_name=user.username, comment_text=request.POST.get('text'))

    return HttpResponseRedirect(reverse('movies:detail', args=(m.id,)))


def search(request):
    search_res = []
    if request.method == "POST":
        print("Post worked ")
        movie_description = request.POST.get("input")
        print(movie_description)
        if len(movie_description) > 0:
            search_res = Movie.objects.filter(movie_title__contains=movie_description)
        return render(request, "movies/search.html",
                      {"search_res": search_res, "empty_res": "There is no such movie1"})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#         username = form.cleaned_data.get('username')
#         my_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=my_password)
#         login(request, user)
#         return render(request, 'home.html', {'user': user})
#     else:
#
#         return auth_views.signin(request)





def profile(request):

    return render(request, "registration/user_profile.html")


def my_logout(request):
    redirect('home.html')
    return auth_views.logout(request)


# def cities_list(request):
#     cities_list = Cities.objects.all()
#     return render(request,'home.html', {'cities_list' : cities_list})

def email_sender(input_message, email_to, client):
    ''' function to send email '''
    to = email_to
    gmail_user = 'ayannaimankhan@gmail.com' ## email of sender account
    gmail_pwd = 'Superpassword' ## password of sender account
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' +'Subject:Authenticate your account For MovieDreamers.com! \n'
    input_message = input_message + client
    msg = header + input_message
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
    print("EMAIL SENT")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/acc_active_html.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email_sender(message, to_email, user.username)
            email.send()
            print("email sent to" + user.email)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, "home.html")
    else:
        return ('Activation link is invalid!')

# def logout(request):

# def cinemas_list(request):
#     print("-----____________________----------")
#     needed_cinemas = []
#     if request.method == "POST":
#         city = request.POST.get("cinemas")
#         if city.is_valid():
#             needed_cinemas = Cinema.objects.filter(city_id__contains=city)
#         return render(request, "home.html", {'cinemas': needed_cinemas})
#
#     else:
#         return render(request,"home.html", {'cinemas': needed_cinemas , 'empty_ans' : "No cinema here((("})
#

# def buy_ticket(request, session_id):
#     if request.method == "POST":
#
