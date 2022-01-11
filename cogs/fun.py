import asyncio
import time

import discord
from discord.ext import commands
import requests,random
from build.generalPurpose import dumbot, getDataFromLink
from build.library import loadingFunnyMessages, moviequotes
from build.urbanDict import searchitem
import re as reg
import wikipedia
from typing import List,Dict
#sends images and quotes
class webmaster(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name='cat',
        brief='Sends an image of a cute (*most of the times*) cat ꓷ:',
        help='Sends a cat image.')
    async def sendCat(self,ctx):
        await ctx.send("Command Disabled Until Further Update")

    @commands.command(
        name='dog',
        brief='Sends an image of a heckin good doggo ꓷ:',
        help='Fucking furry.')
    async def sendDog(self,ctx):
        data = await getDataFromLink(url="https://dog.ceo/api/breeds/image/random", json=True, jsonType='message', returnFile=True, fileName='Dog.png')
        if data == None:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(content= "From PPT with \U0001F49A", file=data)

    @commands.command(
        name='wallpaper',
        brief='Sends a wallpaper.',
        help='Sends a wallpaper with size of 1920x1080')
    async def sendWallpaper(self,ctx):
        data = await getDataFromLink(url="https://picsum.photos/1920/1080", returnFile=True, fileName='Why are you looking at this.png')
        if data == None:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(file=data)

    @commands.command(
        name="quote",
        brief="Sends a quote from a movie/anime.",
        help="Sends a random quote")
    async def sendQuote(self,ctx):
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        url = requests.get('https://animechan.vercel.app/api/random').json()
        await msg.edit(content=f"A quote from {url['character']} : {url['quote']}")

    @commands.command(
        aliases=['re', 'ree', 'reee', 'reeee'],
        brief='It just \'***REEEEEE***\'s lmao',
        help='***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
    async def sendRee(self,ctx):
        num = random.randint(10,100)
        await ctx.send("*R" + "E" * num + "*")

    @commands.command(
        name="say",
        aliases = ["speak"],
        brief="repeats your shit",
        help="repeat")
    async def sendRepeat(self,ctx,*,args):
        if reg.search(pattern='@everyone|@here', string=args, flags=reg.I):
            await ctx.send('Fuck you, you cant loophoel dis')
        else:
            await ctx.message.channel.purge(limit=1)
            await ctx.send(args)

    @commands.command(
        name="yeye",
        aliases= ["yeeyee", "yeyee","yeeye"],
        brief="issi asked me to do it",
        help="yeeeyeeeee")
    async def sendYeye(self,ctx):
        await ctx.send("*Y" + "E" * random.randint(10,50) + "Y" + "E" * random.randint(10,50) + "*")

    @commands.command(
        name="joke",
        aliases=["getjoke","jk"],
        brief="It send a random joke",
        help="a random joke, can be explicit or offensive so beware")
    async def sendJoke(self,ctx, *, args = 'null'):
        # https://sv443.net/jokeapi/v2/
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        if str(args).count('-ex') >= 1:
            url = requests.get('https://v2.jokeapi.dev/joke/Any').json()
        else:
            url = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode').json()
        if url['type'] == 'single':
            await msg.edit(content=url['joke'])
        elif url['type'] == 'twopart':
            await msg.edit(content=f"{url['setup']}\n{url['delivery']}")

    @commands.command(
        name="dadjoke",
        brief='i hate my life',
        help='you hate me')
    async def sendDadjoke(self,ctx):
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        url = requests.get("https://icanhazdadjoke.com/", headers={"accept" : "application/json"}).json()
        await msg.edit(content=url['joke'])

    @commands.command(
        name='yomomma',
        aliases=['yourmom', 'yomom'],
        brief='we like mom jokes',
        help='sends a random yomomma joke')
    async def sendMomjoke(self,ctx):
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        url = requests.get('https://api.yomomma.info/').json()
        await msg.edit(content=url['joke'])


    @commands.command(
        name='wikipedia',
        aliases=['wiki']
    )
    async def wikime(self, ctx, *, arg):
        try:
            data = wikipedia.summary(arg, sentences=7, auto_suggest=False)
            await ctx.send(data)
        except wikipedia.exceptions.DisambiguationError as e:
            pass
            await ctx.send(
                "The Search is highly vauge, it gave multiple outputs which *I* cannot send. Try Something on-point")
        except Exception as e:
            await ctx.send("Idk what the fuck happened, ping PPT/Finix/Draf")
            await dumbot.sendErrorToChannel(self, ctx,"Wikipedia", e)


    @commands.command(
        name="dict",
        aliases=['urban', 'urbandict', 'define']
    )
    async def urban(self, ctx, *, arg):
        search = searchitem(arg)
        await ctx.send(search)

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if reg.search(pattern=r'\bours?\b', string=msg.content, flags=reg.I) and not msg.author.bot:
    #         seq = ["<:doggo:863639575666098186>", "<:pepCom:863639491533340682>", "<:BlackCom:863642798070431744>",
    #                "<:Star:863642810879443004>", "<a:Communist:863640421628641320>", "<:comthumb:863646009334169651>",
    #                "<:usrBall:863646049028276234>", "<:yeye:863647634361942018>", '<:russianpepe:863647634001887273>']
    #         rand = random.choice(seq)
    #         await msg.add_reaction(rand)
    @commands.command(name="temp")
    async def tempratureConversion(self,ctx,*,arg):
        x = arg.split()
        if len(x) > 1:
            arg = arg.replace(" ", "")
        if reg.match("[0-9]+[a-zA-Z]",arg):
            tempMap:Dict[str,List[str]] = {}
            valueNeeded: List[int] = [i for i in arg if i.isdigit()]
            numberRequired: int = int("".join(valueNeeded))
            if arg[-1].upper() == "C":
                tempMap[arg] = [str(int((numberRequired * 9/5) + 32)) + "F" , str(numberRequired + 273)+"K"]
                #Convert to Celcius
            elif arg[-1].upper() == "K":
                tempMap[arg] = [str(int((numberRequired - 273.15)*9/5 + 32)) + "F" , str(numberRequired + 273)+"C"]
            elif arg[-1].upper() == "F":
                tempMap[arg] = [str(int((numberRequired - 32) * 5/9)) + "C", str(int((numberRequired -32)*5/9 + 273.15)) + "K" ]


        #Todo do Graphical Changes
        # embed = discord.Embed()
        # embed.set_author(name=f"{arg[:-1]}°{arg[-1]}" )
        # for i,j in tempMap.items():
        #     for x in j:
        #         embed.add_field(name=f"°{x[-1]}", value=f"{x[:-1]}")
        # await ctx.send(embed=embed)

        await ctx.send(tempMap)

    @commands.command(name='moviequotes', aliases=['mq'])
    async def movieQuote(self,ctx,explicit:bool=False,nsfw:bool=False) -> None:
        if explicit in ["explicit","true","allow"]:
            explicit = True
        if nsfw in["nsfw","true","allow"]:
            nsfw = True
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        quoteObj = moviequotes(explicit,nsfw)

        try:
            await asyncio.wait_for(quoteObj.getMovieQuote(),timeout=10)


            embed = discord.Embed(
                title=quoteObj.movieName,
                description=quoteObj.quote,
                color=discord.Color.random()
            )
            embed.set_footer(text=f"Type: {quoteObj.type}")
            embed.set_thumbnail(url=quoteObj.imageUrl)
            await msg.edit(embed=embed)
        except asyncio.TimeoutError:
            await msg.edit(content=f"Whoops I couldn't find it.")




def setup(bot):
    bot.add_cog(webmaster(bot))
