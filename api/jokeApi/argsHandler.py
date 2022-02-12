from dataclasses import dataclass

from api.jokeApi.category import Category
from api.jokeApi.flags import FlagBlacklist


@dataclass(slots=True)
class ArgsHandler:
    args: str

    async def GetCategories(self, **kwargs) -> list[Category]:
        if not self.args:
            return
        return await Category.FromArgs(self.args, **kwargs)

    async def GetFlags(self, *, inverse: bool = False, **kwargs):
        return await FlagBlacklist.FromArgs(self.args, inverse=inverse, **kwargs)

    async def SafeMode(self):
        if not self.args:
            return True
        return False
