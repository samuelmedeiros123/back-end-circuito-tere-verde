from rest_framework import serializers
from parquestere.models import Parquestere, Atrações, Trilhas

class ParquestereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parquestere
        fields = ['id', 'nome', 'lugar', 'descrição', 'abre_as', 'fecha_as', 'slug', 'image',]
        
        
class AtraçõesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrações
        fields = ['id', 'parques', 'nome', 'descrição', 'tipo', 'data_horario']
        
class TrilhasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilhas
        fields = ['id', 'parque', 'nome', 'descrição', 'dificuldade', 'distância']
        

