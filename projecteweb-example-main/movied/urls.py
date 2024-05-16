from django.urls import path
from movied import views as v

urlpatterns = [
    path("<int:id_cinema>", v.list_movies, name="list_movies"),
    path("add-movies", v.add_movies_api, name="add_movies"),
    path("add-cinemas", v.add_cinemas, name='add'),
    path("<int:id_cinema>/<int:id_movie>/", v.movie_reservation, name='movie-reservation'),
    path("<int:id_cinema>/create/<int:id_movie>/", v.confirm_reservation, name='confirm-reservation'),
    path("reservations", v.list_reservations, name='list-reservations'),
    path("cinemas", v.list_cinemas, name='list-cinemas'),

]
