from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def agregar_contacto(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last = request.POST.get('last')
        email = request.POST.get('email')
        # Hacer algo con los datos recibidos, como guardarlos en la base de datos o enviar un correo electrónico
        persons.objects.create(first_name=name, last_name=last, handle=email)

        return redirect(" agregar_contacto")

    person = persons.objects.all()

    return render(request, 'index.html', {
        "persons": person
    })
    
def eliminar_contacto(request,id):
    contacto = persons.objects.filter(id=id)
    contacto.delete()
    return redirect("agregar_contacto")
