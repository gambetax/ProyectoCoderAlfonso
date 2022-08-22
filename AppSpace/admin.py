from django.contrib import admin

from AppSpace.models import SistemaPlanetario,Estrella,Planeta,Habitante,ClaseEstrella,TipoPlaneta
# Register your models here.

admin.site.register(SistemaPlanetario)
admin.site.register(TipoPlaneta)
admin.site.register(ClaseEstrella)
admin.site.register(Estrella)
admin.site.register(Planeta)
admin.site.register(Habitante)

