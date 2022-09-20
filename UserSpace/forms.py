from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from UserSpace.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username','email','imagen')

class UserEditForm(UserChangeForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_texts = {k:'' for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'