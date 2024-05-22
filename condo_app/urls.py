from django.urls import path
from . import views

app_name="condo_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('manut_condominio', views.CondominioListView.as_view(), name='manut_condominio'),
    path('manut_tag', views.TagListView.as_view(), name='manut_tag'),
    path('manut_apartamento', views.ApartamentoListView.as_view(), name='manut_apartamento'),
    path('novo_condominio', views.CondominioCreateView.as_view(), name='novo_condominio'),
    path('detalhe_condominio/<int:pk>/', views.CondominioDetailView.as_view(), name='detalhe_condominio'),
    path('detalhe_tag/<int:pk>/', views.TagDetailView.as_view(), name='detalhe_tag'),
    path('detalhe_apartamento/<int:pk>/', views.ApartamentoDetailView.as_view(), name='detalhe_apartamento'),
    path('atualiza_condominio/<int:pk>/', views.CondominioUpdateView.as_view(), name='atualiza_condominio'),
    path('atualiza_tag/<int:pk>/', views.TagUpdateView.as_view(), name='atualiza_tag'),
    path('atualiza_apartamento/<int:pk>/', views.ApartamentoUpdateView.as_view(), name='atualiza_apartamento'),
    path('excluir_condominio/<int:pk>/', views.CondominioDeleteView.as_view(), name='excluir_condominio'),
    path('excluir_tag/<int:pk>/', views.TagDeleteView.as_view(), name='excluir_tag'),
    path('excluir_apartamento/<int:pk>/', views.ApartamentoDeleteView.as_view(), name='excluir_apartamento'),
    path('novo_apartamento', views.ApartamentoCreateView.as_view(), name='novo_apartamento'),
    path('nova_tag', views.TagCreateView.as_view(), name='nova_tag'),
    path('lista_acessos', views.ControleDeAcessoView.as_view(), name='lista_acessos'),
]