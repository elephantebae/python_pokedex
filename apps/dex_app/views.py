from django.shortcuts import render, redirect
from .models import *
import pokebase as pb

# Create your views here.
def home(request):
    
    return render(request, 'dex_app/index.html')