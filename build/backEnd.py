from build.connection import *

conn = connection()
col = createDb(conn,'DiscordBot','UserInfo')

def addVal(guildId,UserId,muteStatus=False,banStatus=False):
    col.insert_one({'guildId':guildId,'UserId':UserId,'muteStatus':muteStatus})

def checkExist(guildId, UserId):
    count = col.find({"$and":[{'guildId':guildId},{'UserId':UserId}]}).count()
    if count == 0:
        print("Adding someone new!")
        addVal(guildId,UserId)

def checkMuted(guildId, UserId):
    muted = col.find({"$and":[{'guildId':guildId},{'UserId':UserId},{'muteStatus':True}]}).count()
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