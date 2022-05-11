import json
from lib2to3.pgen2 import token
from pydantic import BaseModel
from typing import Optional

class Coneccion(BaseModel):
    id:Optional[str]
    token:str
    url:str
    tiemp_respuesta:str
    httpcode:str
    content:str
    tiempo:str
