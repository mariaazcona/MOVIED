from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import *
import requests
import random
from django.http import HttpResponse
from django.contrib.auth.models import User

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


def list_movies(request):
    movies = Movie.objects.all()
    return render(request, "list_movies.html", {"movies": movies})


@login_required(login_url='login')
def movie_reservation(request, id_movie):
    movie = get_object_or_404(Movie, id_movie=id_movie)
    context = {
        'movie': movie,
    }

    return render(request, 'movie.html', context)


@login_required(login_url='login')
def confirm_reservation(request, id_movie):
    if request.method == 'POST':
        showtime = request.POST.get('showtime')
        num_people = request.POST.get('num_people')
        movie = get_object_or_404(Movie, id_movie=id_movie)
        new_reservation = Reservation(
            showtime=int(showtime),
            num_tickets=num_people,
            id_client=request.user,
            movie=movie,
        )
        new_reservation.save()
    return redirect('list_movies')


@login_required(login_url='login')
def list_reservations(request):
    reservations = Reservation.objects.filter(id_client=request.user.id)
    return render(request, "list_reservations.html", {"reservations": reservations})
