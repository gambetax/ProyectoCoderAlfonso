from django.urls import path
from AppSpace.views import inicio, sistema_planetario
from AppSpace.views import estrellas
from AppSpace.views import planetas
from AppSpace.views import habitantes,buscar_habitantes

urlpatterns = [
    path('', inicio, name='AppSpaceInicio'),
    path('sistema', sistema_planetario , name='AppSpaceSistema'),

    path('estrellas', estrellas, name='AppSpaceEstrellas'),

    path('planetas', planetas, name='AppSpacePlanetas'),

    path('habitantes', habitantes, name='AppSpaceHabitantes'),
    path('buscar_habitantes', buscar_habitantes, name='AppSpaceBuscarHabitantes'),

    path('regiones', inicio, name='AppSpaceRegiones'),
    path('claseEstrellas', inicio, name='AppSpaceClaseEstrella'),
    path('clasePlanetas', inicio, name='AppSpaceClasePlaneta'),

]