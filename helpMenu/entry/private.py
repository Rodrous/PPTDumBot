from helpMenu.helpMenuEntry import EntryFactory
from helpMenu.commands import RestrictedCategory


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
    entry.Create(
        Name="Ily",
        Brief="Sends ily cause Draf do be lazy",
        Desc="Sends ily + random int + ping"
    )
    entry.Create(
        Name="vc",
        Brief="Pings People to vc",
        Desc="Pings everyone whos on the list to vc, please let us know if you wanna be added or removed"
    )
