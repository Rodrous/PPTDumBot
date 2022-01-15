from dataclasses import dataclass, field
from typing import Optional, ClassVar, Union

from helpMenu.commands import CommandTracker, CommandCategory


@dataclass(frozen=True, slots=True)
class HelpMenuEntry:
    Category: CommandCategory
    Name: str
    Brief: str
    Desc: str
    Aliases: Optional[list[str]] = field(default_factory=list)
    Syntax: Optional[str] = ''
    _Instances: ClassVar = CommandTracker()

    def __post_init__(self):
        # Formatting instance variables
        if self.Syntax:
            syntax = "{Prefix}" + f"{self.Name.lower()} {self.Syntax}"
            object.__setattr__(self, "Syntax", syntax)
        if self.Aliases:
            aliases = [alias.lower() for alias in self.Aliases]
            object.__setattr__(self, "Aliases", aliases)
        # Adding Object to _Instances
        self._Instances.Add(self)

    @classmethod
    def GetCategory(cls, Category: CommandCategory, AsList: bool = False) -> Union[dict, list]:
        return cls._Instances.GetCategory(Category, AsList)

    @classmethod
    def GetCommand(cls, Alias: str) -> 'HelpMenuEntry':
        return cls._Instances.GetCommand(Alias)

    @classmethod
    def GetAll(cls) -> list:
        return cls._Instances.GetAll()

    def __contains__(self, item):
        """
        Checking if item is in any alias of the object
        """
        name = self.Name.lower()
        allAliases = self.Aliases.copy()
        allAliases.append(name)
        return item in allAliases
