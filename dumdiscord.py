import discord
from discord.ext import commands
import aiohttp
import requests
import io
import base64
import random
import re as reg

with open("client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8') 
restrictedChannels = ["database"]

 # ------------------------------------------------------------------------------------------------------------------ 

# This is how Danny(Creator of python API for discord) handles custom prefixes, but that needs cogs which i have no idea
# how they work or what they are even, so imma just keep that here for later use and reference.
    # def getPrefix(bot, msg):
    #     user_id = bot.user.id
    #     base = [f'<@!{user_id}> ', f'<@{user_id}> ']
    #     if msg.guild is None:
    #         base.append('!')
    #         base.append('?')
    #     else:
    #         base.extend(bot.prefixes.get(msg.guild.id, ['?', '!']))
    #     return base

# From here to end of setprefix() is all from 'https://stackoverflow.com/questions/56796991/discord-py-changing-prefix-with-command'
# With slight modifications.
customPrefix = {}
defaultPrefix = ['!']

async def readyUp(bot, msg):
    await bot.change_presence(activity=discord.Game('Blackfinix was here.'))
    return await getPrefix(msg)

bot = commands.Bot(command_prefix='!')  # This is the same as a client initialization, but bot has more functionalities.

async def getPrefix(bot, msg):
    guild = msg.guild
    if guild:     #Only allow custom prefixs in guild
        return customPrefix.get(guild.id, defaultPrefix)
    else:
        return defaultPrefix

@bot.command(
            name = "setprefix",
            brief = "Set your own prefix.",
            help = "Use this to set your own custom Prefix for the Bot to listen to.")
async def setPrefix(self, msg, *,prefixes = ''):
    if bot.get_guild(msg.guild.id):
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
            customPrefix[msg.guild.id] = prefixes.split() or defaultPrefix
            await msg.send(f"Prefixes set as {prefixes}!")
        else: 
            msg.channel.send(content = 'You cant use that here yet.',delete_after = 6)
    else:
        msg.channel.send('This is a Server-Only command.')

@bot.command(
            name = "prefix",
            brief = "Check the default prefix.")
async def sendPrefix(msg):
    if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
        await msg.channel.send(f'Current default prefix is : {defaultPrefix[0]} or {bot.get_prefix(msg)}')
    else : 
        msg.channel.send(content = 'You cant use that here yet.', delete_after = 6)

@bot.command(
            name = "resetprefix",
            brief = "Reset the prefix to the default.",
            help = "Use this to reset the Prefix the bot listens to, to the default.")
async def resetPrefix(msg):
    if bot.get_guild(msg.guild.id):
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
            customPrefix.clear()
            bot.command_prefix = defaultPrefix
            await msg.channel.send(f'Reset the prefix to : {defaultPrefix[0]}')
        else : 
            msg.channel.send('You cant use that here yet.')
    else:
        msg.channel.send('This is a Server-Only command.')

@bot.event
async def on_message(msg):
    # Add stuff here, but DO NOT DELETE THE LINE BELOW!! or nothing will work

    await bot.process_commands(msg)


@bot.command(
            name = "quote",
            brief = "Sends a quote from a movie/anime.",
            help = "I mean, what else do you need to know. It sends a quote from a movie/anime. Thats it bruv." )
async def sendQuote(msg):
    url = requests.get('https://animechan.vercel.app/api/random').json()
    await msg.channel.send(f"A quote from {url['character']} : {url['quote']}")

@bot.command(
            name = 'cat',
            brief = 'Sends an image of a cute (*most of the times*) cat ꓷ:',
            help = 'Fucking furry.')
async def sendCat(msg):
    get_image_url = requests.get(f"https://aws.random.cat/meow").json()
    url = get_image_url['file']
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return await msg.channel.send("Couldn't download the file")
            data = io.BytesIO(await response.read())
            await msg.channel.send("From PPT with \U0001F49A")
            await msg.channel.send(file=discord.File(data,"Cat.png"))

@bot.command(
            name = 'dog',
            brief = 'Sends an image of a heckin good doggo ꓷ:',
            help = 'Fucking furry.')
async def sendDog(msg):
    get_image_url = requests.get(f"https://dog.ceo/api/breeds/image/random").json()
    url = get_image_url['message']
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return await msg.channel.send("Couldn't download the file")
            data = io.BytesIO(await response.read())
            await msg.channel.send(content = "From PPT with \U0001F49A", 
                                        file=discord.File(data,"dog.png"))

@bot.command(
            aliases = ['re','ree','reee','reeee'],
            brief = 'It just \'***REEEEEE***\'s lmao',
            help = '***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
async def sendRee(msg):
    num = random.randint(1,100)
    await msg.channel.send("*R"+"E"*num + "*")


@bot.command(
            name = 'helpme',
            brief = 'This is like help, but better.',
            help = 'What else do you need to know bro, just run the command')
async def sendHelp(msg):
    embed = discord.Embed(title="Bot help perhaps", 
        description="Some useful commands. If a command has <:white_check_mark:857551644546826250> it works, if it has <:x:857551644546826250>, you cant use it in a server")
    embed.add_field(name="!ree", value="Rees out of frustration (<:white_check_mark:857551644546826250>)")
    embed.add_field(name="!s", value="Sends a Random image from internet [1920x1080] (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!cat", value = "Sends a Cat pic \U0001F408 (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!quote", value = "Sends a random anime quote! (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!invite", value = "Sends 'add bot to server' link (<:x:857551644546826250>)")
    embed.add_field(name= "!dog", value="Get a Dog pic \U0001F436 (<:white_check_mark:857551644546826250>)")
    if msg.guild.id == 826148528870129675 and str(msg.channel) not in restrictedChannels:
        embed.add_field(name = "For PPT and Gif", value = "If it has the X emoji, you can use it in the test server, but i dont guarantee it will work.")
    await msg.channel.send(content=None, embed=embed)

@bot.command(
            name = 'clear',
            brief = 'Clears a certain amount of messages in the current chat.',
            help = '*insert Thanos snap here*')
async def clearChat(msg):
    await msg.channel.purge(limit=1)
    await msg.channel.send("Command Depricated UwU (for now)")

@bot.command(
            name = 's',
            brief = 'Sends a wallpaper.',
            help = 'Sends a wallpaper with size of 1920x1080')
async def sendWallpaper(msg):
    url = f"https://picsum.photos/1920/1080"
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await msg.channel.send("Couldn't download the file..")
                data = io.BytesIO(await response.read())
                await msg.channel.send(file=discord.File(data,"Why are you looking at this.png"))

@bot.command(
            name = 'invite',
            brief = 'Please dont use this.',
            help = 'Pwease dont use this uwu')
async def sendInvite(msg):
    if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
        await msg.channel.send("This was a mistake")
        await msg.channel.send("<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
    else : 
        msg.channel.send(content = 'You cant use that here yet.', delete_after = 6)

# @bot.command(
#             name = 'steal',
#             brief = 'Steals an emoji',
#             help = 'Steal an emoji and add it to the server emojis, if there is space.')
# async def stealEmoji():


@bot.command(
            name = 'ping',
            brief = 'Pong',
            help = 'Returns the delay of the bot')
async def ping(msg):
    await msg.send(f'Pong!\n{round(bot.latency * 1000)}ms')

if __name__ == "__main__":
    bot.run(id)
