import asyncio

from helpMenu.commands import PublicCategory
from helpMenu.helpMenuEntry import EntryFactory


async def Init():
    """
    Entry For Commands
    HelpMenuEntry:
        :Param Name: Name of the command
        :Param Brief: A brief desc about the command
        :Param Desc: A detailed description of the command
        :Param Aliases: Optional list of aliases
        :Param Syntax: Optional Syntax details, will only need the flags at the end example [User: Id, Name] [Number] [Message -> Optional]
    """
    entry = EntryFactory(PublicCategory.Moderation)
    await asyncio.gather(
        entry.Create(
            Name="Clear",
            Brief="Will clear the chat",
            Desc="Removed specified amount of messages from current chat",
            Aliases=['purge'],
            Syntax="[Amount]"
        ),
        entry.Create(
            Name="Mute",
            Brief="Will mute a person from speaking, reacting etc",
            Desc="Gives person mute role for a specified amount of time so they cant speak or react",
            Syntax="[User: Name, Id] [Time]"
        ),
        entry.Create(
            Name="UnMute",
            Brief="Will unmute a person",
            Desc="Removes the muted role so they can speak again",
            Syntax="[User: Name, ID]"
        )
    )
