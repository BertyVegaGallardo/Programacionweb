from rest_framework import serializers
from core.models import Formulario_Persona


class  PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario_Persona
        fields = ['rut', 'nombre', 'Apellido_paterno', 'Apellido_materno', 'edad', 'sexo']