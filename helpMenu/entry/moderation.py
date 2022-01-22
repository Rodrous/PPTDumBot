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
            name="Clear",
            brief="Will clear the chat",
            desc="Removed specified amount of messages from current chat",
            aliases=['purge'],
            syntax="[Amount]"
        ),
        entry.Create(
            name="Mute",
            brief="Will mute a person from speaking, reacting etc",
            desc="Gives person mute role for a specified amount of time so they cant speak or react",
            syntax="[User: Name, Id] [Time]"
        ),
        entry.Create(
            name="UnMute",
            brief="Will unmute a person",
            desc="Removes the muted role so they can speak again",
            syntax="[User: Name, ID]"
        )
    )
