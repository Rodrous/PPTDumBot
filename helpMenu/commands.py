from enum import Enum
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from helpMenu.helpMenuEntry import HelpMenuEntry


class CommandCategory(Enum):
    Fun = 52382
    Game = 6724095
    Utility = 16375162
    Moderation = 13524060


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

    def GetCommand(self, Alias: str):
        Alias = Alias.lower()
        commands = self.GetAll()
        for cmd in commands:
            if Alias not in cmd:
                continue
            return cmd

    def GetAll(self) -> list:
        allCommands = []
        for category in CommandCategory:
            commands = self.GetCategory(category, AsList=True)
            allCommands.extend(commands)
        return allCommands
