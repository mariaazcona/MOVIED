import os
import django
import sqlite3

# Configurar la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import *


def populate_cinemas():
    cinemas = [
        {
            'name': 'JCA Cinemes',
            'phone': '123456',
            'email': 'jcacinemes@gmail.com',
            'website': 'www.jcacinemes.com',
            'city': 'Lleida',

        },
    ]

    for cinema in cinemas:
        Cinema.objects.create(
            name=cinema['name'],
            phone=cinema['phone'],
            email=cinema['email'],
            website=cinema['website'],
            city=cinema['city'],
        )


def populate_clients():
    clients = [
        {
            'username': 'neusfdez',
            'name': 'Neus',
            'phone': '11111111',
            'email': 'neus@gmail.com',
            'card_number': '0000111122223333'
        },
    ]

    for client in clients:
        Client.objects.create(
            username=client['username'],
            name=client['name'],
            phone=client['phone'],
            email=client['email'],
            card_number=client['card_number']
        )

def populate_movies():
    movies = [
        {
            'cinema': 'JCA Cinemes',
            'name': 'Toy story',
            'price': '10',
            'overview': 'Sinopsis de la peli...',
            'genre': 'Fantasy',
            'ranking' : '8',
        },
    ]

    for movie in movies:
        cinema = Cinema.objects.get(name=movie['cinema'])
        Movie.objects.create(
            id_cinema=cinema,
            name=movie['name'],
            price=movie['price'],
            overview=movie['overview'],
            genre=movie['genre'],
            ranking=movie['ranking']
        )

populate_cinemas()
populate_clients()
populate_movies()