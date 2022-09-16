import django.db
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required, permission_required

from AppSpace.models import SistemaPlanetario,Estrella,Planeta,Habitante,ClasePlaneta, ClaseRegion, ClaseEstrella


from AppSpace.forms import SistemaPlanetarioForm, BuscarSistemaForm, BuscarEstrellaForm, BuscarPlanetaForm, \
    BuscarPlanetaSistemaForm
from AppSpace.forms import HabitanteForm, BuscarHabitanteForm
from AppSpace.forms import EstrellaForm, ClaseEstrellForm
from AppSpace.forms import PlanetaForm, ClasePlanetaForm, ClaseRegionForm

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

# CRUD : CREATE, READ, UPDATE, DELETE

# SISTEMA PLANETARIO : CREATE
# SISTEMA PLANETARIO : READ
# SISTEMA PLANETARIO : EDIT
# SISTEMA PLANETARIO :

# ESTRELLAS : CREATE
# ESTRELLAS : READ
# ESTRELLAS :
# ESTRELLAS :

# PLANETAS : CREATE
# PLANETAS : READ
# PLANETAS :
# PLANETAS :

# HABITANTES : CREATE
# HABITANTES : READ
# HABITANTES :
# HABITANTES :

# CLASE ESTRELLA : CREATE
# CLASE ESTRELLA :
# CLASE ESTRELLA :
# CLASE ESTRELLA :

# CLASE PLANETA : CREATE
# CLASE PLANETA :
# CLASE PLANETA :
# CLASE PLANETA :

# CLASE REGION:
# CLASE REGION:
# CLASE REGION:
# CLASE REGION:


#VISTAR PARA VER LISTADOS COMPLETOS

def ver_sistemas(request):
    sistemas = SistemaPlanetario.objects.all()

    contexto = {
        'sistemas': sistemas,
    }
    return render(request,'AppSpace/sistemas/sistemas.html', contexto)

def ver_estrellas(request):
    estrellas = Estrella.objects.all()

    contexto = {
        'estrellas': estrellas,
    }
    return render(request, 'AppSpace/estrellas/estrellas.html', contexto)


def ver_planetas(request):

    planetas = []

    if request.method == 'POST':
        sistema_planetario = request.POST.get('sistema_planetario')
        planetas = Planeta.objects.filter(sistema_planetario=sistema_planetario)

    contexto = {
        'my_form' : BuscarPlanetaSistemaForm(),
        'planetas': planetas,
    }
    return render(request, 'AppSpace/planetas/planetas.html', contexto)


def ver_habitantes(request,habitando_planeta):
    habitantes = Habitante.objects.filter(habitando_planeta=habitando_planeta)

    contexto = {
        'habitantes': habitantes,
    }
    return render(request, 'AppSpace/habitantes/habitantes.html', contexto)

#VISTAS PARA CREAR

@login_required()
def crear_sistema_planetario(request):
    if request.method == 'POST':
        my_form = SistemaPlanetarioForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = SistemaPlanetario(
                nombre = data.get('nombre'),
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
    return render(request, 'AppSpace/sistemas/crear_sistema.html', contexto)

@login_required()
def crear_estrellas(request):
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

@login_required()
def crear_planetas(request):

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
        'planetas' : planetas,
        'my_form' : PlanetaForm(),
    }
    return render(request,'AppSpace/planetas/planetas.html',contexto)
@login_required
def crear_habitantes(request):

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

# CARACTERISTICAS DE ESTRELLAS, PLANETAS Y REGIONES

@login_required
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

@login_required
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

@login_required
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



#METODOS/VISTAS PARA BUSCAR

@login_required
def buscar_sistemas_planetarios(request):
    sistema_planetario = []
    if request.method =='POST':
        nombre = request.POST.get('nombre')
        sistema_planetario = SistemaPlanetario.objects.filter(nombre__icontains=nombre)

    contexto = {
        'my_form' : BuscarSistemaForm(),
        'sistemas' : sistema_planetario,
    }

    return render(request,'AppSpace/sistemas/buscar_sistemas.html', contexto)

@login_required
def buscar_estrellas(request):
    estrellas = []
    if request.method =='POST':
        nombre = request.POST.get('nombre')
        estrellas = Estrella.objects.filter(nombre__icontains=nombre)
    contexto = {
        'my_form' : BuscarEstrellaForm(),
        'estrellas' : estrellas,
    }
    return render(request,'AppSpace/estrellas/buscar_estrellas.html', contexto)

@login_required
def buscar_planetas(request):
    planetas = []
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        planetas = Planeta.objects.filter(nombre__icontains=nombre)

    contexto = {
        'my_form' : BuscarPlanetaForm(),
        'planetas' : planetas
    }

    return render(request,'AppSpace/planetas/buscar_planetas.html', contexto)

@login_required
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

#MVISTAS PARA EDITAR

def editar_sistema(request, nombre):

    sistema = SistemaPlanetario.objects.get(nombre=nombre)

    if request.method == 'POST':
        my_form = SistemaPlanetarioForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            sistema.nombre = data.get('nombre')
            sistema.cant_estrellas = data.get('cant_estrellas')
            sistema.cant_planetas = data.get('cant_planetas')
            sistema.clase_estrella = data.get('clase_estrella')

            sistema.save()

            return redirect('AppSpaceSistema')

    form_Space = SistemaPlanetarioForm(initial={
        'sistema': sistema.nombre,
        'cant_estrellas': sistema.cant_estrellas,
        'cant_planetas' : sistema.cant_planetas,
        'clase_estrella' : sistema.clase_estrella,
    })

    contexto = {
        'sistema': form_Space,
    }

    return render(request, 'AppSpace/sistemas/editar_sistema.html', contexto)

def editar_estrellas(request, nombre):

    estrella = Estrella.objects.filter(nombre=nombre)

    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            estrella.nombre = data.get('nombre')
            estrella.clase_estrella = data.get('clase_estrella')
            estrella.temperatura_media = data.get('temperatura_media')
            estrella.sistema_planetario = data.get('sistema_planetario')

            estrella.save()

            return redirect('AppSpaceSistema')

    form_Space = EstrellaForm(initial={
        'nombre': estrella.nombre ,
        'clase_estrella': estrella.clase_estrella,
        'temperatura_media' : estrella.temperatura_media,
        'sistema_planetario' : estrella.sistema_planetario,})

    contexto = {
        'sistema_form': form_Space,
    }

    return render(request, 'AppCoder/sistemas/editar_estrella.html', contexto)

def editar_estrellas(request, nombre):

    estrella = Estrella.objects.filter(nombre=nombre)

    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            estrella.nombre = data.get('nombre')
            estrella.clase_estrella = data.get('clase_estrella')
            estrella.temperatura_media = data.get('temperatura_media')
            estrella.sistema_planetario = data.get('sistema_planetario')

            estrella.save()

            return redirect('AppSpaceSistema')

    form_Space = EstrellaForm(initial={
        'nombre': estrella.nombre ,
        'clase_estrella': estrella.clase_estrella,
        'temperatura_media' : estrella.temperatura_media,
        'sistema_planetario' : estrella.sistema_planetario,})

    contexto = {
        'sistema_form': form_Space,
    }

    return render(request, 'AppCoder/sistemas/editar_estrella.html', contexto)

def editar_estrellas(request, nombre):

    estrella = Estrella.objects.filter(nombre=nombre)

    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            estrella.nombre = data.get('nombre')
            estrella.clase_estrella = data.get('clase_estrella')
            estrella.temperatura_media = data.get('temperatura_media')
            estrella.sistema_planetario = data.get('sistema_planetario')

            estrella.save()

            return redirect('AppSpaceSistema')

    form_Space = EstrellaForm(initial={
        'nombre': estrella.nombre ,
        'clase_estrella': estrella.clase_estrella,
        'temperatura_media' : estrella.temperatura_media,
        'sistema_planetario' : estrella.sistema_planetario,})

    contexto = {
        'sistema_form': form_Space,
    }

    return render(request, 'AppCoder/sistemas/editar_estrella.html', contexto)

#VISTAS PARA ELIMINAR

def eliminar_sistema(request, camada):



    return render(request, 'AppCoder/sistemas/editar_estrella.html', contexto)

