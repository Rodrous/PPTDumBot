import asyncio
import re as reg
from typing import Union

import discord

from helpMenu import menus, initialize
from helpMenu.eventHandler import EventHandler
from helpMenu.reactions import Reaction


async def React(
        Event: EventHandler,
        Embed: discord.Embed,
        Reactions: list[Reaction], *,
        RecursionMax: int = 5, RecursionSpeed: float = 1, _RecursionDepth: int = 0):
    """  Running Checks  """
    if _RecursionDepth >= RecursionMax:
        return
    if Event.Loop:
        await asyncio.sleep(RecursionSpeed)
        await React(
            Event, Embed, Reactions,
            RecursionMax=RecursionMax, RecursionSpeed=RecursionSpeed, _RecursionDepth=_RecursionDepth + 1)
        return
    if not Event.Message.embeds:
        return
    botEmbed = Event.Message.embeds[0]
    authorField = botEmbed.author.name
    if not _ValidateHelpMenuEmbed(Event.Message, authorField):
        return
    await _Execute(Event, Embed, Reactions)


async def _Execute(Event: EventHandler, Embed, Reactions: list[Reaction]):
    """  Executing Event  """
    await initialize.PublicCommands()
    Event.Loop = True
    await asyncio.gather(
        Event.Message.clear_reactions(),
        Event.Message.edit(embed=Embed)
    )
    for react in Reactions:
        await Event.Message.add_reaction(react.value)
    Event.Loop = False


async def MenuFactory(Emote: Union[Reaction, discord.Emoji, str], Prefix: str):
    """  Finds the correct Menu  """
    # Convert to correct type
    match Emote:
        case discord.Emoji():
            Emote = await Reaction.FromEmoji(Emote)
        case str():
            Emote = Reaction(Emote)
    # Match Emote to Menu
    match Emote:
        case Reaction.Fun:
            return await menus.Fun(Prefix)
        case Reaction.Games:
            return await menus.Games(Prefix)
        case Reaction.Utility:
            return await menus.Utility(Prefix)
        case Reaction.Moderation:
            return await menus.Moderation(Prefix)
        case Reaction.Return:
            return await menus.Intro(Prefix)
        case _:
            return None, None


def _ValidateHelpMenuEmbed(ctx: discord.Message, AuthorField: str) -> bool:
    if not ctx.author.id == 852977382016024646:
        return False
    if not reg.search(pattern=r'\AServer Index', string=AuthorField):
        return False
    return True
