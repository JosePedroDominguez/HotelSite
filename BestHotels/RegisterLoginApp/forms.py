from django import forms
from django.db.models import fields

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        fields = ["Email",'Password1','Password2',"Nombre","Apellido","Dni","Calle","CodigoPostal","Pais","Provincia"]