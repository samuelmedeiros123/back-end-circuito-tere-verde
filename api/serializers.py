from rest_framework import serializers
from parquestere.models import Parquestere, Atrações, Trilhas, FotoParque

class AtraçõesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atrações
        fields = ['id', 'parques', 'nome', 'descrição', 'tipo', 'data_horario','status']
        
        
class TrilhasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilhas
        fields = ['id', 'parque', 'nome', 'descrição', 'dificuldade', 'distância', 'status']

class FotoParqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoParque
        fields = ["id", "imagem", "legenda"]

class ParquestereSerializer(serializers.ModelSerializer):
    atrações = AtraçõesSerializer(many=True, read_only=True)
    trilhas = TrilhasSerializer(many=True, read_only=True)
    fotos = FotoParqueSerializer(many=True, read_only=True)
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
            'status',
            'história',
            'atrações',
            'trilhas',
            'fotos'
            
        ]
        
        

        
