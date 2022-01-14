import os
import motor.motor_asyncio,base64

async def connection ():
    OOO000O0O0O0O00OO = os.environ.get("mongoDb")
    O00OOO0O0OOO0O00O = motor.motor_asyncio.AsyncIOMotorClient(OOO000O0O0O0O00OO )
    return O00OOO0O0OOO0O00O

def createDb(connectionObj,databaseName,collectionName):
    db = connectionObj[databaseName]
    collection = db[collectionName]
    return collection