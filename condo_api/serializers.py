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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class ControleDeAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControleDeAcesso
        fields = "__all__"
