from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from apps.core import models as modelo
from django.contrib.auth.forms import AuthenticationForm


#FORMULARIOS USUARIOS
class CrearUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = modelo.Admin
        fields = ('usuario','correo','password1')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self, commit=True):
        usuario = super(CrearUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        
        if commit:
            
            usuario.save()
        return usuario

class ModificarUsuario(forms.ModelForm):
    
    class Meta:
        model = modelo.Admin
        fields = ('usuario','correo',)
    
    def clean_password(self):
        return self.initial['password']

class ModificarPassword(forms.ModelForm):
    class Meta:
        model = modelo.Admin
        fields = ('password',)

    def save(self, commit=True):
        usuario = super(ModificarPassword, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        
        if commit:
            
            usuario.save()
        return usuario

class LoginForm(AuthenticationForm):
    #mensajes
    error_messages = {
        'invalid_login': (
            "Porfavor ingrese un %(username)s y contraseña correcta."
            "Los campos pueden ser sensibles a mayusculas y minusculas."
        ),
        'inactive': ("Cuenta inactiva."),
    }
