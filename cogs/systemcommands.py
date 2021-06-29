from asyncio.windows_events import NULL
from discord.ext import commands
import discord,base64
import re as reg
import requests,aiohttp,io

with open("config/allowedguildIds.txt") as file:
    f = file.readlines()

allowedguilds = [base64.b64decode(i).decode('utf-8')  for i in f]

restrictedChannels = ["database"]

class syscom(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name='invite',
        brief='Please dont use this.',
        help='Pwease dont use this uwu')
    async def sendInvite(self,ctx):
        if str(ctx.message.guild.id) in allowedguilds:
            await ctx.send("This was a mistake")
            await ctx.send(
                "<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
        else:
            await ctx.send(content='You cant use that here yet.', delete_after=6)

    @commands.command(
        name='ping',
        brief='Pong',
        help='Returns the delay of the bot')
    async def ping(self,ctx):
        embed = discord.Embed()
        embed.add_field(name="Pong", value=f"{round(self.bot.latency * 1000)}ms")
        await ctx.send(embed=embed)

    @commands.command(
        name = 'steal',
        brief = 'Yoink an emoji',
        help = 'FBI OPEN UP')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_emojis = True)
    async def stealEmoji(self, ctx, *, args = ''):
        # gLimit = ctx.guild.emoji_limit
        # gCurr = len(await ctx.guild.fetch_emojis())
        # turl = 'https://cdn.discordapp.com/emojis/'
        # if args != '':
        #     msg = args.split()

        #     if reg.match(pattern='<a?:.*:\d*>',string=msg[0]):
        #         name = '_'.join(msg[1:]) or (''.join(reg.findall(pattern='(?<=:)[a-zA-Z1-9~_]*(?=:)', string=msg[0])))
        #     else:
        #         await ctx.send("Wrong Input detected. Not an emoji.")
        #         return

        #     eid = int(''.join(reg.findall(pattern='(?<=:)\d*(?=>)', string=msg[0])))
        #     emoj = commands.Bot.get_emoji(self=ctx.bot, id=eid)
        #     eimgbytes = await emoj.url.read()
        #     print (emoj.url)

        #     if gCurr >= gLimit:
        #         await ctx.send("This server is already at the limit and cant have more emojis **):**")
        #         return
            
        #     newEm = await ctx.guild.create_custom_emoji(name=name, image=eimgbytes, reason=f'{ctx.author.mention} triggered the command : $steal')
        #     await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')
        # else:
        #     await ctx.send("No emoji detected.")
        #     return

        url = f"https://cdn.discordapp.com/emojis/853662523843674112.png"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await ctx.send("Couldn't download the file")
                data = io.BytesIO(await response.read())
                await ctx.send("From PPT with \U0001F49A")
                await ctx.send(file=discord.File(data, "Cat.png"))
        



def setup(bot):
    bot.add_cog(syscom(bot))