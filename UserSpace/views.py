from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from UserSpace.forms import UserRegisterForm, AvatarForm, UserEditForm
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

def editar_perfil(request):
    usuario = request.user

    if request.method=='POST':
        my_form = UserEditForm(request.POST)
        if my_form.is_valid():

            data = my_form.cleaned_data

            usuario.email=data.get('email')
            usuario.password1 = data.get('password1')
            usuario.password2 = data.get('password2')
            if(usuario.username=='admin' or usuario.username=='gambeta'):
                usuario.is_staff = 1

            usuario.save()
            return render(request,'AppSpace')

    form_User = UserEditForm(initial={
        'email':usuario.email
    })

    contexto = {
        'usuario' : form_User,
    }

    return render(request,'UserSpace/editar_perfil.html',contexto)

def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST,request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            avatar = Avatar.objects.filter(user=data.get('usuario'))

            if len(avatar)>0:
                avatar = avatar[0]
                avatar.imagen = form.cleaned_data['imagen']
                avatar.save()
            else:
                avatar = Avatar(user=data.get('user'),imagen=data.get('imagen'))
                avatar.save()


        return redirect('AppSpaceInicio')

    contexto = {
        'avatar' : AvatarForm()
    }
    return render(request,'UserSpace/avatar.html',contexto)