from django.urls import path
from . import views

app_name="condo_app"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('condominio', views.CondominioCreateView.as_view(), name='condominio'),
    path('apartamento', views.ApartamentoCreateView.as_view(), name='apartamento'),
    path('tag', views.TagCreateView.as_view(), name='tag'),
]