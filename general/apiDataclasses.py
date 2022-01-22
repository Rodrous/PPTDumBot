from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .errors import ApiError


class JokeApiType(Enum):
    Single = "single"
    TwoPart = "twopart"


@dataclass(frozen=True, slots=True)
class JokeApiFlags:
    nsfw: bool
    religious: bool
    political: bool
    racist: bool
    sexist: bool
    explicit: bool


@dataclass(frozen=True, slots=True)
class JokeApi:
    """
    API: https://v2.jokeapi.dev/
    Must contain either joke or setup and delivery
    """
    category: str
    type: JokeApiType
    flags: JokeApiFlags
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
            case JokeApiType.Single:
                return self.joke
            case JokeApiType.TwoPart:
                return f"{self.setup}{separator}{self.delivery}"

    @classmethod
    async def FromJson(cls, dictionary: dict):
        if dictionary["error"]:
            raise ApiError("An error with the api has occurred")
        category = dictionary["category"]
        joke_type = JokeApiType(dictionary["type"])
        flags = JokeApiFlags(**dictionary["flags"])
        joke_id = dictionary["id"]
        safe = dictionary["safe"]
        language = dictionary["lang"]
        match joke_type:
            case JokeApiType.Single:
                return cls(category, joke_type, flags, joke_id, safe, language, joke=dictionary["joke"])
            case JokeApiType.TwoPart:
                return cls(category, joke_type, flags, joke_id, safe, language, setup=dictionary["setup"], delivery=dictionary["delivery"])
            case _:
                raise ApiError("Incorrect Joke Types")
