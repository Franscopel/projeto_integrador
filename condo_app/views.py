from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import Condominio, Apartamento, Tag
from .forms import CondominioForm, ApartamentoForm, TagForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CondominioCreateView(CreateView):
    model = Condominio
    form_class = CondominioForm
    template_name = 'condominio.html'
    success_message = 'Condomínio cadastrado com sucesso!'

    def get_success_url(self):
        return reverse('condominio')
    
class ApartamentoCreateView(CreateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'apartamento.html'
    success_message = 'Apartamento cadastrado com sucesso!'

    def get_success_url(self):
        return reverse('apartamento')
    
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag.html'
    success_message = 'Tag cadastrada com sucesso!'

    def get_success_url(self):
        return reverse('tag')