from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.commands import CommandCategory


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

    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="Clear",
        Brief="Will clear the chat",
        Desc="Removed specified amount of messages from current chat",
        Aliases=['purge'],
        Syntax="[Amount]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="Mute",
        Brief="Will mute a person from speaking, reacting etc",
        Desc="Gives person mute role for a specified amount of time so they cant speak or react",
        Syntax="[User: Name, Id] [Time]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="UnMute",
        Brief="Will unmute a person",
        Desc="Removes the muted role so they can speak again",
        Syntax="[User: Name, ID]"
    )