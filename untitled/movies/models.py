# that thing where we say what will be in our database (like movie title , primere date and etc.)
import datetime
from django.db import models

from django.utils import timezone


class Movie(models.Model):
    movie_title = models.CharField('Movie title', max_length=200)

    movie_imdb = models.FloatField('IMDB score')

    movie_description = models.TextField('Movie Description')

    movie_published_date = models.DateTimeField('published date')

    movie_genre = models.CharField('Movie genres', max_length=200)

    def __str__(self):
        return self.movie_title

    def was_published_resently(self):
        return self.movie_published_date >= (timezone.now() - datetime.timedelta(days=7))


class City(models.Model):
    name = models.CharField('City', max_length=25)
    tag = models.CharField('tag', max_length=25)

    def __str__(self):
        return 'Cities: {}'.format(self.name)


class Cinema(models.Model):
    city_id = models.IntegerField('city_id')
    cinema_name = models.CharField('City', max_length=25)
    cinema_adress = models.CharField('City', max_length=50)


class Ticket(models.Model):
    ticket_name = models.CharField('Ticket name', max_length=20)
    ticket_sum = models.IntegerField('Ticket price')


class Session(models.Model):
    film_id = models.IntegerField("film_id_for_session")
    cinema_id = models.IntegerField("cinema_id_for_session")

    session_date = models.CharField('Session_date', max_length=30)
    session_time = models.CharField('Session_time', max_length=30)
    session_hall = models.CharField('Session hall', max_length=30)


class Comment(models.Model):
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE)  # CASECADE delete all comments when movie will be deleted
    author_name = models.CharField('Author of comment', max_length=50)
    comment_text = models.CharField('Comment', max_length=200)

    def __str__(self):
        return self.author_name
