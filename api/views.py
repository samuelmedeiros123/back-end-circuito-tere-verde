# from django.http import JsonResponse
from parquestere.models import Parquestere, Atrações, Trilhas
from .serializers import ParquestereSerializer, AtraçõesSerializer, TrilhasSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

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
    
@api_view(['GET'])
def parquestere_detalhes(request, slug):
   parque = get_object_or_404(Parquestere, slug=slug)
   if request.method == 'GET':
       serializer = ParquestereSerializer(parque)
       return Response(serializer.data, status=status.HTTP_200_OK)