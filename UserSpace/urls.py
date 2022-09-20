from django.urls import path

from AppSpace.views import inicio
from django.contrib.auth.views import LogoutView,TemplateView
from UserSpace.views import solicitud_inicio_sesion, registrar, editar_perfil, agregar_avatar

urlpatterns = [
    path('login/', solicitud_inicio_sesion, name='UserLogin'),
    path('register/', registrar, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='./index.html'), name='UserLogout'),
    path('avatar/', agregar_avatar, name='UserAvatar'),
    path('editar_perfil',editar_perfil, name='UserEditar'),
    path('sobre_mi', TemplateView.as_view(template_name='./about_me.html') ,name='SobreMi')
]

