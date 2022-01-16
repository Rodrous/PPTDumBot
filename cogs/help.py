from discord.ext import commands
import discord

from build.generalPurpose import dumbot
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu import menus, initialize
from helpMenu.react import React, startupLoop


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
            if not foundCommand:
                embed = discord.Embed(
                    title="404: Not Found",
                    description=f"Command {requestedCommand} not found",
                    color=discord.Colour.red()
                )
                await ctx.send(embed=embed)
                return
            desc = str(foundCommand).format(Prefix=prefix)
            embed = discord.Embed(
                title=foundCommand.Name,
                description=desc,
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
