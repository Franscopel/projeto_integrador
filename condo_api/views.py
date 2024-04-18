import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Apartamento, Condominio, Tag, ControleDeAcesso

from .serializers import ApartamentoSerializer, CondominioSerializer, TagSerializer, ControleDeAcessoSerializer

@api_view(['GET'])
def get_condominios(request):
    if request.method == 'GET':
        condominios = Condominio.objects.all()

        serializer = CondominioSerializer(condominios, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_apartamentos(request):
    if request.method == 'GET':
        apartamentos = Apartamento.objects.all()

        serializer = ApartamentoSerializer(apartamentos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tags(request):
    if request.method == 'GET':
        tags = Tag.objects.all()

        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_controle_de_acessos(request):
    if request.method == 'GET':
        controle_de_acessos = ControleDeAcesso.objects.all()

        serializer = ControleDeAcessoSerializer(controle_de_acessos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)