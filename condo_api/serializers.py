from rest_framework import serializers

from .models import Condominio, Apartamento, Tag, ControleDeAcesso

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = "__all__"

class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = "__all__"
