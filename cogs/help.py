import discord
from discord.ext import commands

from build import checks
from build.generalPurpose import Dumbot
from helpMenu import menus, initialize
from helpMenu.commands import RestrictedCategory
from helpMenu.eventHandler import EventHandler
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.react import React, MenuFactory, AddReactions

context = discord.ext.commands.Context


class getHelp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(
                name = 'help',
                aliases = ['helpme'],
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx: context, *, args=""):
        args = args.split()
        pf = await Dumbot.get_prefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            intro, reactions = await menus.Intro(prefix)
            msg = await ctx.send(embed=intro)
            event = EventHandler.GetEvent(msg)
            await AddReactions(msg, event, reactions)
        else:
            await initialize.PublicCommands()
            requestedCommand = args[0].lower()
            foundCommand = await HelpMenuEntry.PublicSearch(requestedCommand)
            embed = await _BuildEmbed(foundCommand, requestedCommand)
            await ctx.send(embed=embed)

    @checks.private()
    @commands.command(
        name="personalhelp",
        aliases=["phelp", "pershelp", "privhelp", "privatehelp"])
    async def personalHelp(self, ctx, *, args=""):
        await ctx.message.channel.purge(limit=1)
        args = args.split()
        pf = await Dumbot.get_prefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            await initialize.PrivateCommands()
            embed = await menus.Private(prefix)
            await ctx.send(embed=embed)
        else:
            requestedCommand = args[0].lower()
            foundCommand = await HelpMenuEntry.PrivateSearch(requestedCommand, RestrictedCategory.Private)
            embed = await _BuildEmbed(foundCommand, requestedCommand)
            await ctx.send(embed=embed)

    @checks.devsOnly()
    @commands.command(
        name="devhelp"
    )
    async def devHelp(self, ctx, *, args=""):
        await ctx.send("Not Implemented Yet!")

    @commands.Cog.listener()
    async def on_reaction_add(self, react, user):
        if user.bot:
            return
        ctx = react.message
        pf = await Dumbot.get_prefix(ctx, self.bot)
        prefix = pf[2]
        event = EventHandler.GetEvent(ctx)
        try:
            embed, reactions = await MenuFactory(react.emoji, prefix)
        except ValueError as e:
            print(e)
            return
        await React(event, embed, reactions)


async def _BuildEmbed(FoundCommand: HelpMenuEntry, RequestedCommand: str) -> discord.Embed:
    if FoundCommand:
        embed = discord.Embed(
            title=FoundCommand.Name,
            description=FoundCommand.BuildDesc(),
            color=FoundCommand.Category.value
        )
    else:
        embed = discord.Embed(
            title="404: Not Found",
            description=f"Command {RequestedCommand} was not found",
            color=discord.Color.red()
        )
    return embed


def setup(bot):
    bot.add_cog(getHelp(bot))
