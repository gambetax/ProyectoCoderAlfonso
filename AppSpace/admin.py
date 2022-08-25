from django.contrib import admin

from AppSpace.models import SistemaPlanetario,Estrella,Planeta,Habitante,ClaseEstrella,ClasePlaneta
# Register your models here.

admin.site.register(SistemaPlanetario)
admin.site.register(ClasePlaneta)
admin.site.register(ClaseEstrella)
admin.site.register(Estrella)
admin.site.register(Planeta)
admin.site.register(Habitante)

