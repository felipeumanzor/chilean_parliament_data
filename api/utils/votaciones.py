from pymongo import MongoClient, DESCENDING
from .database_conection import get_db
from json import dumps, loads
from bson import json_util
from django.http import HttpResponse


def get_by_diputado():
    proyectos = []
    for doc in get_db().proyectosdeley.find({}, { "_id":0 ,"NumeroBoletin":1 , "Nombre":1 , "TipoIniciativa":1 , "Materias":1 }).sort('Votaciones.VotacionProyectoLey.Fecha', DESCENDING):
        proyectos.append(doc )
    return proyectos


