from django.urls import path
from movied import views as v


urlpatterns = [
    path("", v.list_movies, name="list_movies"),
    path("add-movies", v.add_movies_api, name="add_movies"),
    path("<int:id_movie>/", v.movie_reservation, name='movie-reservation'),
]