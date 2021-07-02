from discord.ext import commands
import requests, random,discord,aiohttp,io
from build import generalPurpose as gp


#sends images and quotes
class webmaster(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name='cat',
        brief='Sends an image of a cute (*most of the times*) cat ꓷ:',
        help='Fucking furry.')
    async def sendCat(self,ctx):
        data = await gp.getDataFromLink(url="https://aws.random.cat/meow", json=True, jsonType='file', returnFile=True, fileName='Cat.png')
        await ctx.send("From PPT with \U0001F49A")
        await ctx.send(file=data)

    @commands.command(
        name='dog',
        brief='Sends an image of a heckin good doggo ꓷ:',
        help='Fucking furry.')
    async def sendDog(self,ctx):
        data = await gp.getDataFromLink(url="https://dog.ceo/api/breeds/image/random", json=True, jsonType='message', returnFile=True, fileName='Dog.png')
        await ctx.send("From PPT with \U0001F49A")
        await ctx.send(file=data)

    @commands.command(
        name='s',
        brief='Sends a wallpaper.',
        help='Sends a wallpaper with size of 1920x1080')
    async def sendWallpaper(self,ctx):
        data = await gp.getDataFromLink(url="https://picsum.photos/1920/1080", returnFile=True, fileName='Why are you looking at this.png')
        await ctx.send(file=data)

    @commands.command(
        name="quote",
        brief="Sends a quote from a movie/anime.",
        help="I mean, what else do you need to know. It sends a quote from a movie/anime. Thats it bruv.")
    async def sendQuote(self,ctx):
        url = requests.get('https://animechan.vercel.app/api/random').json()
        await ctx.send(f"A quote from {url['character']} : {url['quote']}")

    @commands.command(
        name='Ree',
        aliases=['re', 'reee', 'reeee'],
        brief='It just REEEEEEEEEEE\'s lmao',
        help='***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
    async def sendRee(self,ctx):
        num = random.randint(1, 100)
        await ctx.send("*R" + "E" * num + "*")

def setup(bot):
    bot.add_cog(webmaster(bot))
