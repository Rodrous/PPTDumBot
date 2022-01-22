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
    entry = EntryFactory(PublicCategory.Utility)
    await asyncio.gather(
        entry.Create(
            name="Feedback",
            brief="Sends us Feedback",
            desc="Will send us Feedback, please do not abuse this or it will result in a ban from the command",
            aliases=["fb"],
            syntax="[Message]"
        ),
        entry.Create(
            name="BugReport",
            brief="Sends us a BugReport",
            desc="Will send us a BugReport, please do not abuse this or it will result in a ban from the command",
            aliases=["bugs", "bugrep", "bug-report", "bug-rep"],
            syntax="[Message]"
        ),
        entry.Create(
            name="Steal",
            brief="Steals an emote",
            desc="Will steal an emote from another server via the emote itself or via link",
            syntax="[Emote/Link] [Name->Optional]"
        ),
        entry.Create(
            name="Ping",
            brief="Pong! Checks ping",
            desc="Will check the current ping of the bot"
        )
    )
