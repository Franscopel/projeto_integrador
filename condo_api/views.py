import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Apartamento, Condominio

from .serializers import ApartamentoSerializer, CondominioSerializer

@api_view(['GET'])
def get_condominios(request):
    if request.method == 'GET':
        condominios = Condominio.objects.all()

        serializer = CondominioSerializer(condominios, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)