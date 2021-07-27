import discord
from discord.ext import commands
import requests,random
from build import generalPurpose as gp
from build.library import moviequotes
import re as reg
import wikipedia

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
        name='wallpaper',
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
        if str(args).count('-ex') >= 1:
            url = requests.get('https://v2.jokeapi.dev/joke/Any').json()
        else:
            url = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode').json()
        if url['type'] == 'single':
            await ctx.send(url['joke'])
        elif url['type'] == 'twopart':
            await ctx.send(f"{url['setup']}\n{url['delivery']}")

    @commands.command(
        name="dadjoke",
        brief='i hate my life',
        help='you hate me')
    async def sendDadjoke(self,ctx):
        url = requests.get("https://icanhazdadjoke.com/", headers={"accept" : "application/json"}).json()
        await ctx.send(url['joke'])

    @commands.command(
        name='yomomma',
        aliases=['yourmom', 'yomom'],
        brief='we like mom jokes',
        help='sends a random yomomma joke')
    async def sendMomjoke(self,ctx):
        url = requests.get('https://api.yomomma.info/').json()
        await ctx.send(url['joke'])

    @commands.command(
        name='moviequotes',
        aliases=['mq', 'moviequote'])
    async def movieQuote(self,ctx,*,args = ''):
        args = args.lower().split()
        pf = await gp.getPrefix(ctx, self.bot)
        prefix = pf[2]
        error_message = {'movie': 'Error 404','character': '',
                     'quote': f'It was not found, make sure it was the right syntax\nDo `{prefix}help moviequotes` for info on syntax',
                     'id': 'Contact PPT/Finix/Giraffe if you think its been a mistake',
                     'image': ''}
        if not args or args[0] == 'random':
            quote = await moviequotes.random()
        elif args[0] == 'get':
            try:
                quote = await moviequotes.GET(int(args[1]))
            except Exception as e:
                print(f"Quote fail Get: {e}")
                quote = error_message
        elif args[0] == 'per':
            try:
                string = "\s".join(args[2:])
                quote = await moviequotes.per(args[1], string)
            except Exception as e:
                print(f"Quote fail Per: {e}")
                quote = error_message
        else:
            quote = error_message

        await ctx.send('__**This has not been fully implemented yet**__')
        string = f'{quote["quote"]}'
        if quote["character"]:
            string = string + f'\n**-{quote["character"]}**'
        embed = discord.Embed(title=quote['movie'] ,description=string, color= 4029286)
        embed.set_footer(text=f"Quote ID: {quote['id']}")
        if quote["image"]:
            embed.set_thumbnail(url=quote["image"])
        await ctx.send(embed= embed)


    @commands.Cog.listener()
    async def on_message(self, msg):
        if reg.search(pattern=r'\bours?\b', string=msg.content, flags=reg.I) and not msg.author.bot:
            seq = ["<:doggo:863639575666098186>", "<:pepCom:863639491533340682>", "<:BlackCom:863642798070431744>",
                   "<:Star:863642810879443004>", "<a:Communist:863640421628641320>", "<:comthumb:863646009334169651>",
                   "<:usrBall:863646049028276234>", "<:yeye:863647634361942018>", '<:russianpepe:863647634001887273>']
            rand = random.choice(seq)
            await msg.add_reaction(rand)

    @commands.command(
        name='wikipedia',
        aliases=['wiki']
    )
    async def wikime(self,ctx,*,arg):
        try:
            data = wikipedia.summary(arg,sentences=7,auto_suggest=False)
            await ctx.send(data)
        except wikipedia.exceptions.DisambiguationError as e:
           print(type(e))
           await ctx.send("The Search is highly vauge, it gave multiple outputs which *I* cannot send. Try Something on-point")
        except Exception as e:
            await ctx.send("Idk what the fuck happened, ping PPT/Finix/Draf")
            print(e)


def setup(bot):
    bot.add_cog(webmaster(bot))