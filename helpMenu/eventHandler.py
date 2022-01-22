from dataclasses import dataclass, field
from typing import ClassVar, Union

import discord

from general.returnCodes import ReturnCode
from helpMenu.reactions import Reaction


@dataclass(slots=True)
class EventHandler:
    message: discord.Message
    message_id: int = field(init=False)
    _reaction: Reaction = field(init=False)
    _loop: bool = field(init=False)
    _events: ClassVar[dict] = field(init=False, default={})

    def __post_init__(self):
        self.message_id = self.message.id
        self._reaction = None
        self._loop = False
        self._events[self.message_id] = self

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        if not isinstance(value, bool):
            return
        match value:
            case True:
                self._loop = value
            case False:
                del self._events[self.message_id]

    @property
    def reaction(self):
        return self._reaction

    async def SetReaction(self, reaction: Union[discord.Emoji, Reaction, str]) -> ReturnCode:
        if self._reaction:
            return ReturnCode.Unchanged
        try:
            match reaction:
                case discord.Emoji():
                    reaction = await Reaction.FromEmoji(reaction)
                case str():
                    reaction = Reaction(reaction)
        except ValueError:
            return ReturnCode.Unchanged
        self._reaction = reaction
        return ReturnCode.Success

    def __enter__(self):
        self.loop = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.loop = False

    @classmethod
    def GetEvent(cls, message: discord.Message) -> 'EventHandler':
        event = cls._events.get(message.id, None)
        if event:
            return event
        return cls(message)
