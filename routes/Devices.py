
from lib2to3.pgen2 import token
from fastapi import APIRouter
from Peticiones.Request import rquest,rquestput
from fastapi import Request


Devices_router=APIRouter()


#List Devices
@Devices_router.get("/alldevice")
async def List_Devices(request:Request):
    url="https://makesens.aws.thinger.io/v1/users/MakeSens/devices"
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await  rquest(url,token,parametros)
 

#Read Device Status
@Devices_router.get("/status/{id}")
async def Devices_Status(id:str,request:Request):
    url="https://makesens.aws.thinger.io/v1/users/MakeSens/devices/"+id
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquest(url,token,parametros)
#Statistics
@Devices_router.get("/statistics/{id}")
async def Devices_Status(id:str,request:Request):
    token=request.headers.get("Authorization")
    url='https://makesens.aws.thinger.io/v1/users/MakeSens/devices/'+id+'/stats'
    parametros=request.query_params
    return await rquest(url,token,parametros)

#Callback
@Devices_router.get("/callback/{id}")
async def Callback(id:str,request:Request):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id+'/callback'
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await (url,token,parametros)

#properties
@Devices_router.get("/properties/{id}")
async def Properties(id:str,request:Request,asset_group: str):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id+'/properties'
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquest(url,token,parametros)

#properties(preguntar)
@Devices_router.get("/readproperties/{id}/{properties}")
async def Read_Device_Property(id:str,properties:str,request:Request):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id+'/properties/'+properties
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquest(url,token,parametros)
#Update  Device
@Devices_router.put("/updatedevice/{id}")
async def Update_Device(id:str,request:Request):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquestput(url,token,parametros)

#Update  Device Project
@Devices_router.put("/updatedevice/projects/{id}")
async def Update_Device_Project(id:str,request:Request):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id+'/projects'
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquestput(url,token,parametros)

#Update Device Property
@Devices_router.put("/updatedevice/property/{id}/{property}")
async def Update_Device_Property(id:str,property:str,request:Request):
    url='https://makesens.aws.thinger.io/v3/users/MakeSens/devices/'+id+'/properties'+property
    token=request.headers.get("Authorization")
    parametros=request.query_params
    return await rquestput(url,token,parametros)