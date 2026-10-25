from django.urls import path
from . import views

urlpatterns = [
    path("parquestere/", views.parquestere_list, name="parquestere_list"),
]
