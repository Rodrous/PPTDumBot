from discord.ext import commands
import discord,base64,typing

with open("config/allowedguildIds.txt") as file:
    f = file.readlines()

allowedguilds = [base64.b64decode(i).decode('utf-8')  for i in f]

class moderation(commands.Cog):
        def __init__(self,bot):
            self.bot=bot

        @commands.command(
            name='invite',
            brief='Please dont use this.',
            help='This bot is just pain with extra steps')
        async def sendInvite(self, ctx):
            if str(ctx.message.guild.id) in allowedguilds:
                await ctx.send(
                    "This was a mistake\n<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")
            else:
                await ctx.send(content='You cant use that here yet.', delete_after=6)

        @commands.command(
            name='clear',
            aliases=['purge'],
            help='Clears a certain amount of messages in the current chat.',
            brief='!clear <somenumber>')
        @commands.has_permissions(manage_messages=True)
        async def clearChat(self, ctx, amount: typing.Optional[int] = 1):
            await ctx.message.channel.purge(limit=int(amount))

def setup(bot):
    bot.add_cog(moderation(bot))