from django.contrib import admin
from .models import Parquestere, Atraccion, Trilha

# Register your models here.

class ParquestereAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description')

admin.site.register(Parquestere)
admin.site.register(Atraccion)
admin.site.register(Trilha)

 
