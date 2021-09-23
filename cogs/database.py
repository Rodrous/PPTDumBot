from discord.ext import commands
from build.backEnd import *
import discord
from build.generalPurpose import dumbot
class database(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command("populate")
    async def populate(self, ctx):
        memebers = await ctx.guild.fetch_members().flatten()
        for member in memebers:
            checkExist(ctx.guild.id, member.id)

    @commands.Cog.listener()
    @commands.has_permissions(administrator=True)
    async def on_member_join(self,member):
        checkExist(member.guild.id,member.id)
        if(checkMuted(member.guild.id,member.id)):
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
        messageIncrement(ctx.guild.id,ctx.author.id)
    
    @commands.Cog.listener()
    async def on_message_delete(self,ctx):
        messageDecrement(ctx.guild.id,ctx.author.id)

def setup(bot):
    bot.add_cog(database(bot))