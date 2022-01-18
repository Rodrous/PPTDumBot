from dataclasses import dataclass, field
from typing import Optional, ClassVar, Union

from helpMenu.commands import CommandTracker, CommandCategory, RestrictedCategory


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
    async def GetCategory(cls, Category: CommandCategory, AsList: bool = False) -> Union[dict, list]:
        return cls._Instances.GetCategory(Category, AsList)

    @classmethod
    async def PublicSearch(cls, Alias: str) -> 'HelpMenuEntry':
        return cls._Instances.PublicSearch(Alias)

    @classmethod
    async def PrivateSearch(cls, Alias: str, Category: RestrictedCategory) -> 'HelpMenuEntry':
        return cls._Instances.PrivateSearch(Alias, Category)

    def BuildDesc(self) -> str:
        string = f"**Category:** {self.Category.name}\n" \
                 f"**Brief:** {self.Brief}"
        if self.Aliases:
            string += f"\n**Aliases:** {', '.join(self.Aliases)}"
        if self.Syntax:
            string += f"\n**Syntax:** `{self.Syntax}`"
        string += f"\n\n{self.Desc}"
        return string

    def __contains__(self, item):
        """
        Checking if item is in any alias of the object
        """
        name = self.Name.lower()
        allAliases = self.Aliases.copy()
        allAliases.append(name)
        return item in allAliases


@dataclass(frozen=True, slots=True)
class EntryFactory:
    Category: CommandCategory

    def Create(self,
               Name: str,
               Brief: str,
               Desc: str,
               Aliases: Optional[list[str]] = [],
               Syntax: Optional[str] = ''):
        HelpMenuEntry(self.Category, Name, Brief, Desc, Aliases, Syntax)
