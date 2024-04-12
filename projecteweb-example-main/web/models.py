from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=100)
    award = models.ManyToManyField('Award')
    release_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    producer = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Award(models.Model):
    award_name = models.CharField(max_length=100)
    award_year = models.IntegerField()

    def __str__(self):
        return self.award_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Name(models.Model):
    actor_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    category = models.CharField(max_length=100)
    awards = models.ManyToManyField('Award')

    def __str__(self):
        return self.actor_name


class Budget(models.Model):
    movie = models.ManyToManyField(Title)
    amount = models.IntegerField()

    def _str_(self):
        return self.movie


class Rating(models.Model):
    movie_title = models.ManyToManyField(Title)
    rating_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    num_votes = models.IntegerField()

    def _str_(self):
        return self.movie_title
