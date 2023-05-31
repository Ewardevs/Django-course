from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about,name="about"),  
    path('hello/<str:username>', views.hello,name="hello"),
    # se puede crear variables en la rutas con <str:variable>
    
    path("projects/",views.projects,name="projects"),
    path("task/",views.tasks,name="tasks"),
    path("createtask/",views.createtask,name="create_task"),
    path("createprojects/",views.create_project,name="create_project"),
    
    
    path("alumnos/",views.mostraralumnos,name="alumnos"),
    path("projects/<int:id>",views.projectdetail,name="detail"),
]
