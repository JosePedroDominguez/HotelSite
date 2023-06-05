from django.shortcuts import render,redirect
from RegisterLoginApp.forms import CustomUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def Register_Page(request):
    data={
        'from':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(Email = formulario.cleaned_data["Email"], Password = formulario.cleaned_data["Password1"])
            login(request, user)
            messages.success(request,"Cuenta Creada Exitosamente")
            return redirect(to="Home")
        data["from"] = formulario
    return(render(request,'Register/Register.html', data))