from discord.ext import commands
import discord,base64

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
    async def ping(self,msg):
        embed = discord.Embed()
        embed.add_field(name="Pong", value=f"{round(self.bot.latency * 1000)}ms")
        await msg.send(embed=embed)



def setup(bot):
    bot.add_cog(syscom(bot))