from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Movie(models.Model):
    id_movie = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    duration = models.CharField(max_length=10, default="-")
    price = models.CharField(max_length=50)
    overview = models.CharField(max_length=500)
    genre = models.CharField(max_length=50)
    poster = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    id_cinema = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None, null=True)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    num_tickets = models.IntegerField(default=None)
    showtime = models.IntegerField(default=None)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return str(self.id_reservation)
