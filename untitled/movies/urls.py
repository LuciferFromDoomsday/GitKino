from django.urls import path
from .import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),   #/movies
    path('<int:movie_id>/', views.detail, name='detail'),   #/movies/1/
    path('<int:movie_id>/leave_comment/', views.leave_comment, name='leave_comment'),

    path('search/', views.search, name='search'),
path('register/' , views.register , name = 'register'), #/register
]

