from pymongo import MongoClient, DESCENDING
from .database_conection import get_db
from json import dumps, loads
from bson import json_util
from django.http import HttpResponse


def get_by_diputado(id_diputado):

    votaciones = []

    query = get_db().votaciones.aggregate(
        [
            {"$sort": {"Fecha": -1}},
            {"$unwind": {"path": "$Votos.Voto"}},
            {
                "$match": {
                    "Votos.Voto.Diputado.Id": str(id_diputado),
                    "Quorum.@Valor": "1",
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "Id": 1,
                    "Descripcion": 1,
                    "Fecha": 1,
                    "Resultado": 1,
                    "Votos.Voto.OpcionVoto": 1,
                    "Nombre": 1,
                }
            },
            {"$limit": 50},
        ]
    )

    for doc in query:
        votaciones.append(doc)
    return votaciones

