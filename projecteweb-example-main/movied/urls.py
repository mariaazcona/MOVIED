from django.urls import path
from movied import views as v


urlpatterns = [
    path("cinema/<int:id>/", v.cinema_detail, name='cinema-detail'),
]