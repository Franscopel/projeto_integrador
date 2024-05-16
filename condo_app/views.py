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
        return reverse('condo_app:condominio')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)
    
class ApartamentoCreateView(CreateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'apartamento.html'
    success_message = 'Apartamento cadastrado com sucesso!'

    def get_success_url(self):
        return reverse('condo_app:apartamento')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)
    
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag.html'
    success_message = 'Tag cadastrada com sucesso!'

    def get_success_url(self):
        return reverse('condo_app:tag')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)