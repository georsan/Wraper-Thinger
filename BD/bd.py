from http import client
from model.modelo import Coneccion
from config.db import collection_name,db

def guardar(con:Coneccion):
    nuevo=dict(con)
    collection_name.insert_one(nuevo)

def dato(item)-> dict:
    return{
        "Token":item["token"],
        "Url":item["url"],
        "Tiempo de respuesta":item["tiemp_respuesta"],
        "Http code":item["httpcode"],
        "Contenido":item["content"],
        "Hora":item["tiempo"]
    }
#prueba
def traerdatos():
    pass