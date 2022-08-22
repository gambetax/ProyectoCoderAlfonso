from django.urls import path
from AppSpace.views import inicio, sistema_planetario,estrellas,planetas,habitantes

urlpatterns = [
    path('', inicio, name='AppSpaceInicio'),
    path('sistema',sistema_planetario , name='AppSpaceSistema'),
    path('estrellas',estrellas, name='AppSpaceEstrellas'),
    path('planetas',planetas, name='AppSpacePlanetas'),
    path('habitantes',habitantes, name='AppSpaceHabitantes'),
]