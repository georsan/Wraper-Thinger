from datetime import datetime
from email import header
from time import time
from fastapi import APIRouter, Request
import httpx
from Peticiones.Request import rquest,rquestput
Buckets_router=APIRouter()

#Buckets_router
@Buckets_router.get("/buckets")
async def List_Buckets(request:Request):
    parametros=request.query_params
    url="https://makesens.aws.thinger.io/v1/users/MakeSens/buckets"
    token=request.headers["Authorization"]
    return await  rquest(url,token,parametros)
#Read_Bucket Config
@Buckets_router.get("/bucketsconfig/{id}")
async def Read_Bucket_Config(id:str,request:Request):
    url="https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/"+id
    token=request.headers["Authorization"]
    parametros=request.query_params
    return await  rquest(url,token,parametros)
#Read_Bucket data 
@Buckets_router.get("/bucketsdata/{id}")
async def Read_Bucket_Data(id:str,request:Request):
    url="https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/"+id+"/data"
    token=request.headers["Authorization"]
    parametros=request.query_params
    return await  rquest(url,token,parametros)
#Update_Device
@Buckets_router.put("/updatedevice/{id}")
async def Update_Device(id:str,request:Request):
    url='https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/'+id
    token=request.headers["Authorization"]
    parametros=request.query_params
    return await  rquestput(url,token,parametros)
#Update_Device Project
@Buckets_router.put("/updatedeviceproject/{id}")
async def Update_Device(id:str,request:Request):
    url='https://makesens.aws.thinger.io/v1/users/MakeSens/buckets/'+id+"/projects"
    token=request.headers["Authorization"]
    parametros=request.query_params
    return await  rquestput(url,token,parametros)
