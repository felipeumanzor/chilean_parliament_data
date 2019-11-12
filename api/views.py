from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .utils import diputados, proyectos, votaciones
from django.views.decorators.cache import cache_page


@api_view(["GET"])
@cache_page(60 * 15)
def get_diputados(request):
    try:
        return Response(diputados.index(), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_proyectos(request):
    try:
        return Response(proyectos.index(), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_proyectos_by_author(request, author_id):
    try:
        return Response(proyectos.get_by_author(author_id), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_votos_by_diputado(request, diputado_id):
    try:
        return Response(
            votaciones.get_by_diputado(diputado_id), status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_gastos_by_diputado(request, author_id):
    try:
        return Response(proyectos.get_by_author(author_id), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_diputado_by_id(request, diputado_id):
    try:
        return Response(diputados.get_by_id(diputado_id), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@cache_page(60 * 15)
def get_proyecto_by_id(request, proyecto_id):
    try:
        return Response(proyectos.get_by_id(proyecto_id), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
