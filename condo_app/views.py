from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from .models import Condominio, Apartamento, ControleDeAcesso, Tag
from .forms import CondominioForm, ApartamentoForm, TagForm

#
# View do Index
#
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#
# Views de Condominio
#
class CondominioCreateView(CreateView):
    model = Condominio
    form_class = CondominioForm
    template_name = 'novo_condominio.html'
    success_message = 'Condomínio cadastrado com sucesso!'

    def get_success_url(self):
        return reverse('condo_app:novo_condominio')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)

class CondominioListView(ListView):
    model = Condominio
    template_name = 'manut_condominio.html'
    context_object_name = 'object_list'

class CondominioDetailView(DetailView):
    model = Condominio
    template_name = 'detalhe_condominio.html'


class CondominioUpdateView(UpdateView):
    model = Condominio
    fields = ['nome', 'cnpj', 'endereco', 'cep', 'num_blocos', 'num_aptos']
    template_name = 'atualiza_condominio.html'

    def get_form(self):
        form = super().get_form()
        # Disable nome and cnpj fields
        form.fields['nome'].widget = forms.HiddenInput()
        form.fields['cnpj'].widget = forms.HiddenInput()
        return form
    def get_success_url(self):
        return reverse('condo_app:manut_condominio')


class CondominioDeleteView(DeleteView):
    model = Condominio
    template_name = 'excluir_condominio.html' 

    def get_success_url(self):
        return reverse('condo_app:manut_condominio')
    
    def delete(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return super().delete(request, *args, **kwargs)

#
# Views de Apartamento
#
class ApartamentoCreateView(CreateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'novo_apartamento.html'
    success_message = 'Apartamento cadastrado com sucesso!'

    def get_success_url(self):
        return reverse('condo_app:novo_apartamento')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)

class ApartamentoListView(ListView):
    model = Apartamento
    template_name = 'manut_apartamento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['condominios'] = Condominio.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        condominio_id = self.request.GET.get('condominio_id')
        if condominio_id:
            # Filtra se um condomínio foi selecionado
            queryset = queryset.filter(condominio_id=condominio_id)
        return queryset.none() if not condominio_id else queryset

class ApartamentoDetailView(DetailView):
    model = Apartamento
    template_name = 'detalhe_apartamento.html'

class ApartamentoUpdateView(UpdateView):
    model = Apartamento
    fields = ['andar', 'tags',]
    template_name = 'atualiza_apartamento.html'

    def get_success_url(self):
        return reverse('condo_app:manut_apartamento')


class ApartamentoDeleteView(DeleteView):
    model = Apartamento
    template_name = 'excluir_apartamento.html' 

    def get_success_url(self):
        return reverse('condo_app:manut_apartamento')
    
    def delete(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return super().delete(request, *args, **kwargs)

#
# Views de Tags
#
class TagListView(ListView):
    model = Tag
    template_name = 'manut_tag.html'
    context_object_name = 'object_list'

class TagDetailView(DetailView):
    model = Tag
    template_name = 'detalhe_tag.html'

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'nova_tag.html'
    success_message = 'Tag cadastrada com sucesso!'

    def get_success_url(self):
        return reverse('condo_app:manut_tag')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)

class TagUpdateView(UpdateView):
    model = Tag
    fields = ['num_sequencial']
    template_name = 'atualiza_tag.html'

    def get_success_url(self):
        return reverse('condo_app:manut_tag')

class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'excluir_tag.html' 

    def get_success_url(self):
        return reverse('condo_app:manut_tag')
    
    def delete(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return super().delete(request, *args, **kwargs)

#
# Views de Controle de Acesso   
#
class ControleDeAcessoView(TemplateView):
    template_name = 'lista_acessos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        queryset = ControleDeAcesso.objects.all()
        if start_date and end_date:
            queryset = queryset.filter(data_hora__range=[start_date, end_date])
        
        context['acessos'] = queryset
        return context