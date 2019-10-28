from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .utils import diputados, proyectos 

@api_view(['GET'])
def get_diputados(request):
    try:
        return Response( diputados.index() , status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_proyectos(request):
    try:
        return Response( proyectos.index() , status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_proyectos_by_author(request, author_id):
    try:
        return Response( proyectos.get_by_author(author_id) , status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)