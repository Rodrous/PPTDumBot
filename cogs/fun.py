from discord.ext import commands
import requests,aiohttp,io,discord,random,sys
from build import generalPurpose as gp
import re as reg

#sends images and quotes
class webmaster(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name='cat',
        brief='Sends an image of a cute (*most of the times*) cat ꓷ:',
        help='Sends a cat image.')
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
        author_allowed_ids= [323457305855262721, 579036541238640731]
        if author_allowed_ids.__contains__(ctx.author.id):
            randomint = str("1" + "0" * random.randint(10,100))
            num = random.randint(10,int(randomint))
            await ctx.send("ily " + str(num))
        else:
            await ctx.send("you cant use that", delete_after=6)

    @commands.command(
        name="say",
        brief="repeats your shit",
        help="repeat")
    async def sendRepeat(self,ctx,*,args):
        args_string=str(args)
        await ctx.message.channel.purge(limit=1)
        if reg.match(pattern='@everyone|@here', string=args_string.lower()):
            await ctx.send('Fuck you, you cant loophoel dis', delete_after=6)
        else:
            await ctx.send(args)



def setup(bot):
    bot.add_cog(webmaster(bot))