from django.http import HttpResponse

# render para renderizar archivos html y redirect para redireccionar a una ruta - URL
from django.shortcuts import render,redirect

# Crea formularios de registro
from django.contrib.auth.forms import UserCreationForm

# Es la tabla de User que trae Django
from django.contrib.auth.models import User

# Se utiliza para guardar en las cookies
from django.contrib.auth import login

# Es un error de database cuando hay dos datos UNIQUE y se repiten
from django.db import IntegrityError

# Create your views here.


# esto envia a la pagina de inicio
def home(request):
    return render(request, "home.html")

# Aqui se envia a la pagina de signup y tambien se valida si el usuario es correcto
def signup(request):
    
    # Verfica y envia a al formulario
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm,
        })
        
    else:
        
        # verifica que las contraseña 1 y 2 del formulario sean igual
        if request.POST["password1"] == request.POST["password2"]:
            # USER REGISTER
            
            try:
                
                # Aca se crea una variable user donde se guarda los datos puestos en el formulario con el
                # metodo POST, aclarar que User es un model ya creado por Django
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"]
                )
                
                # Guardamos los datos
                user.save()
                
                # Esto guarda los datos en la cookie
                login(request,user)
                
                # Retorna la vista de tareas
                return redirect("tasks")
            
            # Basicamente esto crea un usuario si las dos contraseñas puestas en el form iguales
            
            # si el usuario puesto es igual a un usuario ya creado entonces dara el error IntegrityError: 
            # que es cuando un dato que esta en tipo INIQUE de la db, no se puede repetir
            except IntegrityError:
                
                # Si especificamente encuentra el error se va renderizar el formulario pero con un mensaje
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "username already exists"
                })
        # si el if anterior no se ejecuta quiere decir que las contraseñas no son iguales entonces
        # renderiza el miso formulario pero con un mensaje de error
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "Password do not match"
        })

def tasks(request):
    return render(request,"tasks.html")
