from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView

from servicii.models import ServiciiModel


def home(request):
    return render(request, template_name='home/home.html', context={})


class HomeView(ListView):
    template_name = 'home/home.html'
    model = ServiciiModel #Select ALL pentru ca mostenesc ListView





