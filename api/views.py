from django.shortcuts import render
# from django.http import JsonResponse
from parquestere.models import Parquestere, Atrações, Trilhas
from .serializers import ParquestereSerializer, AtraçõesSerializer, TrilhasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# def parquestere_lista(request):
    #parques = Parquestere.objects.all()
    #parques_list = list(parques.values())
    #return JsonResponse(parques_list, safe=False)
    
@api_view(['GET'])
def parquestere_lista(request):
    if request.method == 'GET':
        parques = Parquestere.objects.all()
        serializer = ParquestereSerializer(parques, many=True) # passamos a queryset para o serializer para converter os objetos em dicionários json, usamos many=True porque estamos serializando uma lista de objetos """
        return Response(serializer.data, status=status.HTTP_200_OK) # retornamos a lista de dicionários json como resposta da requisição