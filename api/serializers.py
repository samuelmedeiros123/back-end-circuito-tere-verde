from rest_framework import serializers
from parquestere.models import Parquestere, Atrações, Trilhas

class AtraçõesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrações
        fields = ['id', 'parques', 'nome', 'descrição', 'tipo', 'data_horario']
        
        
class TrilhasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilhas
        fields = ['id', 'parque', 'nome', 'descrição', 'dificuldade', 'distância']


class ParquestereSerializer(serializers.ModelSerializer):
    atrações = AtraçõesSerializer(many=True, read_only=True)
    trilhas = TrilhasSerializer(many=True, read_only=True)
    class Meta:
        model = Parquestere
        fields = [
            'id',
            'nome',
            'lugar',
            'descrição',
            'abre_as',
            'fecha_as',
            'slug',
            'image',
            'aberto',
            'história',
            'atrações',
            'trilhas',
        ]
        
        

        
