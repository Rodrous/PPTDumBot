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
    entry = EntryFactory(RestrictedCategory.DevOnly)
    """  NOT INITIATED YET!!  """
