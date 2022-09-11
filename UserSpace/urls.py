from django.urls import path

from AppSpace.views import inicio
from django.contrib.auth.views import LogoutView
from UserSpace.views import solicitud_inicio_sesion,registrar,avatar

urlpatterns = [
    path('login/', solicitud_inicio_sesion, name='UserLogin'),
    path('register/', registrar, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='./index.html'), name='UserLogout'),
    path('avatar/', avatar, name='UserAvatar'),
]

