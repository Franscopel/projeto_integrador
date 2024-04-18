from django.urls import path

from . import views

urlpatterns = [
    path("condominios", views.get_condominios, name = "get_all_condominios"),
    path("apartamentos", views.get_apartamentos, name = "get_all_apartamentos")
]