import asyncio

from helpMenu.commands import RestrictedCategory
from helpMenu.helpMenuEntry import EntryFactory


async def Init():
    """
    Entry For Commands
    HelpMenuEntry:
        :Param Category: Category of type CommandCategory
        :Param Name: Name of the command
        :Param Brief: A brief desc about the command
        :Param Desc: A detailed description of the command
        :Param Aliases: Optional list of aliases
        :Param Syntax: Optional Syntax details, will only need the flags at the end example [User: Id, Name] [Number] [Message -> Optional]
    """
    entry = EntryFactory(RestrictedCategory.Private)
    await asyncio.gather(
        entry.Create(
            name="Ily",
            brief="Sends ily cause Draf do be lazy",
            desc="Sends ily + random int + ping"
        ),
        entry.Create(
            name="vc",
            brief="Pings People to vc",
            desc="Pings everyone whos on the list to vc, please let us know if you wanna be added or removed"
        )
    )
