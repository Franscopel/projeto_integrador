from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Apartamento

from ..serializers import ApartamentoSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciador_apartamentos(request):
    if request.method == 'GET':

        try:
            apartamento = Apartamento.objects.all()
            serializer = ApartamentoSerializer(apartamento, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        novo_apartamento = request.data
        serializer = ApartamentoSerializer(data=novo_apartamento)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id_apartamento = request.data["id"]

        try: 
            update_apartamento=Apartamento.objects.get(id=id_apartamento)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=ApartamentoSerializer(update_apartamento, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id_apartamento = request.data["id"]

        try: 
            delete_apartamento=Apartamento.objects.get(id=id_apartamento)
            Apartamento.delete(delete_apartamento)
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)