from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from movied.models import *
import requests
import random
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import ReservationForm

API = 'https://api.andrespecht.dev/movies'


def add_movies_api(request):
    response = requests.get(API)

    if response.status_code == 200:
        movie_data = response.json()
        registered_movies = Movie.objects.all()
        for movie_info in movie_data['response']:
            if movie_info['title'] not in registered_movies:
                movie = Movie(
                    name=movie_info['title'],
                    year=str(movie_info['year']),
                    duration=movie_info['runningTime'],
                    price=random.randint(6, 10),
                    overview=movie_info['description'],
                    genre=', '.join(movie_info['genre']),
                    poster=movie_info['poster']
                )
                movie.save()

    return redirect('home')


def add_cinemas(request):
    cinema1 = Cinema(
        name="JCA Cinemes alpicat",
        city="Lleida"
    )
    cinema1.save()
    cinema2 = Cinema(
        name="Cinemes Lauren",
        city="Lleida"
    )
    cinema2.save()
    cinema3 = Cinema(
        name="Espai Funàtic",
        city="Lleida"
    )
    cinema3.save()
    return redirect('home')


def list_movies(request, id_cinema):
    movies = Movie.objects.all()
    return render(request, "list_movies.html", {"movies": movies, "id_cinema": id_cinema})


@login_required(login_url='login')
def movie_reservation(request, id_cinema, id_movie):
    movie = get_object_or_404(Movie, id_movie=id_movie)
    context = {
        'movie': movie,
        'id_cinema': id_cinema
    }

    return render(request, 'movie.html', context)


@login_required(login_url='login')
def confirm_reservation(request, id_cinema, id_movie):
    if request.method == 'POST':
        showtime = request.POST.get('showtime')
        num_people = request.POST.get('num_people')
        movie = get_object_or_404(Movie, id_movie=id_movie)
        cinema = get_object_or_404(Cinema, id_cinema=id_cinema)
        new_reservation = Reservation(
            showtime=int(showtime),
            num_tickets=num_people,
            id_client=request.user,
            movie=movie,
            cinema_id=cinema
        )
        new_reservation.save()
    return redirect('list_movies', id_cinema=id_cinema)


@login_required(login_url='login')
def list_reservations(request):
    reservations = Reservation.objects.filter(id_client=request.user.id)
    return render(request, "list_reservations.html", {"reservations": reservations})


def list_cinemas(request):
    cinemas = Cinema.objects.all()
    return render(request, "list_cinemas.html", {"cinemas": cinemas})


@login_required
def delete_reservation(request, id_reservation):
    reservation = Reservation.objects.get(id_reservation=id_reservation)
    reservation.delete()
    return redirect('list-reservations')


@login_required
def edit_reservation(request, id_reservation):
    reservation = get_object_or_404(Reservation, id_reservation=id_reservation)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully.')
            return redirect('list-reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form})
