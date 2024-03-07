from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

   
class BuscarProducto(forms.Form):
    descripcion = forms.CharField(max_length=50)
    
    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        