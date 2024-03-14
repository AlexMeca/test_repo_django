from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import CreateUserForm


class LoginUserView(LoginView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('home-page')


class UserChangePasswordView(PasswordChangeView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('serviciu-all')


class CreateUserView(CreateView):
    template_name = "authentication/form.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('serviciu-all')


class LogOutUserView(LogoutView):
    success_url = reverse_lazy('serviciu-all')
