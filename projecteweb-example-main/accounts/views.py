from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to the login page after a successful registration
    template_name = "registration/signup.html"  # The template used to render the page


@login_required
def usr_logout(request):
    logout(request)
    return redirect('home')
