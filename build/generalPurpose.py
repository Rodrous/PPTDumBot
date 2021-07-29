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

# Returns the prefix...
async def getPrefix(msg, bot, string:bool=False):
    tp = await bot.get_prefix(msg)
    if string:
        return ' or '.join(tp[1:]) # ...either in a string as : "@PPTDumbBot or $"...
    return tp # ...or as a List type

#todo Urban Dict Scrapy/Api Add

# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import requests
#
# def get_definition_link(section_url : str):
#     word_url = "http://www.urbandictionary.com/define.php?term="+section_url
#     response = requests.get(word_url)
#     return response.url
#
# def read_definition(word_url : str):
#     try:
#         html = urlopen(word_url)
#         soup = BeautifulSoup(html, features="html.parser")
#         def_definition = soup.find("div","meaning").text
#         def_word = soup.find("a","word").string
#         def_example = soup.find("div","example").text
#     except:
#         def_definition = "NULL"
#         def_word = "NULL"
#         def_example = "NULL"
#     return {"word" : def_word, "def" : def_definition, "example" : def_example}
#
# section_url = input("Word to search for:")
# definition_link = get_definition_link(section_url)
# url = read_definition(definition_link)
# if url['def'] == "NULL":
#     print("This word isn't defined")
# else:
#     print(f"{url['def']}\n{url['example']}\n\n{definition_link}")

# WEBSCRAPING URBANDICT, NEEDS TO FIGURE OUT THE EXAMPLE
