import django.db
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from AppSpace.models import SistemaPlanetario,Estrella,Planeta,Habitante,ClasePlaneta, ClaseRegion, ClaseEstrella


from AppSpace.forms import SistemaPlanetarioForm
from AppSpace.forms import HabitanteForm, BuscarHabitanteForm
from AppSpace.forms import EstrellaForm, ClaseEstrellForm
from AppSpace.forms import PlanetaForm, ClasePlanetaForm, ClaseRegionForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

# CRUD : CREATE, READ, UPDATE, DELETE

# SISTEMA PLANETARIO : CREATE
# SISTEMA PLANETARIO :
# SISTEMA PLANETARIO :
# SISTEMA PLANETARIO :

# ESTRELLAS : CREATE
# ESTRELLAS :
# ESTRELLAS :
# ESTRELLAS :

# PLANETAS : CREATE
# PLANETAS :
# PLANETAS :
# PLANETAS :

# HABITANTES : CREATE
# HABITANTES : READ
# HABITANTES :
# HABITANTES :

# CLASE ESTRELLA :
# CLASE ESTRELLA :
# CLASE ESTRELLA :
# CLASE ESTRELLA :

# CLASE PLANETA :
# CLASE PLANETA :
# CLASE PLANETA :
# CLASE PLANETA :

# CLASE REGION:
# CLASE REGION:
# CLASE REGION:
# CLASE REGION:

def sistema_planetario(request):
    if request.method == 'POST':
        my_form = SistemaPlanetarioForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = SistemaPlanetario(
                nombre = data.get('sistema'),
                cant_estrellas= data.get('cant_estrellas'),
                cant_planetas = data.get('cant_planetas'),
                clase_estrella= data.get('clase_estrella')
            )
            form_data.save()
        else:
            redirect('AppSpace')

    sistema_estrellas= SistemaPlanetarioForm()
    contexto = {
        'sistemas' : sistema_estrellas,
        'my_form' : SistemaPlanetarioForm(),
    }
    return render(request,'AppSpace/sistemas/sistemas.html',contexto)

def estrellas(request):
    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = Estrella(
                nombre = data.get('nombre'),
                clase_estrella = data.get('clase_estrella'),
                temperatura_media= data.get('temperatura_media'),
                sistema_planetario = data.get('sistema_planetario')
            )
            form_data.save()
        else:
            redirect('AppSpace')

    estrellas= Estrella.objects.all()
    contexto = {
        'estrellas' : estrellas,
        'my_form' : EstrellaForm(),
    }
    return render(request,'AppSpace/estrellas/estrellas.html', contexto)

def planetas(request):
    if request.method == 'POST':
        my_form = PlanetaForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            form_data = Planeta(
                nombre=data.get('nombre'),
                clase_planeta=data.get('clase_planeta'),
                regiones=data.get('regiones'),
                habitantes=data.get('habitantes'),
                satelites_naturales=data.get('satelites_naturales'),
                satelites_artificiales=data.get('satelites_artificiales'),
                temperatura_media=data.get('temperatura_media'),
                estrella=data.get('estrella'),
                sistema_planetario=data.get('sistema_planetario'),
            )
            form_data.save()
        else:
            redirect('AppSpaceInicio')

    planetas = Planeta.objects.all()

    contexto = {
        'habitante' : habitantes,
        'my_form' : PlanetaForm(),
    }
    return render(request,'AppSpace/planetas/planetas.html',contexto)

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
    return render(request,'AppSpace/habitantes/habitantes.html',contexto)

def buscar_habitantes(request):

    habitantes = []
    if request.method == "POST":
        apellido = request.POST.get('apellido')
        habitantes = Habitante.objects.filter(apellido__icontains=apellido)

    contexto = {
        'my_form': BuscarHabitanteForm(),
        'habitantes': habitantes
    }

    return render(request,'AppSpace/habitantes/buscar_habitantes.html', contexto)





# CARACTERISTICAS DE ESTRELLAS, PLANETAS Y REGIONES




def crear_clase_estrella(request):
    if request.method == 'POST':
        my_form = ClaseEstrellForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            form_data = ClaseEstrella(
                clase_estrella=data.get('clase_estrella'),
                temperatura=data.get('temperatura'),
                color=data.get('color'),
            )
            form_data.save()
        else:
            redirect('AppSpaceInicio')

    clase_estrellas = ClaseEstrella.objects.all()

    contexto = {
        'clases_estrellas': clase_estrellas,
        'my_form': ClaseEstrellForm(),
    }
    return render(request, 'AppSpace/clase_estrellas.html', contexto)

def crear_clase_planeta(request):
    if request.method == 'POST':
        my_form = ClasePlanetaForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            form_data = ClasePlaneta(
                clase_planeta=data.get('clase_planeta'),
                grupo_planeta=data.get('grupo_planeta'),
                descripcion=data.get('descripcion'),
            )
            form_data.save()
        else:
            redirect('AppSpaceInicio')

    clase_planetas = ClasePlaneta.objects.all()

    contexto = {
        'clases_planetas': clase_planetas,
        'my_form': ClasePlanetaForm(),
    }
    return render(request, 'AppSpace/clase_planetas.html', contexto)
def crear_clase_region(request):
    if request.method == 'POST':
        my_form = ClaseRegionForm(request.POST)

        if my_form.is_valid():

            data = my_form.cleaned_data

            form_data = ClasePlaneta(
                clase_planeta=data.get('clase_planeta'),
                grupo_planeta=data.get('grupo_planeta'),
                descripcion=data.get('descripcion'),
            )
            form_data.save()
        else:
            redirect('AppSpaceInicio')

    clase_regiones = ClaseRegion.objects.all()

    contexto = {
        'clases_regiones': clase_regiones,
        'my_form': ClaseRegionForm(),
    }
    return render(request, 'AppSpace/clase_regiones.html', contexto)

