from django.urls import path

from . import views

urlpatterns = [
    path("condominios", views.get_condominios, name = "get_all_condominios"),
    path("apartamentos", views.get_apartamentos, name = "get_all_apartamentos"),
    path("tags", views.get_tags, name = "get_all_tags"),
    path("controle-de-acessos", views.get_controle_de_acessos, name = "get_all_controle-de-acesos")
]