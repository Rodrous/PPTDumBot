import asyncio
from helpMenu.entry import *


async def InitializeCommands():
    await asyncio.gather(
        fun.Init(),
        games.Init(),
        moderation.Init(),
        utility.Init()
    )
