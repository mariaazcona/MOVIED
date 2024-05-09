from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import *
import requests

API = 'https://api.andrespecht.dev/movies'


# Cinemas
def cinema_list(request):
    all_cinemas = Cinema.objects.all()
    return render(request, "cinemas.html", {"cinemas": all_cinemas})


def cinema_detail(request, id):
    cinema = get_object_or_404(Cinema, id_cinema=id)
    movies = Movie.objects.filter(id_cinema=cinema)
    context = {
        'cinema': cinema,
        'movies': movies
    }
    return render(request, 'cinema.html', context)


@login_required(login_url='login')
def home(request):
    all_cinemas = Cinema.objects.all()
    return render(request, "home.html", {"cinemas": all_cinemas})
