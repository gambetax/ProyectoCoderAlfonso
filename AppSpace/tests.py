from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from faker import Faker
from AppSpace.models import Habitante, Planeta, Estrella, SistemaPlanetario, ClaseEstrella, ClasePlaneta


# Create your tests here.

class Habitantes(TestCase):
    def setUp(self):

        cp= ClasePlaneta.objects.create(clase_planeta='Rocoso',grupo_planeta='Telurico')

        ce = ClaseEstrella.objects.create(clase_estrella='M',temperatura='37000',color='rojo')

        sp= SistemaPlanetario.objects.create(nombre='Solar',cant_estrellas=2,cant_planetas=8,clase_estrella=ce)

        e = Estrella.objects.create(nombre='Sol2',clase_estrella=ce,temperatura_media=38000,sistema_planetario=sp)

        p1 = Planeta.objects.create(nombre='Marte',regiones=2,habitantes=0,satelites_naturales=1
                                    ,satelites_artificiales=0,temperatura_media=-30,
                                    clase_planeta=cp,estrella=e,
                                    sistema_planetario=sp)

        h1 = Habitante.objects.create(nombre='prueba1',apellido='prueba1',edad=22,
                              idioma='prueba idioma 1')

        h2 = Habitante.objects.create(nombre='prueba2', apellido='prueba2', edad=44,
                                 idioma='prueba idioma 2')

    def test_modificar_user(self):

        h1 = Habitante.objects.get(nombre='prueba1')
        h2 = Habitante.objects.get(nombre='prueba2')
        self.assertEqual(h1.nombre, 'prueba1')
        self.assertEqual(h2.idioma, 'prueba idioma 2')


class ViewTests(TestCase):
    def test_sinrespuesta(self):
        response = self.client.get(reverse('AppSpaceInicio'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Space Planets')

    def test_login(self):
        self.user = User.objects.create(username='testuser', password='12345')

        cliente = Client()
        login = cliente.login(username=self.user.username,password=self.user.password)
        response = self.client.get(reverse('AppSpaceInicio'),{'user_id':self.user.id})
        self.assertEqual(response.status_code,200)