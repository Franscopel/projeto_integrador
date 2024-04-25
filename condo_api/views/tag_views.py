from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Tag

from ..serializers import TagSerializer

@api_view(['GET', 'POST', 'PUT'])
def gerenciador_tags(request):
    if request.method == 'GET':

        try:
            tags = Tag.objects.all()
            serializer = TagSerializer(tags, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
   
    if request.method == 'POST':
        nova_tag = request.data
        serializer = TagSerializer(data=nova_tag)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id_tag = request.data["id"]

        try: 
            update_tag=Tag.objects.get(id=id_tag)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=TagSerializer(update_tag, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)