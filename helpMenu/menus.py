from typing import List

import discord

from helpMenu.commands import PublicCategory, RestrictedCategory, CommandCategory
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.reactions import Reaction
from build.generalPurpose import dumbot

botAvatar = dumbot.avatar()


async def Intro(prefix):
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
                     icon_url=botAvatar)
    reactions = [Reaction.Fun, Reaction.Games, Reaction.Utility, Reaction.Moderation]
    return embed, reactions


async def Fun(Prefix):
    description = await _CreateDescription(Prefix, PublicCategory.Fun)
    embed = discord.Embed(
        title='Fun Commands',
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=PublicCategory.Fun.value)
    embed.set_author(name="Server Index -> Fun Commands",
                     icon_url=botAvatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = [Reaction.Return]
    return embed, reactions


async def Games(Prefix):
    description = await _CreateDescription(Prefix, PublicCategory.Game)
    embed = discord.Embed(
        title="Games",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=PublicCategory.Game.value)
    embed.set_author(name="Server Index -> Games",
                     icon_url=botAvatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = [Reaction.Return]
    return embed, reactions


async def Utility(Prefix):
    description = await _CreateDescription(Prefix, PublicCategory.Utility)
    embed = discord.Embed(
        title="Utility Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}\n"
        "If you send a message link in this server you can show the message Cross Channels"

        , color=PublicCategory.Utility.value)
    embed.set_author(name="Server Index -> Utility Commands",
                     icon_url=botAvatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = [Reaction.Return]
    return embed, reactions


async def Moderation(Prefix):
    description = await _CreateDescription(Prefix, PublicCategory.Moderation)
    embed = discord.Embed(
        title="Moderation Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=PublicCategory.Moderation.value)
    embed.set_footer(text="\U00002193 React to return")
    embed.set_author(name="Server Index -> Moderation Commands",
                     icon_url=botAvatar)
    reactions = [Reaction.Return]
    return embed, reactions


async def Private(Prefix):
    description = await _CreateDescription(Prefix, RestrictedCategory.Private)
    embed = discord.Embed(
        title="Private Commands",
        description=
        f"**For more info on each commands do** `{Prefix}phelp [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}",
        color=RestrictedCategory.Private.value
    )
    embed.set_footer(text="This message will self destruct in 1 minute", icon_url=botAvatar)
    return embed


async def _CreateDescription(Prefix: str, Category: CommandCategory) -> str:
    desc = ''
    cmds: List[HelpMenuEntry] = HelpMenuEntry.GetCategory(Category, AsList=True)
    for cmd in cmds:
        desc += f"`{Prefix}{cmd.Name.lower()}` {cmd.Brief}\n"
    return desc