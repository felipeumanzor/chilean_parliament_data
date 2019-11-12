from api.views import (
    get_diputados,
    get_proyectos,
    get_proyectos_by_author,
    get_votos_by_diputado,
    get_gastos_by_diputado,
    get_diputado_by_id,
    get_proyecto_by_id,
)

"""votoparlamentario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("diputados/", get_diputados),
    path("diputados/<diputado_id>/", get_diputado_by_id),
    path("diputados/<diputado_id>/votos/", get_votos_by_diputado),
    path("diputados/<diputado_id>/gastos/", get_gastos_by_diputado),
    path("proyectos/", get_proyectos),
    path("proyectos/by_author/<author_id>/", get_proyectos_by_author),
    path("proyectos/<proyecto_id>/", get_proyecto_by_id),
]
