from django import forms
from .models import *

# aca creamos un nuevo formulario
class createnewtask(forms.Form):
    title = forms.CharField(label="titulo de tarea",max_length=200,widget=forms.TextInput(attrs={"class":"miclase"}))
    description = forms.CharField(label="descripcion",widget=forms.Textarea)
    project = forms.ModelChoiceField(queryset=project.objects.all(),label="proyecto")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = project.objects.all()
    
class crearalumno(forms.Form):
    nombre_alumno = forms.CharField(label="Nombre de alumno",max_length=200,required=True)
    edad_alumno = forms.IntegerField(label="Edad",min_value=0,max_value=100,required=True)
    proyecto = forms.ModelChoiceField(queryset=project.objects.all(),label="proyecto")
    
class createproject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto",max_length=200)
    
