from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from UserSpace.forms import UserRegisterForm,AvatarForm
from UserSpace.models import Avatar


# Create your views here.

def registrar(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,'Tu usuario ha sido registrado')
        else:
            messages.info(request,'Tu usuario no pudo ser registrado')
        return redirect('AppSpaceInicio')

    contexto = {
        'form' : UserRegisterForm(),
        'name_submit' : 'Registrarse'
    }

    return render(request,'UserSpace/register.html',contexto)

def solicitud_inicio_sesion(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario,password=contrasenia)

            if user:
                login(request,user)
                messages.info(request,'Bienvenido')
            else:
                messages.info(request,'Verifica tu inicio de sesión')
        else:
            messages.info(request,'Verifica tu inicio de sesión')
        return redirect('AppSpaceInicio')

    contexto = {
        'form' : AuthenticationForm(),
        'name_submit' : 'login'
    }

    return render(request,'UserSpace/login.html',contexto)

def avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            avatar = Avatar.objects.fields(user=data.get('usuario'))

            if len(avatar)>0:
                avatar = avatar[0]
                avatar.imagen = form.cleaned_data['imagen']
                avatar.save()
            else:
                avatar = Avatar(user=data.get('user'),imagen=data.get('imagen'))

        return redirect('AppSpaceInicio')

    contexto = {
        'form' : AvatarForm()
    }
    return render(request,'UserSpace/avatar.html',contexto)