from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),   #/movies
    path('<int:movie_id>/', views.detail, name='detail'),   #/movies/1/
    path('<int:movie_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('search/', views.search, name='search'),
    path('signup/' , views.signup , name = 'signup'), #/register
    path('login/' , views.log_in , name = 'log_in') ,#/login,
    path('profile/' , views.profile , name = 'profile'),
    path('logout/' , views.my_logout , name = 'my_logout')
    
]

