from django.urls import path

from .views.condominio_views import gerenciador_condominios
from .views.apartamento_views import gerenciador_apartamentos
from .views.tag_views import gerenciador_tags
from .views.controle_de_acesso_views import gerenciador_controle_de_acessos

urlpatterns = [
    path("condominios", gerenciador_condominios, name = "gerenciador_condominios"),
    path("apartamentos", gerenciador_apartamentos, name = "gerenciador_apartamentos"),
    path("tags", gerenciador_tags, name = "gerenciador_tags"),
    path("controle-de-acessos", gerenciador_controle_de_acessos, name = "gerenciador_controle-de-acessos"),
]