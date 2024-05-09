from django.urls import path

from .views import SignUpView, usr_logout

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", usr_logout, name="logout"),
]
