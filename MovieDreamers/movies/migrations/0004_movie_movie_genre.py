# Generated by Django 2.2.6 on 2019-11-28 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_movie_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_genre',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Movie genres'),
            preserve_default=False,
        ),
    ]
