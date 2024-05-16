from django.contrib import admin
from .models import Movie, Reservation, Cinema

admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Cinema)
