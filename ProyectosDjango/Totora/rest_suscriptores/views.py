
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Suscriptor
from .serializers import SuscriptorSerializer
from urllib import response
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_suscriptores(request):
    #Lista Sucriptores
    if request.method == 'GET':
        suscriptor = Suscriptor.objects.all()
        serializer = SuscriptorSerializer(suscriptor,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuscriptorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_suscriptor(request,id):
    #GET,UPDATE,DELETE DE UN SUSCRIPTOR
    try:
        suscriptor = Suscriptor.objects.get(rut=id)
    except Suscriptor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SuscriptorSerializer(suscriptor)
        return Response(serializer.data)
    if request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = SuscriptorSerializer(suscriptor,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suscriptor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
