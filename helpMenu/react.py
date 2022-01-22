import asyncio
import re as reg
from typing import Union

import discord

from helpMenu import menus
from helpMenu.eventHandler import EventHandler
from helpMenu.reactions import Reaction


async def React(
        event: EventHandler,
        embed: discord.Embed,
        reactions: list[Reaction], *,
        recursion_max: int = 10, recursion_speed: float = 1, _recursion_depth: int = 0):
    """  Running Checks  """
    if _recursion_depth >= recursion_max:
        return
    if event.loop:
        await asyncio.sleep(recursion_speed)
        await React(
            event, embed, reactions,
            recursion_max=recursion_max, recursion_speed=recursion_speed, _recursion_depth=_recursion_depth + 1)
        return
    if not event.message.embeds:
        return
    bot_embed = event.message.embeds[0]
    author_field = bot_embed.author.name
    if not _ValidateHelpMenuEmbed(event.message, author_field):
        return
    await _Execute(event, embed, reactions)


async def _Execute(event: EventHandler, embed, reactions: list[Reaction]):
    """  Executing Event  """
    await asyncio.gather(
        event.message.clear_reactions(),
        event.message.edit(embed=embed)
    )
    await AddReactions(event.message, event, reactions)


async def MenuFactory(emote: Union[Reaction, discord.Emoji, str], prefix: str) -> (discord.Embed, list[Reaction]):
    """  Finds the correct Menu  """
    # Convert to correct type
    match emote:
        case discord.Emoji():
            emote = await Reaction.FromEmoji(emote)
        case str():
            emote = Reaction(emote)
    # Match Emote to Menu
    match emote:
        case Reaction.Fun:
            return await menus.Fun(prefix)
        case Reaction.Games:
            return await menus.Games(prefix)
        case Reaction.Utility:
            return await menus.Utility(prefix)
        case Reaction.Moderation:
            return await menus.Moderation(prefix)
        case Reaction.Return:
            return await menus.Intro(prefix)


async def AddReactions(message: discord.Message, event: EventHandler, reactions: list[Reaction]):
    with event:
        for reaction in reactions:
            await message.add_reaction(reaction.value)


def _ValidateHelpMenuEmbed(ctx: discord.Message, author_field: str) -> bool:
    if not ctx.author.id == 852977382016024646:
        return False
    if not reg.search(pattern=r'\AServer Index', string=author_field):
        return False
    return True
