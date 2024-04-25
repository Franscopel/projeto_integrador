from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import ControleDeAcesso

from ..serializers import ControleDeAcessoSerializer

@api_view(['GET', 'POST'])
def gerenciador_controle_de_acessos(request):
    if request.method == 'GET':

        try:
            controle_de_acesso = ControleDeAcesso.objects.all()
            serializer = ControleDeAcessoSerializer(controle_de_acesso, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        novo_controle_de_acesso = request.data
        serializer = ControleDeAcessoSerializer(data=novo_controle_de_acesso)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    