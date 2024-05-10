from django import forms
from .models import Condominio, Apartamento, Tag

class CondominioForm(forms.ModelForm):
    class Meta:
        model = Condominio
        fields = '__all__' 


class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento
        fields = '__all__'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'