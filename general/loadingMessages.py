import discord
from discord.ext import commands

from general.backEnd import getRandomLoadingMessage

__all__ = [
    "loadingFunnyMessages",
    "sendLoadingMessage"
]


async def loadingFunnyMessages(StartMsg: str = "Please wait,") -> str:
    loading_message_end = await getRandomLoadingMessage()
    return f"{StartMsg} {loading_message_end}..."


async def sendLoadingMessage(ctx: commands.Context,
                             StartMsg: str = "Please wait,", *,
                             embed: bool = False, embed_color: int = None):
    loading = await loadingFunnyMessages(StartMsg)
    if not embed:
        return await ctx.send(content=loading)
    embed = discord.Embed(description=loading)
    if embed_color:
        embed.colour = embed_color
    return await ctx.send(embed=embed)
