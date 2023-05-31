from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.
def categoria(request):
    categoria = Categorias.objects.all()
    return render(request,"categorias.html",{
        "categoria":categoria
    })
    
def publicacion(request):
    categoria = Categorias.objects.all()
    publicacion = Publicaciones.objects.all()
    return render(request,"publicacion.html",{
        "publicacion":publicacion,
        "categoria":categoria
    })
    
def publicacion_categoria(request,categoria):
    if categoria=="todas":
        publicacion = Publicaciones.objects.all()
        return render(request,"publicacion.html",{
        "publicacion":publicacion})
    else:
        publicacion = Publicaciones.objects.filter(categoria__categoria = categoria)
        return render(request,"publicacion.html",{
        "publicacion":publicacion
    })

def descripcion(request,titulo):
    descripcion = Publicaciones.objects.filter(titulo=titulo)
    print(descripcion)
    return render(request,"descripcion.html",{
        "descripcion" : descripcion
    })