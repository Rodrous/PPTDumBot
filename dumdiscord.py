import discord
from discord.ext import commands
import aiohttp
import requests
import io
import base64
import random
import typing

with open("config/client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8') 
restrictedChannels = ["database"]

with open("config/allowedguildIds.txt") as file:
    f = file.readlines()

allowedguilds = [base64.b64decode(i).decode('utf-8') for i in f]


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
    await bot.change_presence(activity=discord.Game('Your Mum.'))
    return await getPrefix(msg)

bot = commands.Bot(command_prefix='!')  # This is the same as a client initialization, but bot has more functionalities.


#todo change all guild ids 231248 to allowedguilds
async def getPrefix(bot, msg):
    guild = msg.guild
    if guild:     #Only allow custom prefixs in guild
        return customPrefix.get(guild.id, defaultPrefix)
    else:
        return defaultPrefix

@bot.command(
                name = "setprefix",
                help = "Set your own prefix.",
                brief = "Use this to set your own custom Prefix for the Bot to listen to.")
async def setPrefix(self, msg, *,prefixes = ''):
    if bot.get_guild(msg.guild.id):
        if str(msg.guild.id) in allowedguilds and (str(msg.channel) not in restrictedChannels):
            customPrefix[msg.guild.id] = prefixes.split() or defaultPrefix
            await msg.send(f"Prefixes set as {prefixes}!")
        else: 
            await msg.channel.send(content = 'You cant use that here yet.',delete_after = 6)
    else:
        await msg.channel.send('This is a Server-Only command.')

@bot.command(
                name = "prefix",
                help = "Check the default prefix.")
async def sendPrefix(msg):
    print(msg.guild.id,type(msg.guild.id))
    if str(msg.guild.id) in allowedguilds and (str(msg.channel) not in restrictedChannels):
        await msg.channel.send(f'Current default prefix is : {defaultPrefix[0]} or {bot.get_prefix(msg)}')
    else : 
        await msg.channel.send(content = 'You cant use that here yet.', delete_after = 6)

@bot.command(
                name = "resetprefix",
                help = "Reset the prefix to the default.",
                brief = "Use this to reset the Prefix the bot listens to, to the default.")
async def resetPrefix(msg):
    if bot.get_guild(msg.guild.id):
        if str(msg.guild.id) in allowedguilds and (str(msg.channel) not in restrictedChannels):
            customPrefix.clear()
            bot.command_prefix = defaultPrefix
            await msg.channel.send(f'Reset the prefix to : {defaultPrefix[0]}')
        else : 
            await msg.channel.send('You cant use that here yet.')
    else:
        await msg.channel.send('This is a Server-Only command.')

@bot.command(
                name = "quote",
                help = "Sends a quote from a anime.",
                brief = "I mean, what else do you need to know. It sends a quote from an anime. Thats it bruv." )
async def sendQuote(ctx):
    url = requests.get('https://animechan.vercel.app/api/random').json()
    await ctx.send(f"A quote from {url['character']} : {url['quote']}")

@bot.command(
                name = 'cat',
                help = 'Sends an image of a cute (*most of the times*) cat ꓷ:',
                brief = 'Fucking furry.')
async def sendCat(ctx):
    get_image_url = requests.get(f"https://aws.random.cat/meow").json()
    url = get_image_url['file']
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return await ctx.send("Couldn't download the file")
            data = io.BytesIO(await response.read())
            await ctx.send("From PPT with \U0001F49A")
            await ctx.send(file=discord.File(data,"Cat.png"))

@bot.command(
                name = 'dog',
                help = 'Sends an image of a heckin good doggo ꓷ:',
                brief = 'Fucking furry.')
async def sendDog(ctx):
    get_image_url = requests.get(f"https://dog.ceo/api/breeds/image/random").json()
    url = get_image_url['message']
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return await ctx.send("Couldn't download the file")
            data = io.BytesIO(await response.read())
            await ctx.send(content = "From PPT with \U0001F49A",
                                        file=discord.File(data,"dog.png"))

@bot.command(
                name = 'ree',
                help = 'It just \'***REEEEEE***\'s lmao',
                brief = '***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
async def sendRee(ctx):
    num = random.randint(1,100)
    await ctx.send("*R"+"E"*num + "*")


@bot.command(
                name = 'helpme',
                help = 'This is like help, but better.',
                brief = 'What else do you need to know bro, just run the command')
async def sendHelp(msg):
    # For PPT and Gif, if it has the X emoji, you can use it in the test server.
    embed = discord.Embed(title="Bot help perhaps", 
        description="Some useful commands. If a command has <:white_check_mark:857551644546826250> it works, if it has <:x:857551644546826250>, you cant use it in a server")
    embed.add_field(name="!ree", value="Rees out of frustration (<:white_check_mark:857551644546826250>)")
    embed.add_field(name="!s", value="Sends a Random image from internet [1920x1080] (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!cat", value = "Sends a Cat pic \U0001F408 (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!quote", value = "Sends a random anime quote! (<:white_check_mark:857551644546826250>)")
    embed.add_field(name= "!invite", value = "Sends 'add bot to server' link (<:x:857551644546826250>)")
    embed.add_field(name= "!dog", value="Get a Dog pic \U0001F436 (<:white_check_mark:857551644546826250>)")
    await msg.channel.send(content=None, embed=embed)

@bot.command(
                name = 'clear',
                help = 'Clears a certain amount of messages in the current chat.',
                brief = '!clear <somenumber>')

@commands.has_permissions(manage_messages = True)
async def clearChat(ctx,amount: typing.Optional[int]=1):
    await ctx.message.channel.purge(limit=int(amount))


@bot.command(
                name = 's',
                help = 'Sends a wallpaper.',
                brief = 'Sends a wallpaper with size of 1920x1080')
async def sendWallpaper(ctx):
    url = f"https://picsum.photos/1920/1080"
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await ctx.send("Couldn't download the file..")
                data = io.BytesIO(await response.read())
                await ctx.send(file=discord.File(data,"Why are you looking at this.png"))

@bot.command(
                name = 'invite',
                help = 'Please dont use this.',
                brief = 'Pwease dont use this uwu')
async def sendInvite(ctx):
    if str(ctx.message.guild.id) in allowedguilds and (str(ctx.message.channel) not in restrictedChannels):
        await ctx.send("This was a mistake")
        await ctx.send("<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
    else : 
        await ctx.send(content = 'You cant use that here yet.', delete_after = 6)


if __name__ == "__main__":
    bot.run(id)
