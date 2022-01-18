from enum import Enum

import discord


class Reaction(Enum):
    Fun = "<:PepeLmao:865712134439436328>"
    Games = "<:PepoGamer:865712213141356565>"
    Moderation = "<a:pepeban:865714938667991091>"
    Utility = "<a:pepeAnimeCaught:865712704315850782>"
    Return = "<:return:867101369814745099>"

    @classmethod
    async def FromEmoji(cls, Emoji: discord.Emoji):
        return cls(str(Emoji))
