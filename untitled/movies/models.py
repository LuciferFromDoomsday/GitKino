
#that thing where we say what will be in our database (like movie title , primere date and etc.)
import datetime
from django.db import models

from django.utils import timezone

class Movie(models.Model):

    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED,
         'NR - Not Rated'),
        (RATED_G,
         'G - General Audiences'),
        (RATED_PG,
         'PG - Parental Guidance'
         ' Suggested'),
        (RATED_R, 'R - Restricted'),
    )

    movie_title = models.CharField('Movie title',max_length=200)

    movie_imdb = models.FloatField('IMDB score')

    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)

    movie_description = models.TextField('Movie Description')

    movie_published_date = models.DateTimeField('published date')

    movie_genre = models.CharField('Movie genres', max_length=200)




    def __str__(self):
        return self.movie_title

    def was_published_resently(self):
        return self.movie_published_date >= (timezone.now() - datetime.timedelta(days = 7))




class Cities(models.Model):
    name = models.CharField('City',max_length=25)
    tag = models.CharField('tag',max_length=25)


class Cinema(models.Model):
    city_id = models.ForeignKey(Cities,on_delete= models.CASCADE)
    cinema_name = models.CharField('City',max_length=25)
    cinema_adress = models.CharField('City',max_length=50)


class Ticket(models.Model):
    ticket_name = models.CharField('Ticket name',max_length=20)
    ticket_sum = models.IntegerField('Ticket price')



class Sessions(models.Model):
    film_id = models.ForeignKey(Movie,on_delete= models.CASCADE)
    cinema_id = models.ForeignKey(Cinema,on_delete= models.CASCADE)
    ticket_type = models.ForeignKey(Ticket,on_delete=models.CASCADE)

    session_date = models.DateField('Session_date')
    session_time = models.TimeField('Session_time')
    session_hall = models.IntegerField('Session hall')







class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete= models.CASCADE) #CASECADE delete all comments when movie will be deleted
    author_name = models.CharField('Author of comment',max_length=50)
    comment_text = models.CharField('Comment' , max_length=200)

    def __str__(self):
        return self.author_name





