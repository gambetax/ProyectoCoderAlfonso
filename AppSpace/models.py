import dataclasses
import datetime
import random

from django.db import models
from self import self


# Create your models here.

class ClaseEstrella(models.Model):
    clase_estrella = models.CharField(max_length=2)
    temperatura = models.CharField(max_length=50,default='0')
    color = models.CharField(max_length=50, default='color')

    def __unicode__(self):
        return self.clase_estrella
    def __str__(self):
        return f' Estrella : {self.clase_estrella}'
    class Meta:
        db_table = 'appspace_claseestrella'

class ClasePlaneta(models.Model):
    clase_planeta = models.CharField(max_length=50)
    grupo_planeta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250,null=True)

    def __str__(self):
        return f' Planeta : {self.clase_planeta} '
    class Meta:
        db_table = 'appspace_claseplaneta'

class ClaseRegion(models.Model):
    clase_region = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250,null=True)
    class Meta:
        db_table = 'appspace_claseregion'



class SistemaPlanetario(models.Model):
    nombre = models.CharField(max_length=40)
    cant_estrellas = models.IntegerField()
    cant_planetas = models.IntegerField()
    clase_estrella = models.ForeignKey(ClaseEstrella,on_delete=models.CASCADE)
    # fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' Sistema : {self.nombre}'
    class Meta:
        db_table = 'appspace_sistemaplanetario'

class Estrella(models.Model):
    nombre = models.CharField(max_length=40)
    clase_estrella = models.ForeignKey(ClaseEstrella,blank=True,null=False, on_delete=models.CASCADE)
    temperatura_media =  models.IntegerField()
    sistema_planetario = models.ForeignKey(SistemaPlanetario, on_delete=models.CASCADE)
    # fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f' {self.nombre}'
    class Meta:
        db_table = 'appspace_estrella'


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
    # fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.nombre} '
    class Meta:
        db_table = 'appspace_planeta'


class Habitante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    idioma = models.CharField(max_length=40,null=True)
    planeta_natal = models.ForeignKey(Planeta, on_delete=models.CASCADE, related_name='%(class)s_planeta_natal',blank=True)
    habitando_planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE, related_name='%(class)s_habitando_planeta',blank=True)
    # fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' id: {self.id} | {self.nombre} | {self.apellido} | {self.edad} | {self.idioma} | {self.planeta_natal} | {self.habitando_planeta} '
    class Meta:
        db_table = 'appspace_habitante'