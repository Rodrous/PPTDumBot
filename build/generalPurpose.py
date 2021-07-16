import requests,aiohttp,io
import discord

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

# Returns the prefix...
async def getPrefix(msg, bot, string:bool=False):
    tp = await bot.get_prefix(msg)
    if string:
        return ' or '.join(tp[1:]) # ...either in a string as : "@PPTDumbBot or $"...
    return tp # ...or as a List type

#todo Urban Dict Scrapy/Api Add
