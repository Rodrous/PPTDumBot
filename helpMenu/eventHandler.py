from dataclasses import dataclass, field
from typing import ClassVar

import discord


@dataclass(slots=True)
class EventHandler:
    Message: discord.Message
    MessageID: int = field(init=False)
    _Loop: bool = field(init=False)
    _Events: ClassVar[dict] = field(init=False, default={})

    def __post_init__(self):
        self.MessageID = self.Message.id
        self._Events[self.MessageID] = self
        self._Loop = False

    @property
    def Loop(self):
        return self._Loop

    @Loop.setter
    def Loop(self, value: bool):
        if not isinstance(value, bool):
            return
        match value:
            case True:
                self._Loop = value
            case False:
                del self._Events[self.MessageID]

    @classmethod
    def GetEvent(cls, Message: discord.Message) -> 'EventHandler':
        event = cls._Events.get(Message.id, None)
        if event:
            return event
        return cls(Message)
