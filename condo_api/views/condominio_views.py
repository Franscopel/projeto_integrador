from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Condominio

from ..serializers import CondominioSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciador_condominios(request):
    if request.method == 'GET':

        try:
            condominios = Condominio.objects.all()
            serializer = CondominioSerializer(condominios, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'POST':
        novo_condominio = request.data
        serializer = CondominioSerializer(data=novo_condominio)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id_condominio = request.data["id"]

        try: 
            update_condo=Condominio.objects.get(id=id_condominio)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=CondominioSerializer(update_condo, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id_condominio = request.data["id"]

        try: 
            delete_condo=Condominio.objects.get(id=id_condominio)
            Condominio.delete(delete_condo)
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)