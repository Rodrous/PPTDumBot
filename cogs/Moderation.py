from discord.ext import commands
import discord, base64, typing, asyncio
from build.generalPurpose import Dumbot
from build.backEnd import mute,unmute
import os

allowedguilds = [os.environ.get('allowedGuild')]


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    # ------------------------------------------------------------------------------

    @commands.command(
        name='clear',
        aliases=['purge'],
        help='Clears a certain amount of messages in the current chat.',
        brief='!clear <somenumber>')
    @commands.has_permissions(manage_messages=True)
    async def clearChat(self, ctx, amount: typing.Optional[int] = 1):
        await ctx.message.channel.purge(limit=int(amount))

    # ------------------------------------------------------------------------------

    @commands.command(
        help="Mutes a person, Format:- <user> <time in minutes (Default=10)> <reason> (Default= Being a Biotch)"
    )
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: discord.Member, time=10, reason="being a biotch"):
        getRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await mute(ctx.guild.id, user.id)

        if not getRole:
            try:
                muted = await ctx.guild.create_role(name="Muted", reason="Because People do be bitch")
                for i in ctx.guild.channels:
                    await i.set_permissions(muted, send_messages=False,
                                            read_message_history=False,
                                            read_messages=False,
                                            add_reactions=False)
            except Exception as e:
                print(f"Fuck you!:- {e}")
                await Dumbot.send_error_to_channel(self, ctx, e)
            await user.add_roles(getRole)
        else:
            await user.add_roles(getRole)
        await ctx.send("Done!")
        await user.send(f"You were muted because {reason}")
        await asyncio.sleep(int(time) * 60)
        await user.remove_roles(getRole)

    @commands.command(
        help="Unmutes a person"
    )

    async def unmute(self, ctx, user: discord.Member):
        await unmute(ctx.guild.id, user.id)
        getRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(getRole)
        await ctx.send("Done!")

def setup(bot):
    bot.add_cog(moderation(bot))