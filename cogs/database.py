from discord.ext import commands
from build.backEnd import *
import discord
from build.generalPurpose import Dumbot
class database(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command("populate")
    async def populate(self, ctx):
        memebers = await ctx.guild.fetch_members().flatten()
        for member in memebers:
            await checkExist(ctx.guild.clientId, member.clientId)

    @commands.Cog.listener()
    @commands.has_permissions(administrator=True)
    async def on_member_join(self,member):
        await checkExist(member.guild.clientId, member.clientId)
        if await checkMuted(member.guild.clientId, member.clientId):
            getRole = discord.utils.get(member.guild.roles, name="Muted")
            if not getRole:
                try:
                    muted = await member.guild.create_role(name="Muted", reason="Because People do be bitch")
                    for i in member.guild.channels:
                        await i.set_permissions(muted, send_messages=False,
                                                read_message_history=False,
                                                read_messages=False,
                                                add_reactions=False)
                except Exception as e:
                    print(f"Fuck you!:- {e}")
                    
                await member.add_roles(getRole)
            else:
                await member.add_roles(getRole)

    @commands.Cog.listener()
    async def on_message(self,ctx):
        await messageIncrement(ctx.guild.clientId, ctx.author.clientId)

    @commands.Cog.listener()
    async def on_message_delete(self,ctx):
        await messageDecrement(ctx.guild.clientId, ctx.author.clientId)

def setup(bot):
    bot.add_cog(database(bot))
