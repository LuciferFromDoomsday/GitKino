# Generated by Django 2.2.6 on 2019-12-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_auto_20191208_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='session_id',
            field=models.IntegerField(default=0, verbose_name='session_id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sessions',
            name='ts',
            field=models.IntegerField(default=0, verbose_name='ts'),
            preserve_default=False,
        ),
    ]
