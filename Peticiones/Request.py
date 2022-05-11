from datetime import datetime
from time import time

from fastapi import Response
from BD.bd import guardar
import httpx

async def rquest(url,token,q):

    start=time()
    header={'Authorization':token}
    hora= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = httpx.get(url,params=q,auth=token)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        enviar={ 
            "token":token,
            "url":response.url._uri_reference,
            "httpcode":response.status_code,
            "tiemp_respuesta":time()-start,
            "content":exc.response.text,
            "tiempo":hora
            }
        guardar(enviar)
        return exc.response.text
               
    respuestaTime=time()-start
    enviar={ 
        "token":token,
        "url":response.url._uri_reference,
        "tiemp_respuesta":respuestaTime,
        "httpcode":response.status_code,
        "content":response.json(),
        "tiempo":hora
    }
    guardar(enviar)
    return response.json()

#put
async def rquestput(url,token,parametros):
    start=time()
    #token=client._headers["authorization"]
    hora= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = httpx.get(url,auth=token,params=parametros)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        enviar={ 
            "token":token,
            "url":response.url._uri_reference,
            "httpcode":response.status_code,
            "content":response.text,
            "tiempo":hora
            }
        guardar(enviar)
        return exc.response.text    
    respuestaTime=time()-start
    enviar={ 
        "token":token,
        "url":response.url._uri_reference,
        "tiemp_respuesta":respuestaTime,
        "httpcode":response.status_code,
        "content":response.text,
        "tiempo":hora
    }
    guardar(enviar)
    return response.json()
