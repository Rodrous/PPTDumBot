from discord.ext import commands
import discord,base64,typing
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
        help='This bot is just pain with extra steps')
    async def sendInvite(self,ctx):
        if str(ctx.message.guild.id) in allowedguilds:
             await ctx.send(
                "This was a mistake\n<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
        else:
            await ctx.send(content='You cant use that here yet.', delete_after=6)


    @commands.command(
        name='ping',
        brief='Pong',
        help='Returns the delay of the bot')
    async def ping(self,msg):
        embed = discord.Embed()
        embed.add_field(name="Pong", value=f"{round(self.bot.latency * 1000)}ms")
        await msg.send(embed=embed)

    @commands.command(
        name = 'steal',
        brief = 'FBI OPEN UP',
        help = 'Yoink an emoji, with the given name or the emoji name')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_emojis = True)
    @commands.has_permissions(manage_emojis=True)
    async def stealEmoji(self, ctx, *, args = ''):
        gLimit = ctx.guild.emoji_limit
        gCurr = len(await ctx.guild.fetch_emojis())
        #print(str(gCurr)+'/'+str(gLimit)+' emojis')
        if gCurr >= gLimit:
                return await ctx.send("This server is already at the limit and cant have more emojis **):**")
        turl = 'https://cdn.discordapp.com/emojis/'
        if args == '':
            return await ctx.send("No emoji or link detected.")
        try:

            msg = args.split()
            if reg.match(pattern='https://cdn.discordapp.com/emojis/', string=msg[0]):
                data = await gp.getDataFromLink(url=str(msg[0]), fileName='WhyAreYouLookingAtThis')
                name = '_'.join(msg[1:]) or 'RandomName'
                newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

            else:
                if reg.match(pattern='<a?:.*:\d*>',string=msg[0]):
                    name = '_'.join(msg[1:]) or (''.join(reg.findall(pattern='(?<=:)[a-zA-Z1-9~_]*(?=:)', string=msg[0])))
                else:
                    return await ctx.send("Wrong Input detected. Not an emoji.")

                eid = int(''.join(reg.findall(pattern='(?<=:)\d*(?=>)', string=msg[0])))

                if reg.match(pattern='<a:',string=msg[0]) is not None:
                    turl += str(eid) + '.gif'
                else:
                    turl += str(eid) + '.png'
                    #url = f"https://cdn.discordapp.com/emojis/853662523843674112.png"

                    data = await gp.getDataFromLink(url=turl, fileName="WhyAreYouLookingAtThis")

                    newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                    return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

        except Exception as e:
                print(f"There is some Error Here, error is defined by: {e}")




def setup(bot):
    bot.add_cog(syscom(bot))