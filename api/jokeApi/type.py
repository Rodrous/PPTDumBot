from enum import Enum, auto

from general.errors import ApiError


class Type(Enum):
    Single = auto()
    TwoPart = auto()

    @classmethod
    def FromString(cls, string: str):
        match string.lower():
            case "single":
                return cls["Single"]
            case "twopart":
                return cls["TwoPart"]
            case _:
                raise ApiError("Incorrect Joke Types")
