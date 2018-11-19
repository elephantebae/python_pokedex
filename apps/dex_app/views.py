from django.shortcuts import render, redirect
from .models import *
import pokebase as pb

def home(request):
    
    return render(request, 'dex_app/index.html')


def pokedex(request):
    pokedex = []
    for i in range(1,20,1):
        pokedex.append({'id': i,
            'name': pb.pokemon(i).name,
            'type': pb.pokemon(i).types})
    context={
        'pokedex': pokedex,
    }
    return render(request,'dex_app/pokedex.html', context)