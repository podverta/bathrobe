from django.shortcuts import render
from django.views.generic import ListView
from .models import Bathrobe

class BathrobeLisView(ListView):
    model = Bathrobe
    template_name = 'bb/index.html'

# Create your views here.
