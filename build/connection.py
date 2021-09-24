import os

import pymongo

#Obfuscated this code because whynot
def connection ():
    OOO000O0O0O0O00OO = os.environ.get("mongoDb")
    O00OOO0O0OOO0O00O =pymongo .MongoClient (OOO000O0O0O0O00OO )
    return O00OOO0O0OOO0O00O 


def createDb(connectionObj,databaseName,collectionName):
    db = connectionObj[databaseName]
    collection = db[collectionName]
    return collection



