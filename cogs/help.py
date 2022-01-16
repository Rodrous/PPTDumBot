from discord.ext import commands
import discord

from build.checks import private
from build.generalPurpose import dumbot
from helpMenu.commands import RestrictedCategory
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu import menus, initialize
from helpMenu.react import React, startupLoop


async def BuildCommandMenu(ctx, FoundCommand: HelpMenuEntry, RequestedCommand: str, Prefix: str):
    if not FoundCommand:
        embed = discord.Embed(
            title="404: Not Found",
            description=f"Command {RequestedCommand} not found",
            color=discord.Colour.red()
        )
        await ctx.send(embed=embed)
        return
    desc = str(FoundCommand).format(Prefix=Prefix)
    embed = discord.Embed(
        title=FoundCommand.Name,
        description=desc,
        color=FoundCommand.Category.value
    )
    await ctx.send(embed=embed)


class getHelp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help',
        aliases=['helpme'],
        brief='This is like help, but better.',
        help='What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx, *, args=''):
        await initialize.PublicCommands()
        args = args.split()
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            intro, reactions = await menus.Intro(prefix)
            embed: discord.Message = await ctx.send(embed=intro)
            startupLoop[embed.id] = True
            for react in reactions:
                await embed.add_reaction(react.value)
            del startupLoop[embed.id]
        else:
            requestedCommand = args[0]
            foundCommand: HelpMenuEntry = HelpMenuEntry.PublicSearch(requestedCommand)
            await BuildCommandMenu(ctx, foundCommand, requestedCommand, prefix)

    @private
    @commands.command(
        name="personalhelp",
        aliases=["phelp", "pershelp", "privhelp", "privatehelp"])
    async def personalHelp(self, ctx, *, args=''):
        await initialize.PrivateCommands()
        await ctx.message.channel.purge(limit=1)
        args = args.split()
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            embed = await menus.Private(prefix)
            await ctx.send(embed=embed, delete_after=60)
        else:
            requestedCommand = args[0]
            foundCommand: HelpMenuEntry = HelpMenuEntry.PrivateSearch(requestedCommand, RestrictedCategory.Private)
            await BuildCommandMenu(ctx, foundCommand, requestedCommand, prefix)

    @commands.Cog.listener()
    async def on_reaction_add(self, react, un):
        # fixme reaction bug, need event handler to get latest event on message
        ctx = react.message
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        await React(ctx, react, un, prefix)


def setup(bot):
    bot.add_cog(getHelp(bot))
