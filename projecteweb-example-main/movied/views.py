from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import *
import requests

API = 'https://api.andrespecht.dev/movies'


@login_required(login_url='login')
def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"cinemas": movies})
