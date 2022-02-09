from enum import Enum, auto


class Category(Enum):
    Misc = auto()
    Programming = auto()
    Dark = auto()
    Pun = auto()
    Spooky = auto()
    Christmas = auto()

    @classmethod
    async def FromArgs(cls, args: str, *,
                       misc_flag="-misc",
                       programming_flag="-programming",
                       dark_flag="-dark",
                       pun_flag="-pun",
                       spooky_flag="-spooky",
                       christmas_flag="-christmas") -> list['Category']:
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
