from discord.ext import commands
import discord,base64
import re as reg
from build import generalPurpose as gp

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
            await ctx.send(
                "This was a mistake\n<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
        else:
            await ctx.message.channel.purge(limit=int(1))
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
        brief = 'FBI OPEN UP',
        help = 'Yoink an emoji, with the given name or the emoji name')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_emojis = True)
    async def stealEmoji(self, ctx, *, args = ''):
        gLimit = ctx.guild.emoji_limit
        gCurr = len(await ctx.guild.fetch_emojis())
        turl = 'https://cdn.discordapp.com/emojis/'
        if args != '':
            msg = args.split()

            if reg.match(pattern='<a?:.*:\d*>',string=msg[0]):
                name = '_'.join(msg[1:]) or (''.join(reg.findall(pattern='(?<=:)[a-zA-Z1-9~_]*(?=:)', string=msg[0])))
            else:
                return await ctx.send("Wrong Input detected. Not an emoji.")
            
            if gCurr >= gLimit:
                return await ctx.send("This server is already at the limit and cant have more emojis **):**")

            eid = int(''.join(reg.findall(pattern='(?<=:)\d*(?=>)', string=msg[0])))

            if reg.match(pattern='<a:',string=msg[0]) is not None:
                turl += str(eid) + '.gif'
            else:
                turl += str(eid) + '.png'
            #url = f"https://cdn.discordapp.com/emojis/853662523843674112.png"

            tfile = await gp.getDataFromLink(url=turl,json=False,returnFile=False,fileName="WhyAreYouLookingAtThis.png")
            
            newEm = await ctx.guild.create_custom_emoji(name=name, image=tfile.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
            return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')
        else:
            return await ctx.send("No emoji detected.")

        
        



def setup(bot):
    bot.add_cog(syscom(bot))