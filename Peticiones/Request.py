from datetime import datetime
from time import time
from wsgiref import headers

import httpx


from BD.bd import guardar


async def rquest(url,token,q):

    start=time()
    header={"Authorization":token}
    hora= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = httpx.get(url,params=q,headers=header)
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
    header={"Authorization":token}
    hora= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = httpx.get(url,headers=header,params=parametros)
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
