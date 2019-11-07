from pymongo import MongoClient, DESCENDING
from .database_conection import get_db
from json import dumps, loads
from bson import json_util
from django.http import HttpResponse


def index():
    proyectos = []
    for doc in get_db().proyectosdeley.aggregate([
        {
            '$match': {
                'Votaciones.VotacionProyectoLey.Tipo.@Valor': '1'
            }
        }, {
            '$unwind': {
                'path': '$Votaciones.VotacionProyectoLey'
            }
        }, {
            '$match': {
                'Votaciones.VotacionProyectoLey.TipoVotacionProyectoLey.@Valor': '1'
            }
        }, {
            '$sort': {
                'Votaciones.VotacionProyectoLey.Fecha': -1
            }
        }, {
            '$project': {
                '_id': 0, 
                'Id': 1, 
                'NumeroBoletin': 1, 
                'Nombre': 1, 
                'FechaIngreso': 1, 
                'Votaciones.VotacionProyectoLey.Id': 1, 
                'Votaciones.VotacionProyectoLey.Resultado': 1, 
                'Materias': 1
            }
        }
    ]):
        proyectos.append(doc )
    return proyectos

def get_by_id(id):
    return get_db().diputados.find({}, { "_id":0 ,"Id":1 , "Nombre":1 , "ApellidoPaterno":1 , "ApellidoMaterno":1, "Militancias":1, "Sexo":1 , "FechaNacimiento":1 })

def get_by_author(author_id):
    proyectos = []
    for doc in get_db().proyectosdeley.find({"Autores.ParlamentarioAutor.Diputado.Id":f'{author_id}'}, { "_id":0 ,"NumeroBoletin":1 , "Nombre":1 , "TipoIniciativa":1 , "Materias":1 }).sort('Votaciones.VotacionProyectoLey.Fecha', DESCENDING):
        proyectos.append(doc )
    return proyectos
