# La clase HttpResponse es una respuesta HTTP básica que se utiliza para devolver 
# contenido al cliente desde una vista de Django. Permite enviar datos en forma de texto, 
# HTML, JSON u otros formatos compatibles con HTTP.
from django.http import HttpResponse,JsonResponse # el jsonreponse convierte a formato json para poder mostrar una lista
from .models import project, task,alumnos
from django.shortcuts import get_object_or_404 # si no hay un objeto muestra el error 404 
from django.shortcuts import render # render es para renderixar archivos html
from .form import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    title = "welcome to django"
    return render(request,"index.html",{
        "title": title
    })

def hello(request,username):
    print(username)
    # 
    return HttpResponse("<h1>Hello %s</h1>"% username)
# El parámetro request en una función de vista de Django es un objeto que representa la 
# solicitud HTTP realizada por un cliente. Proporciona información sobre la solicitud, 
# como los datos enviados por el cliente, los encabezados de la solicitud, la URL solicitada 
# y otros detalles relevantes.
def about(request):
    username = "ewar"
    return render(request,"about.html",{
        "username": username
    })

def projects(request):
    projects = project.objects.all()
    return render(request,"projects/projects.html",{
        "projects":projects
    })

def tasks(request):
    tasks = task.objects.all()
    return render(request,"tasks/tasks.html",{
        "tasks":tasks
    })


def mostraralumnos(request):
    alumno = alumnos.objects.all()
    return render(request,"alumnos.html",{
        "alumnos": alumno
    })

def createtask(request):
    # este primer if envia a la pagina de create task
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": createnewtask()})
    # esto valida y envia los datos al formulario para crear la tarea
    else:
        form = createnewtask(request.POST)
        if form.is_valid():
            print(form.cleaned_data['title'],form.cleaned_data['description'], form.cleaned_data['project'])
            task.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], project_id=form.cleaned_data['project'].id)
            return redirect("tasks")
    
def create_project(request):
    if request.method == "GET":
        return render(request,"projects/create_projects.html",{
            "form":createproject()
        })
    else:
        project.objects.create(name = request.POST["name"])
        return redirect("projects")
        
def projectdetail(request,id):
    projects = get_object_or_404(project, id = id)
    tareas = task.objects.filter(project_id=id)
    print(projects)
    return render(request,"projects/detail.html",{
        "project":projects,
        "tareas" : tareas
    })