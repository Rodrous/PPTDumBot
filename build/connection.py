import pymongo

def connection():
    conn_str = "mongodb+srv://bot:bleh123@cluster0.dj6bx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_str)
    return client


def createDb(connectionObj,databaseName,collectionName):
    db = connectionObj[databaseName]
    collection = db[collectionName]
    return collection



