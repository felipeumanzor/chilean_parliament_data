from pymongo import MongoClient, DESCENDING
from .database_conection import get_db
from json import dumps, loads
from bson import json_util
from django.http import HttpResponse


def index():
    proyectos = []
    for doc in get_db().proyectosdeley.aggregate(
        [
            {"$match": {"Votaciones.VotacionProyectoLey.Tipo.@Valor": "1"}},
            {"$unwind": {"path": "$Votaciones.VotacionProyectoLey"}},
            {
                "$match": {
                    "Votaciones.VotacionProyectoLey.TipoVotacionProyectoLey.@Valor": "1"
                }
            },
            {"$sort": {"Votaciones.VotacionProyectoLey.Fecha": -1}},
            {
                "$project": {
                    "_id": 0,
                    "Id": 1,
                    "NumeroBoletin": 1,
                    "Nombre": 1,
                    "FechaIngreso": 1,
                    "Votaciones.VotacionProyectoLey.Id": 1,
                    "Votaciones.VotacionProyectoLey.Resultado": 1,
                    "Votaciones.VotacionProyectoLey.Fecha": 1,
                    "Materias": 1,
                }
            },
        ]
    ):
        proyectos.append(doc)
    return proyectos


def get_by_id(id):
    return list(
        get_db().proyectosdeley.find(
            {"Id": str(id)},
            {
                "_id": 0,
                "Id": 1,
                "Nombre": 1,
                "Autores": 1,
                "Materias": 1,
                "MinisteriosPatrocinantes": 1,
                "Votaciones": 1,
                "TotalNo": 1,
                "TotalSi": 1,
                "TotalDispensado": 1,
            },
        )
    )[0]


def get_by_author(author_id):
    proyectos = []
    for doc in get_db().proyectosdeley.aggregate(
        [
            {
                "$match": {
                    "Votaciones.VotacionProyectoLey.Tipo.@Valor": "1",
                    "Autores.ParlamentarioAutor.Diputado.Id": f"{author_id}",
                }
            },
            {"$unwind": {"path": "$Votaciones.VotacionProyectoLey"}},
            {
                "$match": {
                    "Votaciones.VotacionProyectoLey.TipoVotacionProyectoLey.@Valor": "1"
                }
            },
            {"$sort": {"Votaciones.VotacionProyectoLey.Fecha": -1}},
            {
                "$project": {
                    "_id": 0,
                    "Id": 1,
                    "NumeroBoletin": 1,
                    "Nombre": 1,
                    "FechaIngreso": 1,
                    "Votaciones.VotacionProyectoLey.Id": 1,
                    "Votaciones.VotacionProyectoLey.Resultado": 1,
                    "Votaciones.VotacionProyectoLey.Fecha": 1,
                    "Materias": 1,
                }
            },
        ]
    ):
        proyectos.append(doc)
    return proyectos
