from enum import Enum, auto

from config import FLAG_PREFIX


class Category(Enum):
    Misc = auto()
    Programming = auto()
    Dark = auto()
    Pun = auto()
    Spooky = auto()
    Christmas = auto()

    @classmethod
    async def FromArgs(cls, args: str, *,
                       misc_flag=f"{FLAG_PREFIX}misc",
                       programming_flag=f"{FLAG_PREFIX}programming",
                       dark_flag=f"{FLAG_PREFIX}dark",
                       pun_flag=f"{FLAG_PREFIX}pun",
                       spooky_flag=f"{FLAG_PREFIX}spooky",
                       christmas_flag=f"{FLAG_PREFIX}christmas") -> list['Category']:
        """  Creates a list of Categories based on arguments provided  """
        categories = []
        if misc_flag in args:
            categories.append(cls.Misc)
        if programming_flag in args:
            categories.append(cls.Programming)
        if dark_flag in args:
            categories.append(cls.Dark)
        if pun_flag in args:
            categories.append(cls.Pun)
        if spooky_flag in args:
            categories.append(cls.Spooky)
        if christmas_flag in args:
            categories.append(cls.Christmas)
        return categories
