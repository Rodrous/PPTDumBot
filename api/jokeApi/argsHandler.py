from dataclasses import dataclass

from api.jokeApi.category import Category
from api.jokeApi.flags import FlagBlacklist


@dataclass(slots=True)
class ArgsHandler:
    args: str

    async def GetCategories(self) -> list[Category]:
        if not self.args:
            return
        print(await Category.FromArgs(self.args))
        return await Category.FromArgs(self.args)

    async def GetFlags(self, inverse: bool = False):
        return await FlagBlacklist.FromArgs(self.args, inverse=inverse)
