from pymongo import MongoClient, DESCENDING
from .database_conection import get_db
from json import dumps, loads
from bson import json_util
from django.http import HttpResponse


def index():
    diputados = []
    for doc in get_db().diputados.find(
        {},
        {
            "_id": 0,
            "Id": 1,
            "Nombre": 1,
            "ApellidoPaterno": 1,
            "ApellidoMaterno": 1,
            "Militancias": 1,
            "Sexo": 1,
            "FechaNacimiento": 1,
            "Actual": True,
        },
    ):
        diputados.append(doc)
    return diputados


def get_by_id(id):
    return list(
        get_db().diputados.find(
            {"Id": str(id)},
            {
                "_id": 0,
                "Id": 1,
                "Nombre": 1,
                "ApellidoPaterno": 1,
                "ApellidoMaterno": 1,
                "Militancias": 1,
                "Sexo": 1,
                "FechaNacimiento": 1,
                "gastos": 1,
            },
        )
    )[0]
