import asyncio
import re as reg

import discord
import random
import requests
import wikipedia
from discord.ext import commands

from general.generalPurpose import Dumbot, get_data_from_link
from general.library import loadingFunnyMessages, MovieQuotes
from general.urbanDict import searchitem


# sends images and quotes
class Webmaster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='cat',
        brief='Sends an image of a cute (*most of the times*) cat ꓷ:',
        help='Sends a cat image.')
    async def sendCat(self, ctx):
        await ctx.send("Command Disabled Until Further Update")
    
    @commands.command(
        name='dog',
        brief='Sends an image of a heckin good doggo ꓷ:',
        help='Fucking furry.')
    async def sendDog(self, ctx):
        data = await get_data_from_link(link="https://dog.ceo/api/breeds/image/random", json=True, jsonType='message',
                                        returnFile=True, fileName='Dog.png')
        if data == None:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(content="From PPT with \U0001F49A", file=data)
    
    @commands.command(
        name='wallpaper',
        brief='Sends a wallpaper.',
        help='Sends a wallpaper with size of 1920x1080')
    async def sendWallpaper(self, ctx):
        data = await get_data_from_link(link="https://picsum.photos/1920/1080", returnFile=True,
                                        fileName='Why are you looking at this.png')
        if data == None:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(file=data)
    
    @commands.command(
        name="quote",
        brief="Sends a quote from a movie/anime.",
        help="Sends a random quote")
    async def sendQuote(self, ctx):
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        url = requests.get('https://animechan.vercel.app/api/random').json()
        await msg.edit(content=f"A quote from {url['character']} : {url['quote']}")
    
    @commands.command(
        aliases=['re', 'ree', 'reee', 'reeee'],
        brief='It just \'***REEEEEE***\'s lmao',
        help='***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
    async def sendRee(self, ctx):
        num = random.randint(10, 100)
        await ctx.send("*R" + "E" * num + "*")
    
    @commands.command(
        name="say",
        aliases=["speak"],
        brief="repeats your shit",
        help="repeat")
    async def sendRepeat(self, ctx, *, args):
        if reg.search(pattern='@everyone|@here', string=args, flags=reg.I):
            await ctx.send('Fuck you, you cant loophoel dis')
        else:
            await ctx.message.channel.purge(limit=1)
            await ctx.send(args)
    
    @commands.command(
        name="yeye",
        aliases=["yeeyee", "yeyee", "yeeye"],
        brief="issi asked me to do it",
        help="yeeeyeeeee")
    async def sendYeye(self, ctx):
        await ctx.send("*Y" + "E" * random.randint(10, 50) + "Y" + "E" * random.randint(10, 50) + "*")
    
    @commands.command(
        name="joke",
        aliases=["getjoke", "jk"],
        brief="It send a random joke",
        help="a random joke, can be explicit or offensive so beware")
    async def sendJoke(self, ctx, *, args='null'):
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
    async def sendDadjoke(self, ctx):
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        url = requests.get("https://icanhazdadjoke.com/", headers={"accept": "application/json"}).json()
        await msg.edit(content=url['joke'])
    
    @commands.command(
        name='yomomma',
        aliases=['yourmom', 'yomom'],
        brief='we like mom jokes',
        help='sends a random yomomma joke')
    async def sendMomjoke(self, ctx):
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
            await Dumbot.send_error_to_channel(self, ctx, "Wikipedia", e)
    
    @commands.command(
        name="dict",
        aliases=['urban', 'urbandict', 'define']
    )
    async def urban(self, ctx, *, arg):
        search = searchitem(arg)
        await ctx.send(search)
    
    @commands.command(name='MovieQuotes', aliases=['mq'])
    async def movieQuote(self, ctx, *, arg="None") -> None:
        explicit: bool = False
        nsfw: bool = False
        
        try:
            args = arg.lower().split()
            match args[0]:
                case "explicit":
                    explicit = True
                case "nsfw":
                    nsfw = True
            
            if len(args) >= 2:
                match args[1]:
                    case "nsfw":
                        nsfw = True
                    case "explicit":
                        explicit = True
        except Exception:
            pass
        
        loading = await loadingFunnyMessages()
        msg = await ctx.send(loading)
        quoteObj = MovieQuotes(explicit, nsfw)
        
        try:
            await asyncio.wait_for(quoteObj.get_movie_quote(), timeout=10)
            embed = discord.Embed(
                title=quoteObj.movieName,
                description=f"{quoteObj.quote}",
                color=discord.Color.random()
            )
            embed.set_footer(text=f"{quoteObj.character} \nType: {quoteObj.type}")
            embed.set_thumbnail(url=quoteObj.imageUrl)
            await msg.edit(content="", embed=embed)
        except asyncio.TimeoutError:
            await msg.edit(content=f"Whoops I couldn't find it.")


def setup(bot):
    bot.add_cog(Webmaster(bot))
