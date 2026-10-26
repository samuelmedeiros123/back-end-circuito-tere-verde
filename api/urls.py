from django.urls import path
from . import views

urlpatterns = [
    path("parquesteresopolis/", views.parquestere_lista),
    path("parquesdetalhes/<slug:slug>/", views.parquestere_detalhes),
]