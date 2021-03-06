from dataclasses import dataclass, field
from enum import Enum, unique
from typing import ClassVar, Optional, TYPE_CHECKING

from config import FLAG_PREFIX
from general import colors

if TYPE_CHECKING:
    from helpMenu.helpMenuEntry import HelpMenuEntry


class CommandCategory(Enum):
    ...


@unique
class PublicCategory(CommandCategory):
    Fun = colors.Category.FUN_GREEN
    Game = colors.Category.GAME_BLUE
    Utility = colors.Category.UTILITY_YELLOW
    Moderation = colors.Category.MODERATION_RED


@unique
class RestrictedCategory(CommandCategory):
    Private = colors.Category.PRIVATE_TEAL
    DevOnly = colors.Category.DEV_PINK


@dataclass(frozen=True, slots=True)
class CommandTracker:
    commands: dict = field(default_factory=dict)

    def Add(self, command: 'HelpMenuEntry'):
        if not self.commands.get(command.category, None):
            self.commands[command.category] = {}
        self.commands[command.category][command.name.lower()] = command

    def GetCategory(self, category: CommandCategory, *, AsList: bool = False):
        if not self.commands.get(category, None):
            return {}
        if not AsList:
            return self.commands[category]
        return list(self.commands[category].values())

    def PublicSearch(self, alias: str):
        alias = alias.lower()
        commands = self.PublicGetAll()
        return self._Search(alias, commands)

    def PrivateSearch(self, alias: str, Category: RestrictedCategory):
        alias = alias.lower()
        commands = self.GetCategory(Category, AsList=True)
        return self._Search(alias, commands)

    def PublicGetAll(self) -> list:
        return self._GetAll(PublicCategory)

    def PrivateGetAll(self) -> list:
        return self._GetAll(RestrictedCategory)

    @staticmethod
    def _Search(alias: str, commands: list):
        for cmd in commands:
            if alias not in cmd:
                continue
            return cmd

    def _GetAll(self, categories: CommandCategory) -> list:
        all_commands = []
        for category in categories:
            commands = self.GetCategory(category, AsList=True)
            all_commands.extend(commands)
        return all_commands


@dataclass(frozen=True, slots=True)
class CommandFlags:
    """  Stores a command flag, you can use {name} in your string to format your description  """
    name: str
    desc: str
    syntax: Optional[str] = ""
    _flag_prefix: ClassVar[str] = FLAG_PREFIX

    def __str__(self):
        desc = self.desc.format(name=self.name)
        return f"`{self._flag_prefix}{self.name}{self.syntax}` {desc}"
