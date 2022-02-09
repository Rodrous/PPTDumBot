from dataclasses import dataclass, field
from typing import Optional, ClassVar, Union

from helpMenu.commands import CommandTracker, CommandCategory, RestrictedCategory, CommandFlags


@dataclass(frozen=True, slots=True)
class HelpMenuEntry:
    category: CommandCategory
    name: str
    brief: str
    desc: str
    flags: Optional[list[CommandFlags]] = field(default_factory=list)
    aliases: Optional[list[str]] = field(default_factory=list)
    syntax: Optional[str] = ''
    _instances: ClassVar = CommandTracker()

    def __post_init__(self):
        # Formatting instance variables
        if self.syntax:
            syntax = "{prefix}" + f"{self.name.lower()} {self.syntax}"
            object.__setattr__(self, "syntax", syntax)
        if self.aliases:
            aliases = [alias.lower() for alias in self.aliases]
            object.__setattr__(self, "aliases", aliases)
        # Adding Object to _Instances
        self._instances.Add(self)

    @classmethod
    async def GetCategory(cls, category: CommandCategory, *, AsList: bool = False) -> Union[dict, list]:
        return cls._instances.GetCategory(category, AsList=AsList)

    @classmethod
    async def PublicSearch(cls, alias: str) -> 'HelpMenuEntry':
        return cls._instances.PublicSearch(alias)

    @classmethod
    async def PrivateSearch(cls, alias: str, category: RestrictedCategory) -> 'HelpMenuEntry':
        return cls._instances.PrivateSearch(alias, category)

    def BuildDesc(self) -> str:
        string = f"**Category:** {self.category.name}\n" \
                 f"**Brief:** {self.brief}"
        if self.aliases:
            string += f"\n**Aliases:** {', '.join(self.aliases)}"
        if self.syntax:
            string += f"\n**Syntax:** `{self.syntax}`"
        string += f"\n\n{self.desc}"
        return string

    def __contains__(self, item):
        """
        Checking if item is in any alias of the object
        """
        name = self.name.lower()
        allAliases = self.aliases.copy()
        allAliases.append(name)
        return item in allAliases


@dataclass(frozen=True, slots=True)
class EntryFactory:
    category: CommandCategory

    async def Create(self,
                     name: str,
                     brief: str,
                     desc: str,
                     flags: Optional[list[CommandFlags]] = None,
                     aliases: Optional[list[str]] = None,
                     syntax: Optional[str] = ''):
        if not flags:
            flags = []
        if not aliases:
            aliases = []
        HelpMenuEntry(self.category, name, brief, desc, flags, aliases, syntax)
