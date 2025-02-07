# Generated by Django 2.2.6 on 2019-11-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20191128_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=20, verbose_name='Ticket name')),
                ('ticket_sum', models.IntegerField(verbose_name='Ticket price')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_picture_url',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_premiere',
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_date', models.DateField(verbose_name='Session_date')),
                ('session_time', models.TimeField(verbose_name='Session_time')),
                ('session_hall', models.IntegerField(verbose_name='Session hall')),
                ('cinema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Cinema')),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Ticket')),
            ],
        ),
    ]
