import pymongo,base64

#Obfuscated this code because whynot
def connection ():
    OOO000O0O0O0O00OO =base64 .b64decode ('bW9uZ29kYitzcnY6Ly9ib3Q6YmxlaDEyM0BjbHVzdGVyMC5kajZieC5tb25nb2RiLm5ldC9teUZpcnN0RGF0YWJhc2U/cmV0cnlXcml0ZXM9dHJ1ZSZ3PW1ham9yaXR5').decode ('Utf-8')
    O00OOO0O0OOO0O00O =pymongo .MongoClient (OOO000O0O0O0O00OO )
    return O00OOO0O0OOO0O00O 


def createDb(connectionObj,databaseName,collectionName):
    db = connectionObj[databaseName]
    collection = db[collectionName]
    return collection



