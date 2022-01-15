import discord
from dataclasses import dataclass, field, InitVar
from typing import ClassVar

from helpMenu.reactions import Reaction


@dataclass(slots=True)
class ReactionEvent:
    ctx: discord.Message
    Reaction: Reaction
    User: discord.User
    Prefix: str
    MessageID: int = field(init=False)
    _Loop: bool = field(init=False)
    _Events: ClassVar[dict] = field(init=False, default={})

    def __post_init__(self):
        self.MessageID = self.ctx.id
        self._Events[self.MessageID] = self
        self._Loop = False

    @property
    def Loop(self):
        return self._Loop

    @Loop.setter
    def Loop(self, value: bool):
        if not isinstance(value, bool):
            return
        self._Loop = value

    @classmethod
    def GetEvent(cls, MessageID) -> 'ReactionEvent':
        return cls._Events.get(MessageID, None)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.Reaction == other.Reaction and self.User == other.User
