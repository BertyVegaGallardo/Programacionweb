from django import forms
from django.forms import ModelForm
from .models import Formulario_Persona, Registro


class PersonaForm(ModelForm):

    class Meta:
        model = Formulario_Persona
        fields = '__all__'

class RegistrarseForm(ModelForm):

    class Meta:
        model = Registro
        fields = '__all__'