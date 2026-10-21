from django.db import models

# Create your models here.
class Parquestere(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

class Atraccion(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    tipo = models.CharField(max_length=50)
    horário = models.CharField(max_length=50)

class Trilha(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    dificuldade = models.CharField(max_length=50)
    distância = models.FloatField()
    

def __str__(self):
    return self.name
    