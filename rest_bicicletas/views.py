from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Formulario_Persona
from .serializers import PersonaSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_personas(request):
    if request.method == 'GET':
        persona = Formulario_Persona.objects.all()
        serializer = PersonaSerializer(persona, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parser(request)
        serializer = PersonaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_bicicletas(request, id):
    try:
        persona = Formulario_Persona.objects.get(rut=id)
    except Formulario_Persona.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonaSerializer(persona, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

