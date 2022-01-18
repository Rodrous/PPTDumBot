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
    entry.Create(
        Name="Feedback",
        Brief="Sends us Feedback",
        Desc="Will send us Feedback, please do not abuse this or it will result in a ban from the command",
        Aliases=["fb"],
        Syntax="[Message]"
    )
    entry.Create(
        Name="BugReport",
        Brief="Sends us a BugReport",
        Desc="Will send us a BugReport, please do not abuse this or it will result in a ban from the command",
        Aliases=["bugs", "bugrep", "bug-report", "bug-rep"],
        Syntax="[Message]"
    )
    entry.Create(
        Name="Steal",
        Brief="Steals an emote",
        Desc="Will steal an emote from another server via the emote itself or via link",
        Syntax="[Emote/Link] [Name->Optional]"
    )
    entry.Create(
        Name="Ping",
        Brief="Pong! Checks ping",
        Desc="Will check the current ping of the bot"
    )