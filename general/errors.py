import discord
from discord.ext import commands


class Errors(Exception):
    """
    Base Exception class for this bot
    """
    __default_message__ = "An error has occurred"

    def __init__(self,
                 module: str = None,
                 func: str = None,
                 ctx: commands.Context = None,
                 discord_message: discord.Message = None,
                 details: str = None
                 ):
        self._module = module
        self._func = func
        self.ctx = ctx
        self.discord_message = discord_message if not ctx else ctx.message
        self._UpdateFullPath()
        if details:
            self.details = details
            super().__init__(f"{self.__default_message__}: {details}")
            return
        self.details = self.__default_message__
        super().__init__(self.__default_message__)

    @property
    def full_path(self):
        return self._full_path

    @property
    def module(self):
        return self._module

    @module.setter
    def module(self, value: str):
        self._module = value
        self._UpdateFullPath()

    @property
    def func(self):
        return self._func

    @func.setter
    def func(self, value: str):
        self._func = value
        self._UpdateFullPath()

    def _UpdateFullPath(self):
        self._full_path = f"{self.module}.{self.func}" if self.module and self.func else None


class ApiError(Errors):
    __default_message__ = "An error has occurred with the Api"
