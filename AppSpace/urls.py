from django.urls import path
from AppSpace.views import inicio, sistema_planetario
from AppSpace.views import estrellas
from AppSpace.views import planetas
from AppSpace.views import habitantes,buscar_habitantes
from AppSpace.views import crear_clase_estrella,crear_clase_planeta,crear_clase_region

urlpatterns = [
    path('', inicio, name='AppSpaceInicio'),
    path('sistema', sistema_planetario , name='AppSpaceSistema'),

    path('estrellas', estrellas, name='AppSpaceEstrellas'),

    path('planetas', planetas, name='AppSpacePlanetas'),

    path('habitantes', habitantes, name='AppSpaceHabitantes'),
    path('buscar_habitantes', buscar_habitantes, name='AppSpaceBuscarHabitantes'),
    path('crear_clase_estrella', crear_clase_estrella, name='AppSpaceClaseEstrella'),
    path('crear_clase_planeta', crear_clase_planeta , name='AppSpacePlaneta'),
    path('crear_clase_region', crear_clase_region, name='AppSpaceClaseRegion'),


]