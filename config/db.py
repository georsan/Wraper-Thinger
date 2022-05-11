import collections
from pymongo import MongoClient



cli = MongoClient("mongodb+srv://georsan:root@cluster0.rozni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cli.Datos_coneccion

collection_name=db["Datos_coneccion"]

#collection_name=db.get_collection("Datos_coneccion")

