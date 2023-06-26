import requests
from django.shortcuts import render,redirect
from .models import Pokemon
from django.db.models import Q

# Create your views here.


def pokemons_list(request):
    pokemons = Pokemon.objects.all()
    if request.method == "GET":
        return render(request,"pokemons.html",{
        "pokemons": pokemons
    })
    else:
        buscador = Pokemon.objects.filter(name = request.POST.get('name'))
        print(buscador)
        return render(request,"pokemons.html",{
        "buscador": buscador,
        "pokemons": pokemons
    })