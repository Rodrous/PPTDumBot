from discord.ext import commands
import requests, random
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
        get_image_url = requests.get(f"https://aws.random.cat/meow").json()
        url = get_image_url['file']
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await ctx.send("Couldn't download the file")
                data = io.BytesIO(await response.read())
                await ctx.send("From PPT with \U0001F49A")
                await ctx.send(file=discord.File(data, "Cat.png"))

    @commands.command(
        name='dog',
        brief='Sends an image of a heckin good doggo ꓷ:',
        help='Fucking furry.')
    async def sendDog(self,ctx):
        get_image_url = requests.get(f"https://dog.ceo/api/breeds/image/random").json()
        url = get_image_url['message']
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await ctx.send("Couldn't download the file")
                data = io.BytesIO(await response.read())
                await ctx.send(content="From PPT with \U0001F49A",
                               file=discord.File(data, "dog.png"))

    @commands.command(
        name='s',
        brief='Sends a wallpaper.',
        help='Sends a wallpaper with size of 1920x1080')
    async def sendWallpaper(self,ctx):
        url = f"https://picsum.photos/1920/1080"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await ctx.send("Couldn't download the file..")
                data = io.BytesIO(await response.read())
                await ctx.send(file=discord.File(data, "Why are you looking at this.png"))

    @commands.command(
        name="quote",
        brief="Sends a quote from a movie/anime.",
        help="I mean, what else do you need to know. It sends a quote from a movie/anime. Thats it bruv.")
    async def sendQuote(self,ctx):
        url = requests.get('https://animechan.vercel.app/api/random').json()
        await ctx.send(f"A quote from {url['character']} : {url['quote']}")

    @commands.command(
        aliases=['re', 'ree', 'reee', 'reeee'],
        brief='It just \'***REEEEEE***\'s lmao',
        help='***REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE***')
    async def sendRee(self,ctx):
        num = random.randint(1, 100)
        await ctx.send("*R" + "E" * num + "*")

def setup(bot):
    bot.add_cog(webmaster(bot))