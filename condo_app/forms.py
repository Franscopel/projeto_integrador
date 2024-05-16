from django import forms
from .models import Condominio, Apartamento, Tag

class CondominioForm(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = ("nome", "cnpj", "endereco", "cep", "num_blocos", "num_aptos") 
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}), 
            "cnpj": forms.TextInput(attrs={'class': 'form-control'}), 
            "endereco": forms.TextInput(attrs={'class': 'form-control'}), 
            "cep": forms.TextInput(attrs={'class': 'form-control'}), 
            "num_blocos": forms.NumberInput(attrs={'class': 'form-control'}), 
            "num_aptos": forms.NumberInput(attrs={'class': 'form-control'}), 
            "num_aptos": forms.NumberInput(attrs={'class': 'form-control'})  
        }


class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = ("condominio", "bloco", "num_do_apto", "andar", "tags")
        widgets = {
            "condominio": forms.Select(attrs={'class': 'form-control'}),
            "bloco": forms.NumberInput(attrs={'class': 'form-control'}),
            "num_do_apto": forms.NumberInput(attrs={'class': 'form-control'}),
            "andar": forms.NumberInput(attrs={'class': 'form-control'}),
            "tags": forms.TextInput(attrs={'class': 'form-control'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("num_tag", "num_sequencial")
        widgets = {
            "num_tag": forms.NumberInput(attrs={'class': 'form-control'}),
            "num_sequencial": forms.NumberInput(attrs={'class': 'form-control'}),
        }