import random

from django.db import models



# Create your models here.

CLASE_ESTRELLA_CHOICES = [
    ('1','O'),
    ('2','B'),
    ('3','A'),
    ('4','F'),
    ('5','G'),
    ('6','K'),
    ('7','M'),
]

CLASE_TEMPERATURA_CHOICES = [
    ('1','≥ 33000 K'),
    ('2', '10000–33000 K'),
    ('3', '7500–10000 K'),
    ('4', '6000–7500 K'),
    ('5', '3700–5200 K'),
    ('6', '≤ 3700 K'),
]

class ClasePlaneta(models.Model):
    clase_planeta = models.CharField(max_length=50)
    grupo_planeta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f' Tipo Planeta : {self.clase_planeta} '


class ClaseRegion(models.Model):
    clase_region = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

class ClaseEstrella(models.Model):
    clase_estrella = models.CharField(choices=CLASE_ESTRELLA_CHOICES,max_length=100)
    descripcion = models.CharField(max_length=250)

    def __unicode__(self):
        return self.clase_estrella
    def __str__(self):
        return f' Clase Estrella : {self.clase_estrella}'


class SistemaPlanetario(models.Model):
    nombre = models.CharField(max_length=40)
    cant_estrellas = models.IntegerField()
    cant_planetas = models.IntegerField()
    clase_estrella = models.ForeignKey(ClaseEstrella,on_delete=models.CASCADE)

    def __str__(self):
        return f' Sistema Planetario : {self.nombre}'

class Estrella(models.Model):
    nombre = models.CharField(max_length=40)
    clase_estrella = models.ForeignKey(ClaseEstrella,blank=True,null=False, on_delete=models.CASCADE)
    temperatura_media =  models.IntegerField()
    sistema_planetario = models.ForeignKey(SistemaPlanetario, on_delete=models.CASCADE)

    def __str__(self):
        return f' Estrella : {self.nombre} | {self.nombre}'
class Planeta(models.Model):
    nombre = models.CharField(max_length=40)
    clase_planeta = models.ForeignKey(ClasePlaneta, blank=False,null=False, on_delete=models.CASCADE, default=0)
    regiones = models.IntegerField()
    habitantes = models.IntegerField()
    satelites_naturales = models.IntegerField()
    satelites_artificiales = models.IntegerField()
    temperatura_media = models.FloatField()
    estrella = models.ForeignKey(Estrella, on_delete=models.CASCADE)
    sistema_planetario = models.ForeignKey(SistemaPlanetario, on_delete=models.CASCADE)

    def __str__(self):
        return f' Planeta : {self.nombre} '

class Habitante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    idioma = models.CharField(max_length=40,null=True)
    planeta_natal = models.ForeignKey(Planeta, on_delete=models.CASCADE)
    habitando_planeta = models.CharField(max_length=40)

    def __str__(self):
        return f' id: {self.id} | {self.nombre} | {self.apellido} | {self.edad} | {self.idioma} | {self.planeta_natal} | {self.habitando_planeta} '