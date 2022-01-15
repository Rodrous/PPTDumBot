import re as reg
import discord
import asyncio

from helpMenu import menus
from helpMenu.reactions import Reaction
from helpMenu.eventHandler import ReactionEvent
from helpMenu.initialize import InitializeCommands


startupLoop = {}


async def React(ctx: discord.Message, Emote: discord.Reaction, User: discord.User, Prefix: str):
    emote = Reaction(str(Emote.emoji))
    event = await EventFactory(ctx, emote, User, Prefix)
    if event.Loop or startupLoop.get(ctx.id, None):
        await asyncio.sleep(2)
        await React(ctx, Emote, User, Prefix)
        return
    if not ctx.embeds:
        return
    embed = ctx.embeds[0]
    embedAuthorField = embed.author.name
    if not ValidateHelpMenuEmbed(ctx, User, embedAuthorField):
        return
    await InitializeCommands()
    embed, reaction = await EmbedFactory(emote, Prefix)
    if not embed or not reaction:
        return
    event.Loop = True
    await ctx.clear_reactions()
    await ctx.edit(embed=embed)
    for react in reaction:
        await event.ctx.add_reaction(react)
    event.Loop = False


async def EmbedFactory(Emote: Reaction, Prefix: str):
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


async def EventFactory(ctx, Emote, User, Prefix):
    event = ReactionEvent.GetEvent(ctx.id)
    newEvent = ReactionEvent(ctx, Emote, User, Prefix)
    if not event:
        return newEvent
    if event != newEvent:
        event = newEvent
    return event


def ValidateHelpMenuEmbed(ctx: discord.Message, User: discord.User, AuthorField: str) -> bool:
    if User.bot:
        return False
    if not ctx.author.id == 852977382016024646:
        return False
    if not reg.search(pattern=r'\AServer Index', string=AuthorField):
        return False
    return True
