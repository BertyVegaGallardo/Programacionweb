from django.shortcuts import redirect, render
from .models import Formulario_Persona, Registro
from .forms import PersonaForm, RegistrarseForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def disciplina(request):
    return render(request, 'disciplina.html')

def Noticias(request):
    return render(request, 'Noticias.html')

def QuienesSomos(request):
    return render(request, 'QuienesSomos.html')

def contacto(request):
    return render(request, 'contacto.html')


def dj(request):
    return render(request, 'dj.html')

def xc(request):
    return render(request, 'xc.html')

def ruta(request):
    return render(request, 'ruta.html')

def bmx(request):
    return render(request, 'bmx.html')

def dh(request):
    return render(request, 'dh.html')

def Mariana(request):
    return render(request, 'Mariana.html')

def bosh(request):
    return render(request, 'bosh.html')

def ciclista(request):
    return render(request, 'ciclista.html')

def login (request):
    return render(request, 'login.html')



def Test(request):
    
    Persona= Formulario_Persona.objects.all()

    datos={
        'Formulario_Persona':Persona
    }

    return render(request,'test.html',datos)

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


    return render(request, 'FormularioPersona.html', data)

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

    return render(request,'test2.html',datos)

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


    return render(request, 'Registrarse.html', data)