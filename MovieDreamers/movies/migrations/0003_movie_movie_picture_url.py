# Generated by Django 2.2.6 on 2019-10-31 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_movie_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_picture_url',
            field=models.CharField(default=datetime.date.today, max_length=200, verbose_name='movie_picture_url'),
            preserve_default=False,
        ),
    ]
