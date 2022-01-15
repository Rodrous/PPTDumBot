from discord.ext import commands
import discord

from build.generalPurpose import dumbot
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu import menus
from helpMenu.react import React
from helpMenu.initialize import InitializeCommands


class getHelp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help',
        aliases=['helpme'],
        brief='This is like help, but better.',
        help='What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx, *, args=''):
        await InitializeCommands()
        args = args.split()
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            intro, reactions = await menus.Intro(prefix)
            embed = await ctx.send(embed=intro)
            for react in reactions:
                await embed.add_reaction(emoji=react)
        else:
            requestedCommand = args[0]
            foundCommand: HelpMenuEntry = HelpMenuEntry.GetCommand(requestedCommand)
            if not foundCommand:
                embed = discord.Embed(
                    title="404: Not Found",
                    description=f"Command {requestedCommand} not found",
                    color=discord.Colour.red()
                )
                await ctx.send(embed=embed)
                return
            desc = f"**Category:** {foundCommand.Category.name}\n" \
                   f"**Brief:** {foundCommand.Brief}"
            if foundCommand.Aliases:
                desc += f"\n**Aliases:** {', '.join(foundCommand.Aliases)}"
            if foundCommand.Syntax:
                desc += "\n**Syntax:** `" + foundCommand.Syntax.format(Prefix=prefix) + "`"
            embed = discord.Embed(
                title=foundCommand.Name,
                description=desc + f"\n\n{foundCommand.Desc}",
                color=foundCommand.Category.value
            )
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_add(self, react, un):
        # fixme reaction bug, need event handler to get latest event on message
        ctx = react.message
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        await React(ctx, react, un, prefix)


def setup(bot):
    bot.add_cog(getHelp(bot))
