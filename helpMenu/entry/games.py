from helpMenu.helpMenuEntry import EntryFactory
from helpMenu.commands import PublicCategory


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
    entry = EntryFactory(PublicCategory.Game)
    entry.Create(
        Name="Minesweeper",
        Brief="Generates Minesweeper game",
        Desc="Will randomly generate a Minesweeper game to play with spoiler tags",
        Aliases=['ms', 'mines'],
        Syntax="[Rows] [Columns] [Mines]"
    )
