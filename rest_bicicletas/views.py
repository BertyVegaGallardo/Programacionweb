from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Formulario_Persona
from .serializers import PersonaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions  import IsAuthenticated
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def lista_personas(request):
    if request.method == 'GET':
        persona = Formulario_Persona.objects.all()
        serializer = PersonaSerializer(persona, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonaSerializer(data= data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_bicicletas(request, id):
     
    try:
        persona = Formulario_Persona.objects.get(id=id)
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
