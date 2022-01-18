from dataclasses import dataclass, field
from enum import Enum, unique
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from helpMenu.helpMenuEntry import HelpMenuEntry


class CommandCategory(Enum):
    ...


@unique
class PublicCategory(CommandCategory):
    Fun = 52382
    Game = 6724095
    Utility = 16375162
    Moderation = 13524060


@unique
class RestrictedCategory(CommandCategory):
    Private = 1764824
    DevOnly = 13273297


@dataclass(frozen=True, slots=True)
class CommandTracker:
    Commands: dict = field(default_factory=dict)

    def Add(self, Command: 'HelpMenuEntry'):
        if not self.Commands.get(Command.Category, None):
            self.Commands[Command.Category] = {}
        self.Commands[Command.Category][Command.Name.lower()] = Command

    def GetCategory(self, Category: CommandCategory, AsList: bool = False):
        if not self.Commands.get(Category, None):
            return {}
        if not AsList:
            return self.Commands[Category]
        return list(self.Commands[Category].values())

    def PublicSearch(self, Alias: str):
        alias = Alias.lower()
        commands = self.PublicGetAll()
        return self._Search(alias, commands)

    def PrivateSearch(self, Alias: str, Category: RestrictedCategory):
        alias = Alias.lower()
        commands = self.GetCategory(Category, AsList=True)
        return self._Search(alias, commands)

    def PublicGetAll(self) -> list:
        return self._GetAll(PublicCategory)

    def PrivateGetAll(self) -> list:
        return self._GetAll(RestrictedCategory)

    @staticmethod
    def _Search(Alias: str,  Commands: list):
        for cmd in Commands:
            if Alias not in cmd:
                continue
            return cmd

    def _GetAll(self, Categories: CommandCategory) -> list:
        allCommands = []
        for category in Categories:
            commands = self.GetCategory(category, AsList=True)
            allCommands.extend(commands)
        return allCommands
