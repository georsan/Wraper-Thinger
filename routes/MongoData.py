from typing import Optional

from fastapi import APIRouter

from BD.bd import dato
from config.db import collection_name,db
Monogo_router=APIRouter()

@Monogo_router.get("/data")
def mongodata():
    datos=[]
    for i in collection_name.find():
        datos.append(dato(i))
    return datos

