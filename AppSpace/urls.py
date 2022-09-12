from django.urls import path
from AppSpace.views import inicio
from AppSpace.views import ver_sistemas,crear_sistema_planetario, buscar_sistemas_planetarios,editar_sistema,eliminar_sistema
from AppSpace.views import ver_estrellas,crear_estrellas, buscar_estrellas
from AppSpace.views import ver_planetas,crear_planetas, buscar_planetas

from AppSpace.views import ver_habitantes,crear_habitantes,buscar_habitantes
from AppSpace.views import crear_clase_estrella,crear_clase_planeta,crear_clase_region

urlpatterns = [
    path('', inicio, name='AppSpaceInicio'),

    path('sistemas', ver_sistemas, name='AppSpaceSistema'),
    path('sistema/crear_sistema_planetario', crear_sistema_planetario , name='AppSpaceCrearSistema'),
    path('sistema/buscar_sistema', buscar_sistemas_planetarios, name='AppSpaceBuscarSistemas'),
    path('sistema/editar_sistema/<str:nombre>', editar_sistema, name='AppSpaceEditarSistema'),
    path('sistema/eliminar_sistema/<str:nombre>', eliminar_sistema, name='AppSpaceEliminarSistema'),

    path('estrellas', ver_estrellas, name='AppSpaceEstrellas'),
    path('estrellas/crear_estrellas', crear_estrellas, name='AppSpaceEstrellas'),
    path('estrellas/buscar_estrellas', buscar_estrellas, name='AppSpaceBuscarEstrellas'),
    #path('estrellas/editar_estrellas/<str:nombre>', editar_estrellas, name=''),
    #path('estrellas/eliminar_estrellas/<str:nombre>', eliminar_estrellas, name=''),

    path('planetas/', ver_planetas, name='AppSpacePlanetas'),
    path('planetas/crear_planetas', crear_planetas, name='AppSpaceCrearPlanetas'),
    path('planetas/buscar_planetas', buscar_planetas, name='AppSpaceBuscarPlanetas'),
    #path('planetas/editar_planetas/<str:nombre>', editar_planetas, name=''),
    #path('planetas/eliminar_planetas/<str:nombre>', eliminar_planetas, name=''),

    path('habitantes', ver_habitantes, name='AppSpaceHabitantes'),
    path('habitantes/crear_habitantes', crear_habitantes, name='AppSpaceCrearHabitantes'),
    path('habitantes/buscar_habitantes', buscar_habitantes, name='AppSpaceBuscarHabitantes'),
    #path('habitantes/editar_habitantes/<str:id>', editar_habitantes, name=''),
    #path('habitantes/eliminar_habitantes/<str:id>', eliminar_habitantes, name=''),

    path('crear_clase_estrella', crear_clase_estrella, name='AppSpaceClaseEstrella'),
    path('crear_clase_planeta', crear_clase_planeta , name='AppSpacePlaneta'),
    path('crear_clase_region', crear_clase_region, name='AppSpaceClaseRegion'),


]