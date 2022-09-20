from django.urls import path
from AppSpace.views import inicio
from AppSpace.views import ver_sistemas,crear_sistema_planetario, buscar_sistemas_planetarios,editar_sistema,eliminar_sistema
from AppSpace.views import ver_estrellas,crear_estrellas, buscar_estrellas, editar_estrella, eliminar_estrella
from AppSpace.views import ver_planetas,crear_planetas, buscar_planetas, editar_planeta, eliminar_planeta

from AppSpace.views import ver_habitantes,crear_habitantes,buscar_habitantes, editar_habitante, eliminar_habitante,info_habitante
from AppSpace.views import crear_clase_estrella,crear_clase_planeta,crear_clase_region

urlpatterns = [
    path('', inicio, name='AppSpaceInicio'),

    path('sistemas', ver_sistemas, name='AppSpaceSistema'),
    path('sistema/crear_sistema_planetario', crear_sistema_planetario , name='AppSpaceCrearSistema'),
    path('sistema/buscar_sistemas', buscar_sistemas_planetarios, name='AppSpaceBuscarSistemas'),
    path('sistema/editar_sistema/<int:id>', editar_sistema, name='AppSpaceEditarSistema'),
    path('sistema/eliminar_sistema/<int:id>', eliminar_sistema, name='AppSpaceEliminarSistema'),

    path('estrellas',ver_estrellas, name='AppSpaceEstrellas'),
    path('estrellas/crear_estrellas', crear_estrellas, name='AppSpaceCrearEstrellas'),
    path('estrellas/buscar_estrella', buscar_estrellas, name='AppSpaceBuscarEstrellas'),
    path('estrellas/editar_estrella/<int:id>', editar_estrella, name='AppSpaceEditarEstrella'),
    path('estrellas/eliminar_estrella/<int:id>', eliminar_estrella, name='AppSpaceEliminarEstrella'),

    path('planetas/', ver_planetas, name='AppSpacePlanetas'),
    path('planetas/crear_planetas', crear_planetas, name='AppSpaceCrearPlanetas'),
    path('planetas/buscar_planetas', buscar_planetas, name='AppSpaceBuscarPlanetas'),
    path('planetas/editar_planeta/<int:id>', editar_planeta, name='AppSpaceEditarPlaneta'),
    path('planetas/eliminar_planeta/<int:id>', eliminar_planeta, name='AppSpaceEliminarPlaneta'),

    path('habitantes', ver_habitantes, name='AppSpaceHabitantes'),
    path('habitantes/<int:id>', info_habitante, name='AppSpaceInfoHabitantes'),
    path('habitantes/crear_habitantes', crear_habitantes, name='AppSpaceCrearHabitantes'),
    path('habitantes/buscar_habitantes', buscar_habitantes, name='AppSpaceBuscarHabitantes'),
    path('habitantes/editar_habitante/<int:id>', editar_habitante, name='AppSpaceEditarHabitante'),
    path('habitantes/eliminar_habitante/<int:id>', eliminar_habitante, name='AppSpaceEliminarHabitante'),


    path('crear_clase_estrella', crear_clase_estrella, name='AppSpaceClaseEstrella'),
    path('crear_clase_planeta', crear_clase_planeta , name='AppSpaceClasePlaneta'),
    path('crear_clase_region', crear_clase_region, name='AppSpaceClaseRegion'),


]