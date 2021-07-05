from discord.ext import commands
import requests,aiohttp,io,discord,random,sys

#sends images and quotes
class webmaster(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name='cat',
        brief='Sends an image of a cute (*most of the times*) cat ꓷ:',
        help='Sends a cat image.')
    async def sendCat(self,ctx):
        data = await gp.getDataFromLink(url="https://aws.random.cat/meow", json=True, jsonType='file', returnFile=True, filename='Cat.png')
        await ctx.send("From PPT with \U0001F49A")
        await ctx.send(file=data)

    @commands.command(
        name='dog',
        brief='Sends an image of a heckin good doggo ꓷ:',
        help='Fucking furry.')
    async def sendDog(self,ctx):
        data = await gp.getDataFromLink(url="https://dog.ceo/api/breeds/image/random", json=True, jsonType='message', returnFile=True, filename='Dog.png')
        await ctx.send("From PPT with \U0001F49A")
        await ctx.send(file=data)

    @commands.command(
        name='s',
        brief='Sends a wallpaper.',
        help='Sends a wallpaper with size of 1920x1080')
    async def sendWallpaper(self,ctx):
        data = await gp.getDataFromLink(url="https://picsum.photos/1920/1080", returnFile=True, filename='Why are you looking at this.png')
        await ctx.send(file=data)
        
    @commands.command(
        name="quote",
        brief="Sends a quote from a movie/anime.",
        help="Sends a random quote")
    async def sendQuote(self,ctx):
        url = requests.get('https://animechan.vercel.app/api/random').json()
        await ctx.send(f"A quote from {url['character']} : {url['quote']}")

    @commands.command(
        aliases=['re', 'ree', 'reee', 'reeee'],
        brief='It just \'***REEEEEE***\'s lmao',
        help='***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
    async def sendRee(self,ctx):
        num = random.randint(10,100)
        await ctx.send("*R" + "E" * num + "*")

    @commands.command(
        name="ily",
        brief="Draf is tooo lazy to type it",
        help="ily * num")
    async def sendIly(self, ctx):
        num = random.randint(10, sys.maxsize)
        await ctx.send("ily " + str(num))


def setup(bot):
    bot.add_cog(webmaster(bot))