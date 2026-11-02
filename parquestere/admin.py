from django.contrib import admin
from .models import Parquestere, Trilhas, Atrações, FotoParque

# Register your models here.
class FotoParqueInline(admin.TabularInline):
    model = FotoParque
    extra = 1
class ParquestereAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lugar', 'descrição', 'image')  
    prepopulated_fields = {'slug': ('nome',)}   
    list_filter = ('nome', 'lugar', 'status')   
    search_fields = ('nome', 'lugar')  
    inlines = [FotoParqueInline]
    
admin.site.register(Parquestere, ParquestereAdmin) #precisamos registrar o modelo Parquestere no admin para que possamos gerenciar os parques através da interface administrativa do Django.
admin.site.register(Atrações)
admin.site.register(Trilhas)
admin.site.register(FotoParque)

 
