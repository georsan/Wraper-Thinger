from typing import Optional


from fastapi import APIRouter,Header
from BD.bd import dato, traerdatos
from config.db import collection_name,db
Monogo_router=APIRouter()

@Monogo_router.get("/data")
def mongodata():
    datos=[]
    for i in collection_name.find():
        datos.append(dato(i))
    return datos

