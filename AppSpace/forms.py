import requests
from django import forms

from .models import models, Habitante
from AppSpace.models import Planeta, ClasePlaneta, SistemaPlanetario, Estrella, ClaseEstrella


ESTRELLA_CHOICES = [
        ('O','≥ 33000 K','azul'),
        ('B', '10000–33000 K','azul a blanco azulado'),
        ('A', '7500–10000 K','blanco'),
        ('F', '6000–7500 K','blanco amarillento'),
        ('G', '5200–6000 K','amarillo'),
        ('K', '3700–5200 K','naranja'),
        ('M', '≤ 3700 K','rojo'),
]

IDIOMA_CHOICE = [
    ('EN', 'Ingles'),
    ('ES', 'Espaniol'),
    ('JP', 'Japones'),
    ('GR', 'Aleman'),
    ('AL', 'Alien'),
]

class SistemaPlanetarioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    cant_estrellas = forms.IntegerField()
    cant_planetas = forms.IntegerField()
    clase_estrella = forms.ModelChoiceField(queryset=ClaseEstrella.objects.all())

class EstrellaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    clase_estrella = forms.ModelChoiceField(queryset=ClaseEstrella.objects.all())
    temperatura_media = forms.CharField()
    sistema_planetario = forms.ModelChoiceField(queryset=SistemaPlanetario.objects.all())

class PlanetaForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    clase_planeta = forms.ModelChoiceField(queryset=ClasePlaneta.objects.all())
    regiones = forms.IntegerField()
    habitantes = forms.IntegerField()
    satelites_naturales = forms.IntegerField()
    satelites_artificiales = forms.IntegerField()
    temperatura_media = forms.FloatField()
    estrella = forms.ModelChoiceField(queryset=Estrella.objects.all())
    sistema_planetario = forms.ModelChoiceField(queryset=SistemaPlanetario.objects.all())

class HabitanteForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    idioma = forms.ChoiceField(choices= IDIOMA_CHOICE)
    planeta_natal = forms.ModelChoiceField(queryset=Planeta.objects.all()) #Se debió utilizar un modelChoiceField para traer con un queryset la consulta al listado de Planetas
    habitando_planeta = forms.ModelChoiceField(queryset=Planeta.objects.all())

class HabitanteEditarForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField(disabled=True)
    idioma = forms.ChoiceField(choices= IDIOMA_CHOICE)
    planeta_natal = forms.ModelChoiceField(queryset=Planeta.objects.all(),disabled=True) #Se debió utilizar un modelChoiceField para traer con un queryset la consulta al listado de Planetas
    habitando_planeta = forms.ModelChoiceField(queryset=Planeta.objects.all())

class ClaseEstrellForm(forms.Form):
    clase_estrella = forms.CharField(max_length=2)
    temperatura = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)

class ClasePlanetaForm(forms.Form):
    clase_planeta = forms.CharField(max_length=50)
    grupo_planeta = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=250, required=False)

class ClaseRegionForm(forms.Form):
    clase_region = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=250, required=False)


#FORMULARIOS PARA BUSQUEDA

class BuscarSistemaForm(forms.Form):
    nombre = forms.CharField(max_length=40,required=False)

class BuscarEstrellaForm(forms.Form):
    nombre = forms.CharField(max_length=40,required=False)

#PLANETAS
class BuscarPlanetaSistemaForm(forms.Form):
    sistema_planetario = forms.ModelChoiceField(queryset=SistemaPlanetario.objects.all())

class BuscarPlanetaForm(forms.Form):
    nombre = forms.CharField(max_length=40,required=False)

#HABITANTES
class BuscarHabitanteForm(forms.Form):
    apellido = forms.CharField(max_length=40,required=False)

class BuscarHabitantePlanetaForm(forms.Form):
    habitando_planeta = forms.ModelChoiceField(queryset=Planeta.objects.all())