
from fastapi import FastAPI
from routes.Devices import Devices_router 
from routes.Buckets import Buckets_router
from routes.MongoData import Monogo_router

app = FastAPI()



app.include_router(Devices_router, prefix="/device")
app.include_router(Buckets_router,prefix="/bucket")
app.include_router(Monogo_router,prefix="/mongo")
