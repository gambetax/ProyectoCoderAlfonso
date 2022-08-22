from django import forms

from AppSpace.models import Planeta

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
    cant_planetas = forms.IntegerField()
    clase_estrella = forms.ChoiceField(choices=ESTRELLA_CHOICES)

class EstrellaForm(forms.Form):
    pass

class PlanetaForm(forms.Form):
    pass

class HabitanteForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    idioma = forms.ChoiceField(choices= IDIOMA_CHOICE)
    planeta_natal = forms.CharField(max_length=40)
    habitando_planeta = forms.CharField(max_length=40)

