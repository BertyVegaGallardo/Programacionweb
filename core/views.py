from django.shortcuts import redirect, render
from .models import Formulario_Persona, Registro
from .forms import PersonaForm, RegistrarseForm

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def disciplina(request):
    return render(request, 'core/disciplina.html')

def Noticias(request):
    return render(request, 'core/Noticias.html')

def QuienesSomos(request):
    return render(request, 'core/QuienesSomos.html')

def contacto(request):
    return render(request, 'core/contacto.html')


def Iniciarsesion(request):
    return render(request, 'core/Iniciarsesion.html')

def dj(request):
    return render(request, 'core/dj.html')

def xc(request):
    return render(request, 'core/xc.html')

def ruta(request):
    return render(request, 'core/ruta.html')

def bmx(request):
    return render(request, 'core/bmx.html')

def dh(request):
    return render(request, 'core/dh.html')

def Mariana(request):
    return render(request, 'core/Mariana.html')

def bosh(request):
    return render(request, 'core/bosh.html')

def ciclista(request):
    return render(request, 'core/ciclista.html')

def Test(request):
    
    Persona= Formulario_Persona.objects.all()

    datos={
        'Formulario_Persona':Persona
    }

    return render(request,'core/test.html',datos)

def FormularioPersona(request):
    data = {
        'form': PersonaForm()
    }
    if request.method == 'POST': 
        formulario = PersonaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"]="Éxito"

        else:
            data["form"]=formulario


    return render(request, 'core/FormularioPersona.html', data)

def form_mod_pers(request, id):
    Persona = Formulario_Persona.objects.get(rut=id)
    data = {
        'form': PersonaForm(instance=Persona)
    }
    if request.method == 'POST' :

        formulario = PersonaForm(data=request.POST,instance=Persona)
        if formulario.is_valid:
            formulario.save()
            data ["mensaje"]="Modificación correcta"
    


    return render(request, 'core/form_mod_pers.html', data)


def form_del_pers(request,id):
    Persona= Formulario_Persona.objects.get(rut=id)
    Persona.delete()
    return redirect(to="test")



def Test2(request):
    
    registra= Registro.objects.all()

    datos={
        'Registro':registra
    }

    return render(request,'core/test2.html',datos)

def Registrarse(request):
    data = {
        'form': RegistrarseForm()
    }
    if request.method == 'POST': 
        formulario = RegistrarseForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data["mensaje"]="Éxito  "

        else:
            data["form"]=formulario  


    return render(request, 'core/Registrarse.html', data)