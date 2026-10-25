from django.contrib import admin
from .models import Parquestere, Trilhas, Atrações

# Register your models here.

class ParquestereAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lugar', 'descrição')
    prepopulated_fields = {'slug': ('nome',)}   
    list_filter = ('nome', 'lugar')   
    search_fields = ('nome', 'lugar')  
    
admin.site.register(Parquestere, ParquestereAdmin) #precisamos registrar o modelo Parquestere no admin para que possamos gerenciar os parques através da interface administrativa do Django.
admin.site.register(Atrações)
admin.site.register(Trilhas)

 
