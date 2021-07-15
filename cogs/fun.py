from discord.ext import commands
import requests,random
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
        name="ily",
        brief="Draf is tooo lazy to type it",
        help="ily * num + name")
    async def sendIly(self, ctx):
        allowed_ids = [323457305855262721, 579036541238640731] #[DRAF, NISSY]
        AUTHOR = ctx.author.id
        if allowed_ids.__contains__(AUTHOR):
            randomint = "1" + "0" * random.randint(10,100)
            num = random.randint(10,int(randomint))
            DRAF = allowed_ids[0]
            NISSY = allowed_ids[1]
            if AUTHOR == DRAF:
                name = NISSY
            elif AUTHOR == NISSY:
                name = DRAF
            await ctx.send("ily " + str(num) + f" <@{name}>")
        else:
            await ctx.send("you cant use that", delete_after=6)

    @commands.command(
        name="say",
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
        name='minesweeper',
        aliases=['ms'])
    async def mineSweeper(self,ctx,rows = 8, columns = 8, mines = 5):
        run = True
        if int(rows) > 11:
            run = False
        if int(columns) > 9:
            run = False
        if int(mines) < 3:
            run = False
        if int(mines) >= int(rows) - 1 or int(mines) >= int(columns) - 1:
            run = False
        if run:
            arr = [[0 for column in range(int(columns))] for rows in range(int(rows))]
            border_x = columns - 1
            border_y = rows - 1
            for num in range(int(mines)):
                x = random.randint(0, border_x)
                y = random.randint(0, border_y)
                arr[y][x] = 'X'
                if x != border_x:
                    if arr[y][x + 1] != 'X':  # right
                        arr[y][x + 1] += 1
                if x != 0:
                    if arr[y][x - 1] != 'X':  # left
                        arr[y][x - 1] += 1
                if y != border_y:
                    if arr[y + 1][x] != 'X':  # up
                        arr[y + 1][x] += 1
                if y != 0:
                    if arr[y - 1][x] != 'X':  # down
                        arr[y - 1][x] += 1
                if y != border_y and x != border_x:
                    if arr[y + 1][x + 1] != 'X':  # up right
                        arr[y + 1][x + 1] += 1
                if y != 0 and x != border_x:
                    if arr[y - 1][x + 1] != 'X':  # down right
                        arr[y - 1][x + 1] += 1
                if y != border_y and x != 0:
                    if arr[y + 1][x - 1] != 'X':  # up left
                        arr[y + 1][x - 1] += 1
                if y != 0 and x != 0:
                    if arr[y - 1][x - 1] != 'X':  # down left
                        arr[y - 1][x - 1] += 1
            ms = ''
            for row in arr:
                if ms:
                    ms = f'{ms}\n' + " ".join(str(cell) for cell in row)
                else:
                    ms = " ".join(str(cell) for cell in row)
            replace = {'X': '||:boom:||', '0': '||:zero:||', '1': '||:one:||', '2': '||:two:||', '3': '||:three:||',
                       '4': '||:four:||'}
            for item in replace:
                ms = ms.replace(item, replace[item])
            await ctx.send(ms)
        else:
            await ctx.send('Max rows is 11, max columns is 9 and minumum bombs is 3, and no weird numbers\nSyntax is `minesweeper [rows] [columns] [mines]`')

    @commands.Cog.listener()
    async def on_message(self, message):
        if reg.search(pattern=r'\bours?\b', string=message.content, flags=reg.I):
            seq = ["<:doggo:863639575666098186>", "<:pepCom:863639491533340682>", "<:BlackCom:863642798070431744>",
                   "<:Star:863642810879443004>", "<a:Communist:863640421628641320>", "<:comthumb:863646009334169651>",
                   "<:usrBall:863646049028276234>", "<:yeye:863647634361942018>", '<:russianpepe:863647634001887273>']
            rand = random.choice(seq)
            await message.add_reaction(rand)


def setup(bot):
    bot.add_cog(webmaster(bot))