from django.db import models
# Create your models here.

STATUS_CHOICES = [
    ("aberto", "Aberto"),
    ("fechado", "Fechado"),
    ("interditado", "Interditado")
]

class Parquestere(models.Model):
       
    nome = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    descrição = models.TextField()
    abre_as = models.TimeField(null=True, blank=True)
    fecha_as = models.TimeField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='parques/', null=True, blank=True)
    aberto = models.BooleanField(default=True)
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default="aberto",
    )
    história = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.aberto = self.status == "aberto"
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Parque"
        verbose_name_plural = "Parques"
    
    def __str__(self):
        return f"{self.nome}"

class Atrações(models.Model):
    
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default="aberto",
    )
    
    parques = models.ForeignKey(Parquestere, on_delete=models.CASCADE, related_name='atrações')
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    tipo = models.CharField(max_length=50)
    data_horario = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"

    def __str__(self):
        return f"{self.nome}"

class Trilhas(models.Model):
    
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default="aberto",
    )
    

    parque = models.ForeignKey(Parquestere, on_delete=models.CASCADE, related_name='trilhas')
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    dificuldade = models.IntegerField(choices=[(1, 'Fácil'), (2, 'Moderada'), (3, 'Difícil')])
    distância = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"

    def __str__(self):
        return f"{self.nome}" 
    

class FotoParque(models.Model):
    parque = models.ForeignKey(Parquestere, on_delete=models.CASCADE, related_name="fotos",
    )
    imagem = models.ImageField(upload_to="parques/galeria/")
    legenda = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = "Foto do parque"
        verbose_name_plural = "Fotos do parque"

    def __str__(self):
        return f"Foto de {self.parque.nome}"