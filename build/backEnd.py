from build.connection import *
from typing import Dict,List,Optional,Union
conn = connection()
col = createDb(conn,'DiscordBot','UserInfo')
quoteCol = createDb(conn,"DiscordBot","Quotes")

def addVal(guildId,UserId,muteStatus=False,banStatus=False):
    col.insert_one({'guildId':guildId,'UserId':UserId,'muteStatus':muteStatus})

def checkExist(guildId, UserId):
    count = col.count_documents({"$and":[{'guildId':guildId},{'UserId':UserId}]})
    if count == 0:
        print("Adding someone new!")
        addVal(guildId,UserId)

def checkMuted(guildId, UserId) -> bool:
    muted = col.count_documents({"$and":[{'guildId':guildId},{'UserId':UserId},{'muteStatus':True}]})
    if muted >=1:
        return True
    return False


def mute(guildId, UserId):
    col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$set':{'muteStatus':True}})

def unmute(guildId, UserId):
    col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$set':{'muteStatus':False}})

def messageIncrement(guildId, UserId):
    col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$inc':{'messageCount':1}})

def messageDecrement(guildId, UserId):
    col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$inc':{'messageCount':-1}})

"""All of the Connection Code for Quotes are below this line"""

def updateQuoteImage(movie:str, imageUrl:str):
    quoteCol.update_one({
        "movie":movie
    },
        {
            "$set": {"imageUrl":imageUrl}
        })

# flags: = None
def addQuote(movie:str,character:str,quote,type:str,imageUrl:str=None):
        checkExisting = quoteCol.count_documents({
            "$and": [
                {'movie': movie},
                {'character': character},

            ]
        }
        )

        if checkExisting == 0:
            quoteCol.insert_one({
                'movie':movie,
                'character':character,
                'quote':quote,
                'imageUrl':imageUrl,
                'type':type

            })
        else:
            quoteCol.update_one(
                {"$and":[
                    {
                        'movie': movie
                    }, {
                        'character': character
                    }
                ]
                },
                {
                    "$addToSet": {
                        "quote": {
                            "$each": quote
                        }
                    }
                }
            )

def getRandomItem(noOfDocuments:int=1):
    return [i for i in quoteCol.aggregate([{'$sample':{'size':noOfDocuments}}])][0]