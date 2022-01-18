import asyncio

from helpMenu.entry import *


async def PublicCommands():
    await asyncio.gather(
        fun.Init(),
        games.Init(),
        moderation.Init(),
        utility.Init()
    )


async def PrivateCommands():
    await asyncio.gather(
        private.Init()
    )
