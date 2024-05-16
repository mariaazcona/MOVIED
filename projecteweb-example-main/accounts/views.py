from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from movied.models import *




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        self.create_client_for_user(form.instance)
        return super().form_valid(form)

    def create_client_for_user(self, user):
        client = Client(username=user.username)
        client.save()

@login_required
def usr_logout(request):
    logout(request)
    return redirect('home')
