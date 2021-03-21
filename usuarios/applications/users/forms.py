from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegisterForm"""
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )   
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )   
    )
    class Meta:
        """Meta definition for UserRegisterForm"""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'La contraseña no coincide')
    
    def clean_password1(self):
        if len(self.cleaned_data['password1']) < 8:
            self.add_error('password1', 'La contraseña es muy corta. Mínimo 8 carateres')
    
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'style': '{margin : 10px}',
            }
        )   
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )   
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username , password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')