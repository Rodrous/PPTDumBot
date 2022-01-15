from discord.ext import commands
import discord
import re as reg
import asyncio
from typing import List

from build.generalPurpose import dumbot
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.commands import CommandCategory
from helpMenu.entry import *

bot_avatar = dumbot.avatar()


async def InitializeCommands():
    await asyncio.gather(
        fun.Init(),
        games.Init(),
        moderation.Init(),
        utility.Init()
    )


async def IntroMenu(prefix):
    embed = discord.Embed(
        title="Help Menu",
        description=
        f"**Server Prefix:** `{prefix}`"
        "\n\n**React with:**"
        "\n<:PepeLmao:865712134439436328> For Fun"
        "\n<:PepoGamer:865712213141356565> For Games"
        "\n<a:pepeAnimeCaught:865712704315850782> For Utility"
        "\n<a:pepeban:865714938667991091> For Moderation"
        , color=11187115)
    embed.set_author(name='Server Index',
                     icon_url=bot_avatar)
    reactions = ['<:PepeLmao:865712134439436328>', '<:PepoGamer:865712213141356565>', '<a:pepeAnimeCaught:865712704315850782>', '<a:pepeban:865714938667991091>']  # fun, games, utility, moderation
    return embed, reactions


async def CreateDescription(Prefix: str, Category: CommandCategory) -> str:
    desc = ''
    cmds: List[HelpMenuEntry] = HelpMenuEntry.GetCategory(Category, AsList=True)
    for cmd in cmds:
        desc += f"`{Prefix}{cmd.Name.lower()}` {cmd.Brief}\n"
    return desc


async def FunHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Fun)
    embed = discord.Embed(
        title='Fun Commands',
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Fun.value)
    embed.set_author(name="Server Index -> Fun Commands",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


async def GamesHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Game)
    embed = discord.Embed(
        title="Games",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Game.value)
    embed.set_author(name="Server Index -> Games",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


async def UtilityHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Utility)
    embed = discord.Embed(
        title="Utility Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}\n"
        "If you send a message link in this server you can show the message Cross Channels"

        , color=CommandCategory.Utility.value)
    embed.set_author(name="Server Index -> Utility Commands",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


async def ModerationHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Moderation)
    embed = discord.Embed(
        title="Moderation Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Moderation.value)
    embed.set_footer(text="\U00002193 React to return")
    embed.set_author(name="Server Index -> Moderation Commands",
                     icon_url=bot_avatar)
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


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
            intro, reactions = await IntroMenu(prefix)
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
        emote = str(react.emoji)
        if ctx.embeds:
            embed = ctx.embeds[0]
            embedAuthorField = embed.author.name
            if not un.bot and ctx.author.id == 852977382016024646 and reg.search(pattern=r'\AServer Index', string=embedAuthorField):
                await InitializeCommands()
                pf = await dumbot.getPrefix(ctx, self.bot)
                prefix = pf[2]
                if emote == "<:return:867101369814745099>":  # return
                    embed, reactions = await IntroMenu(prefix)
                elif emote == '<:PepeLmao:865712134439436328>':  # fun
                    embed, reactions = await FunHelp(prefix)
                elif emote == '<:PepoGamer:865712213141356565>':  # games
                    embed, reactions = await GamesHelp(prefix)
                elif emote == '<a:pepeAnimeCaught:865712704315850782>':  # utility
                    embed, reactions = await UtilityHelp(prefix)
                elif emote == '<a:pepeban:865714938667991091>':  # moderation
                    embed, reactions = await ModerationHelp(prefix)
                else:
                    embed, reactions = None, None
                if embed and reactions:
                    await ctx.clear_reactions()
                    await ctx.edit(embed=embed)
                    for react in reactions:
                        await ctx.add_reaction(emoji=react)


def setup(bot):
    bot.add_cog(getHelp(bot))
