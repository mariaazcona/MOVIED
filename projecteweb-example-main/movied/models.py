from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


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


class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_reservation


class ReservationMovie(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    id_reservation = models.AutoField(primary_key=True)
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    num_tickets = models.IntegerField(default=None)
