# Generated by Django 5.0.2 on 2024-04-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='award',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='movie_title',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='Award',
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]