from build.connection import *

conn = connection()
col = createDb(conn,'DiscordBot','UserInfo')

def addVal(guildId,UserId,muteStatus=False,banStatus=False):
    col.insert_one({'guildId':guildId,'UserId':UserId,'muteStatus':muteStatus})

def checkExist(fguildId, fUserId):
    count = col.find({"$and":[{'guildId':fguildId},{'UserId':fUserId}]}).count()
    if count >=1:
        print("Already Exist in Db")
    else:
        print("Doesn't Exist")
        addVal(fguildId,fUserId)

def checkMuted(fguildId, fUserId):
    muted = col.find({"$and":[{'guildId':fguildId},{'UserId':fUserId},{'muteStatus':True}]}).count()
    if muted >=1:
        return True
    return False


def mute(fguildId, fUserId):
    col.update_one({"$and":[{'guildId':fguildId},{'UserId':fUserId}]},{'$set':{'muteStatus':True}})