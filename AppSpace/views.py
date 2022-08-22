import django.db
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from AppSpace.models import SistemaPlanetario,Estrella,Planeta,Habitante
from AppSpace.forms import SistemaPlanetarioForm,HabitanteForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def sistema_planetario(request):
    if request.method == 'POST':
        my_form = SistemaPlanetarioForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = SistemaPlanetarioForm(nombre = data.get('nombre'),
                                        cant_planetas = data.get('cant_planetas'),
                                        clase_estrella= data.get('clase_estrella'))
            form_data.save()
        else:
            redirect('AppSpace')

    sistema_estrellas= SistemaPlanetarioForm()
    contexto = {
        'sistemas' : sistema_estrellas,
        'my_form' : my_form,
    }
    return render(request,'AppSpace/AppSpaceSistema')

def estrellas(request):
    if request.method == 'POST':
        my_form = Estrella(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = Estrella(
                nombre = data.get('nombre'),
                clase_estrella = data.get('clase_estrella'),
                temperatura_media= data.get('temperatura_media'),
                sistema_estrella = data.get('sistema_estrella')
            )
            form_data.save()
        else:
            redirect('AppSpace')

    estrella= Estrella.objects.all()
    contexto = {
        'estrella' : estrella,
        'my_form' : my_form,
    }
    return render(request,'AppSpace/AppSpaceEstrella')


def planetas(request):
    pass

def habitantes(request):


    if request.method == 'POST':
        my_form = HabitanteForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            form_data = Habitante(
                nombre=data.get('nombre'),
                apellido=data.get('apellido'),
                edad=data.get('edad'),
                idioma=data.get('idioma'),
                planeta_natal=data.get('planeta_natal'),
                habitando_planeta=data.get('habitando_planeta'),
            )
            form_data.save()
        else:
            redirect('AppSpaceInicio')

    habitantes = Habitante.objects.all()

    contexto = {
        'habitante' : habitantes,
        'my_form' : HabitanteForm(),
    }
    return render(request,'AppSpace/habitantes.html',contexto)