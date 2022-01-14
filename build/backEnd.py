import asyncio
from build.connection import createDb,connection
from typing import Dict,List,Optional,Union

async def addVal(guildId,UserId,muteStatus=False):
    await col.insert_one({'guildId':guildId,'UserId':UserId,'muteStatus':muteStatus})

async def checkExist(guildId, UserId):
    count = await col.count_documents({"$and":[{'guildId':guildId},{'UserId':UserId}]})
    if count == 0:
        print("Adding someone new!")
        await addVal(guildId,UserId)

async def checkMuted(guildId, UserId) -> bool:
    muted = await col.count_documents({"$and":[{'guildId':guildId},{'UserId':UserId},{'muteStatus':True}]})
    if muted >=1:
        return True
    return False


async def mute(guildId, UserId):
    await col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$set':{'muteStatus':True}})

async def unmute(guildId, UserId):
    await col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$set':{'muteStatus':False}})

async def messageIncrement(guildId, UserId):
    await col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$inc':{'messageCount':1}})

async def messageDecrement(guildId, UserId):
    await col.update_one({"$and":[{'guildId':guildId},{'UserId':UserId}]},{'$inc':{'messageCount':-1}})

"""All of the Connection Code for Quotes are below this line"""

async def updateQuoteImage(movie:str, imageUrl:str):
    await quoteCol.update_one({
        "movie":movie
    },
        {
            "$set": {"imageUrl":imageUrl}
        })

# flags: = None
async def addQuote(movie:str,character:str,quote:List[List[Union[str,Optional[Dict[str,bool]]]]],type:str,imageUrl:str=None):
        checkExisting = await quoteCol.count_documents({
            "$and": [
                {'movie': movie},
                {'character': character},

            ]
        }
        )

        if checkExisting == 0:
            await quoteCol.insert_one({
                'movie':movie,
                'character':character,
                'quote':quote,
                'imageUrl':imageUrl,
                'type':type

            })
        else:
            await quoteCol.update_one(
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

async def getRandomQuote(noOfDocuments:int=1):
    async for i in quoteCol.aggregate([{'$sample':{'size':noOfDocuments}}]):
        return i

async def addWaitingMessage(message:str) -> None:
    await LoadingMessage.update_one({'message':message},{'$setOnInsert':{'message':message}},upsert=True)


async def getRandomLoadingMessage(noOfDocuments:int=1) -> str:
    async for i in LoadingMessage.aggregate([{'$sample': {'size':noOfDocuments}}]):
        return i['message']


if __name__ == "build.backEnd":
    loop = asyncio.get_event_loop()
    conn = loop.run_until_complete(connection())

    """ Creating a DB or getting a DB Object doesnt do any IO work, so awaiting it is not required"""
    col = createDb(conn, 'DiscordBot', 'UserInfo')
    quoteCol = createDb(conn, "DiscordBot", "Quotes")
    LoadingMessage = createDb(conn,"DiscordBot","LoadingMessage")


