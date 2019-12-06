from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'movies'
urlpatterns = [
path('',views.home, name='home'),
    path('list/', views.index, name='index'),   #/movies
    path('<int:movie_id>/', views.detail, name='detail'),   #/movies/1/
    path('<int:movie_id>/leave_comment/', views.leave_comment, name='leave_comment'),

    path('search/', views.search, name='search'),
path('signup/' , views.signup , name = 'signup'), #/register
#
    
path('profile/' , views.profile , name = 'profile'),
path('logout/' , views.my_logout , name = 'my_logout'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    
]

