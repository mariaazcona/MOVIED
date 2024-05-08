from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Cinema(models.Model):
    name = models.CharField(max_length=50)
    id_cinema = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)


class Movie(models.Model):
    id_movie = models.AutoField(primary_key=True)
    id_cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    overview = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    ranking = models.FloatField(max_length=50, null=True)


class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)


class ReservationMovie(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    id_reservation = models.AutoField(primary_key=True)
    id_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)  # Hacer el campo nullable si es necesario
    num_tickets = models.IntegerField()
