from django.contrib import admin
from .models import Movie, Reservation, Client, ReservationMovie

admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Client)
admin.site.register(ReservationMovie)
