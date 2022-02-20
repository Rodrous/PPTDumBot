import asyncio

import discord
from discord.ext import commands

from general import checks, colors
from general.generalPurpose import Dumbot
from general.returnCodes import ReturnCode
from helpMenu import menus, initialize
from helpMenu.commands import RestrictedCategory
from helpMenu.eventHandler import EventHandler
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.react import React, MenuFactory, AddReactions

context = discord.ext.commands.Context


class HelpMenu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
                name = 'help',
                aliases = ['helpme'],
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def SendHelp(self, ctx: context, *, args=""):
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
            requested_command = args[0].lower()
            found_command = await HelpMenuEntry.PublicSearch(requested_command)
            embed = await _BuildEmbed(found_command, requested_command, prefix)
            await ctx.send(embed=embed)

    @checks.private()
    @commands.command(
        name="personalhelp",
        aliases=["phelp", "pershelp", "privhelp", "privatehelp"])
    async def personalHelp(self, ctx, *, args=""):
        await initialize.PrivateCommands()
        tasks = await asyncio.gather(
            Dumbot.get_prefix(ctx, self.bot),
            ctx.message.channel.purge(limit=1),
            initialize.PrivateCommands()
        )
        args = args.split()
        prefix = tasks[0][2]
        if not args:
            embed = await menus.Private(prefix)
            await ctx.send(embed=embed)
        else:
            requested_command = args[0].lower()
            found_command = await HelpMenuEntry.PrivateSearch(requested_command, RestrictedCategory.Private)
            embed = await _BuildEmbed(found_command, requested_command, prefix)
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
        event = EventHandler.GetEvent(ctx)
        if event.reaction:
            return
        tasks = await asyncio.gather(
            event.SetReaction(react.emoji),
            Dumbot.get_prefix(ctx, self.bot),
            initialize.PublicCommands()
        )
        return_code = tasks[0]
        prefix = tasks[1][2]
        if return_code is ReturnCode.Unchanged:
            return
        try:
            embed, reactions = await MenuFactory(react.emoji, prefix)
        except ValueError as e:
            print(e)
            return
        await React(event, embed, reactions)


async def _BuildEmbed(found_command: HelpMenuEntry, requested_command: str, prefix: str) -> discord.Embed:
    if not found_command:
        return discord.Embed(
            title="404: Not Found",
            description=f"Command {requested_command} was not found",
            color=colors.Fault.ERROR
        )
    desc = found_command.BuildDesc()
    if found_command.flags:
        flags = [str(flag) for flag in found_command.flags]
        desc += "\n\n**Flags:**\n" + "\n".join(flags)
    return discord.Embed(
        title=found_command.name,
        description=desc.format(prefix=prefix),
        color=found_command.category.value
    )


def setup(bot):
    bot.add_cog(HelpMenu(bot))
