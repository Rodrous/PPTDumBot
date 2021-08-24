import requests,aiohttp,io
import discord, base64

async def getDataFromLink(url:str, json:bool=False, jsonType:str='', returnFile:bool=False, fileName:str='aRandomName.png'):
    link = url
    if json:
        imageUrl = requests.get(url).json()
        link = imageUrl[jsonType]
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status != 200:
                return None
            data = io.BytesIO(await response.read())
            if returnFile:
                return discord.File(data,fileName)
            return data

class dumbot:

    @staticmethod
    async def getPrefix(msg, bot, string:bool=False):
        # Returns the prefix...
        tp = await bot.get_prefix(msg)
        if string:
            return ' or '.join(tp[1:]) # ...either in a string as : "@PPTDumbBot or $"...
        return tp # ...or as a List type

    @staticmethod
    #todo make this actually find the bot av url and make it async, remember to uncuck it in help menues
    def avatar():
        return 'https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048'