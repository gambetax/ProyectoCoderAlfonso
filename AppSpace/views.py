from django.db.models import F
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from AppSpace.models import SistemaPlanetario, Estrella, Planeta, Habitante, ClasePlaneta, ClaseRegion, ClaseEstrella


from AppSpace.forms import SistemaPlanetarioForm, BuscarSistemaForm, BuscarEstrellaForm, BuscarPlanetaForm, \
    BuscarPlanetaSistemaForm, BuscarHabitantePlanetaForm, HabitanteEditarForm
from AppSpace.forms import HabitanteForm, BuscarHabitanteForm
from AppSpace.forms import EstrellaForm, ClaseEstrellForm
from AppSpace.forms import PlanetaForm, ClasePlanetaForm, ClaseRegionForm


# Create your views here.
def inicio(request):
    habitantes = Habitante.objects.all()

    contexto = {
        'habitantes': habitantes,
    }

    return render(request, 'index.html',contexto)

# CRUD : CREATE, READ, UPDATE, DELETE

# SISTEMA PLANETARIO : CREATE
# SISTEMA PLANETARIO : READ
# SISTEMA PLANETARIO : EDIT
# SISTEMA PLANETARIO : DELETE
# SISTEMA PLANETARIO : DESHABILITAR
# SISTEMA PLANETARIO : HABILITAR

# ESTRELLAS : CREATE
# ESTRELLAS : READ
# ESTRELLAS : EDIT
# ESTRELLAS : DELETE
# ESTRELLAS :
# ESTRELLAS :

# PLANETAS : CREATE
# PLANETAS : READ
# PLANETAS : EDIT
# PLANETAS : DELETE
# PLANETAS :
# PLANETAS :

# HABITANTES : CREATE
# HABITANTES : READ
# HABITANTES : EDIT
# HABITANTES : DELETE
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


# VISTAR PARA VER LISTADOS COMPLETOS

def ver_sistemas(request):
    sistemas = SistemaPlanetario.objects.all()

    contexto = {
        'sistemas': sistemas,
    }
    return render(request, 'AppSpace/sistemas/sistemas.html', contexto)


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
        'my_form': BuscarPlanetaSistemaForm(),
        'planetas': planetas,
    }
    return render(request, 'AppSpace/planetas/planetas.html', contexto)


def ver_habitantes(request):

    habitantes = []

    if request.method == 'POST':
        habitando_planeta = request.POST.get('habitando_planeta')
        habitantes = Habitante.objects.filter(habitando_planeta=habitando_planeta)

    contexto = {
        'my_form': BuscarHabitantePlanetaForm(),
        'habitantes': habitantes,
    }
    return render(request, 'AppSpace/habitantes/habitantes.html', contexto)

# VISTAS PARA CREAR


@login_required()
def crear_sistema_planetario(request):
    if request.method == 'POST':
        my_form = SistemaPlanetarioForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = SistemaPlanetario(
                nombre=data.get('nombre'),
                cant_estrellas=data.get('cant_estrellas'),
                cant_planetas=data.get('cant_planetas'),
                clase_estrella=data.get('clase_estrella')
            )
            form_data.save()
        else:
            redirect('AppSpace')

    sistema_estrellas = SistemaPlanetarioForm()
    contexto = {
        'sistemas': sistema_estrellas,
        'my_form': SistemaPlanetarioForm(),
    }
    return render(request, 'AppSpace/sistemas/crear_sistema.html', contexto)


@login_required()
def crear_estrellas(request):
    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            form_data = Estrella(
                nombre=data.get('nombre'),
                clase_estrella=data.get('clase_estrella'),
                temperatura_media=data.get('temperatura_media'),
                sistema_planetario=data.get('sistema_planetario')
            )
            form_data.save()
        else:
            redirect('AppSpace')

    estrellas = Estrella.objects.all()
    contexto = {
        'estrellas': estrellas,
        'my_form': EstrellaForm(),
    }
    return render(request, 'AppSpace/estrellas/crear_estrellas.html', contexto)


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
        'planetas': planetas,
        'my_form': PlanetaForm(),
    }
    return render(request, 'AppSpace/planetas/crear_planetas.html', contexto)


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
            if not (form_data.edad<0):
                form_data.save()
                planeta = Planeta.objects.get(id=request.POST.get('habitando_planeta'))
                planeta.habitantes = Habitante.objects.exclude(id=None).count()
                planeta.habitantes = F('habitantes') + 1
                planeta.save()
                messages.info(request, 'Datos actualizados')
            else:
                messages.info(request,'Verifique nuevamente los datos')
        else:
            return  redirect('AppSpaceInicio')

    habitantes = Habitante.objects.all()

    contexto = {
        'habitante': habitantes,
        'my_form': HabitanteForm(),
    }
    return render(request, 'AppSpace/habitantes/crear_habitantes.html', contexto)

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


# VISTAS PARA BUSCAR

@login_required
def buscar_sistemas_planetarios(request):
    sistema_planetario = []
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        sistema_planetario = SistemaPlanetario.objects.filter(nombre__icontains=nombre)

    contexto = {
        'my_form': BuscarSistemaForm(),
        'sistemas': sistema_planetario,
    }

    return render(request, 'AppSpace/sistemas/buscar_sistemas.html', contexto)


@login_required
def buscar_estrellas(request):
    estrellas = []
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        estrellas = Estrella.objects.filter(nombre__icontains=nombre)
    contexto = {
        'my_form': BuscarEstrellaForm(),
        'estrellas': estrellas,
    }
    return render(request, 'AppSpace/estrellas/buscar_estrellas.html', contexto)


@login_required
def buscar_planetas(request):
    planetas = []
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        planetas = Planeta.objects.filter(nombre__icontains=nombre)

    contexto = {
        'my_form': BuscarPlanetaForm(),
        'planetas': planetas
    }

    return render(request, 'AppSpace/planetas/buscar_planetas.html', contexto)


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

    return render(request, 'AppSpace/habitantes/buscar_habitantes.html', contexto)

# VISTAS PARA EDITAR


@login_required()
def editar_sistema(request, id):

    sistema = SistemaPlanetario.objects.get(id=id)

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

    form_space = SistemaPlanetarioForm(initial={

        'sistema': sistema.nombre,
        'cant_estrellas': sistema.cant_estrellas,
        'cant_planetas': sistema.cant_planetas,
        'clase_estrella': sistema.clase_estrella,
    })

    contexto = {
        'sistema': form_space,
    }

    return render(request, 'AppSpace/sistemas/editar_sistema.html', contexto)


@login_required()
def editar_estrella(request, id):

    estrella = Estrella.objects.get(id=id)

    if request.method == 'POST':
        my_form = EstrellaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            estrella.nombre = data.get('nombre')
            estrella.clase_estrella = data.get('clase_estrella')
            estrella.temperatura_media = data.get('temperatura_media')
            estrella.sistema_planetario = data.get('sistema_planetario')

            estrella.save()
            return redirect('AppSpaceEstrellas')

    form_space = EstrellaForm(initial={
        'nombre': estrella.nombre,
        'clase_estrella': estrella.clase_estrella,
        'temperatura_media': estrella.temperatura_media,
        'sistema_planetario': estrella.sistema_planetario,
    })

    contexto = {
        'estrella': form_space,
    }

    return render(request, 'AppSpace/estrellas/editar_estrella.html', contexto)


@login_required()
def editar_planeta(request, id):

    planeta = Planeta.objects.get(id=id)

    if request.method == 'POST':
        my_form = PlanetaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            planeta.nombre = data.get('nombre')
            planeta.clase_planeta = data.get('clase_planeta')
            planeta.regiones = data.get('regiones')
            planeta.habitantes = data.get('habitantes')
            planeta.satelites_naturales = data.get('satelites_naturales')
            planeta.satelites_artificiales = data.get('satelites_artificiales')
            planeta.temperatura_media = data.get('temperatura_media')
            planeta.sistema_planetario = data.get('sistema_planetario')

            planeta.save()
            return redirect('AppSpacePlanetas')

    form_space = PlanetaForm(initial={
        'nombre': planeta.nombre,
        'clase_planeta': planeta.clase_planeta,
        'regiones': planeta.regiones,
        'habitantes': planeta.habitantes,
        'satelites_naturales': planeta.satelites_naturales,
        'satelites_artificiales': planeta.satelites_artificiales,
        'temperatura_media': planeta.temperatura_media,
        'sistema_planetario': planeta.sistema_planetario,
    })

    contexto = {
        'planeta': form_space,
    }

    return render(request, 'AppSpace/planetas/editar_planeta.html', contexto)


@login_required()
def editar_habitante(request, id):

    habitante = Habitante.objects.get(id=id)

    if request.method == 'POST':
        my_form = HabitanteForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            habitante.nombre = data.get('nombre')
            habitante.apellido = data.get('apellido')
            habitante.idioma = data.get('idioma')
            habitante.habitando_planeta = data.get('habitando_planeta')

            habitante.save()
            return redirect('AppSpaceHabitantes')

    form_space = HabitanteForm(initial={
        'nombre': habitante.nombre,
        'apellido': habitante.apellido,
        'edad': habitante.edad,
        'planeta_natal': habitante.planeta_natal,
        'habitando_planeta': habitante.habitando_planeta,
    })

    contexto = {
        'habitante': form_space,
    }

    return render(request, 'AppSpace/habitantes/editar_habitante.html', contexto)

# VISTAS PARA ELIMINAR


@login_required()
def eliminar_sistema(request, id):

    sistema = SistemaPlanetario.objects.get(id=id)
    sistema.delete()

    return redirect('AppSpaceSistema')


@login_required()
def eliminar_estrella(request, id):

    estrella = Estrella.objects.get(id=id)
    estrella.delete()

    return redirect('AppSpaceEstrellas')


@login_required()
def eliminar_planeta(request, id):

    planeta = Planeta.objects.get(id=id)
    planeta.delete()

    return redirect('AppSpacePlanetas')


@login_required()
def eliminar_habitante(request, id):

    habitante = Habitante.objects.get(id=id)
    habitante.delete()

    return redirect('AppSpaceHabitantes')

# VISTAS PARA DESHABILITAR/HABILITAR

#
# @login_required()
# def deshabilitar_sistema(request, estado):
#
#     sistema = SistemaPlanetario.objects.get(estado=estado)
#     sistema.save()
#
#     return redirect('AppSpaceSistema')
#
#
# @login_required()
# def deshabilitar_estrella(request, estado):
#
#     estrella = Estrella.objects.get(estado=estado)
#
#     estrella.save()
#
#     return redirect('AppSpaceEstrellas')
#
#
# @login_required()
# def deshabilitar_planeta(request, estado):
#
#     planeta = Planeta.objects.get(estado=estado)
#     planeta.save()
#     return redirect('AppSpacePlanetas')
#
#
# @login_required()
# def deshabilitar_habitante(request, estado):
#
#     habitante = Habitante.objects.get(estado=estado)
#     habitante.save()
#     return redirect('AppSpaceHabitantes')

# INFO

@login_required()
def info_habitante(request, id):

    habitante = Habitante.objects.get(id=id)
    contexto = {
        'habitante' : habitante,
    }
    return render(request, 'AppSpace/habitantes/info_habitante.html', contexto)