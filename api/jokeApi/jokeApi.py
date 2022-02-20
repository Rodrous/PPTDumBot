"""  API: https://v2.jokeapi.dev/  """
from dataclasses import dataclass
from typing import Optional

from api.jokeApi.category import Category
from api.jokeApi.flags import FlagBlacklist
from api.jokeApi.type import Type
from general.errors import ApiError


@dataclass(frozen=True, slots=True)
class Config:
    flags: FlagBlacklist
    categories: Optional[list[Category]] = None
    type: Optional[Type] = None
    safe_mode: bool = False


@dataclass(frozen=True, slots=True)
class JokeApi:
    """
    Must contain either joke or setup and delivery
    """
    category: Category
    type: Type
    flags: FlagBlacklist
    id: int
    safe: bool
    language: str
    joke: str = None
    setup: str = None
    delivery: str = None

    def __post_init__(self):
        if not self.joke and not self.setup and not self.delivery:
            raise TypeError("Must contain joke or delivery and setup")
        if self.setup and not self.delivery:
            raise TypeError("Contains setup but no delivery")
        if not self.setup and self.delivery:
            raise TypeError("Contains delivery but not setup")

    async def BuildJoke(self, separator: Optional[str] = "\n") -> str:
        match self.type:
            case Type.Single:
                return self.joke
            case Type.TwoPart:
                return f"{self.setup}{separator}{self.delivery}"

    @classmethod
    async def FromJson(cls, dictionary: dict):
        if dictionary["error"]:
            raise ApiError(
                __name__, f"{__class__.__name__}.FromJson",
                details="There has been an error with the API server"
            )
        category = Category[dictionary["category"]]
        joke_type = Type.FromString(dictionary["type"])
        flags = FlagBlacklist(**dictionary["flags"])
        joke_id = dictionary["id"]
        safe = dictionary["safe"]
        language = dictionary["lang"]
        match joke_type:
            case Type.Single:
                return cls(category, joke_type, flags, joke_id, safe, language, joke=dictionary["joke"])
            case Type.TwoPart:
                return cls(category, joke_type, flags, joke_id, safe, language, setup=dictionary["setup"], delivery=dictionary["delivery"])
