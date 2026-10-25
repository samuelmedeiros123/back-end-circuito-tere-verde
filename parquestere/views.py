from django.shortcuts import render
from django.http import HttpResponse

def parquestere_list(request):
    informacoes = {"id": 1, "nome": "Parque Nacional da Serra dos Órgãos", "lugar": "Teresópolis, RJ", "descrição": "O Parque Nacional da Serra dos Órgãos é uma unidade de conservação brasileira localizada na Serra dos Órgãos, no estado do Rio de Janeiro. É conhecido por suas montanhas imponentes, trilhas desafiadoras e rica biodiversidade.", "abre_as": "08:00", "fecha_as": "17:00"}
    return HttpResponse(informacoes)

# Create your views he