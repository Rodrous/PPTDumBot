"""  API: https://v2.jokeapi.dev/  """
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

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


class Category(Enum):
    Misc = auto()
    Programming = auto()
    Dark = auto()
    Pun = auto()
    Spooky = auto()
    Christmas = auto()


@dataclass(frozen=True, slots=True)
class FlagBlacklist:
    nsfw: bool = False
    religious: bool = False
    political: bool = False
    racist: bool = False
    sexist: bool = False
    explicit: bool = False

    async def GetFlagData(self) -> list[tuple[str, bool]]:
        return [
            ("nsfw", self.nsfw),
            ("religious", self.religious),
            ("political", self.political),
            ("racist", self.racist),
            ("sexist", self.sexist),
            ("explicit", self.explicit)
        ]

    @classmethod
    async def All(cls):
        return cls(
            nsfw=True,
            religious=True,
            political=True,
            racist=True,
            sexist=True,
            explicit=True
        )

    @classmethod
    async def FromArgs(cls, args: str,
                       nsfw_flag: str = "-nsfw",
                       religious_flag: str = "-rel",
                       political_flag: str = "-pol",
                       racist_flag: str = "-rct",
                       sexist_flag: str = "-sexist"):


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
            raise ApiError("An error with the api has occurred")
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


async def BuildRequestUrl(config: Config) -> str:
    """
    Will build an url for the joke api to request
    :param config: the config to create the correct url specifications
    :return: string containing an api url
    """
    base_url = "https://v2.jokeapi.dev/joke/"
    if config.categories:
        categories = [category.name for category in config.categories]
    else:
        categories = ["Any"]
    url = f"{base_url}{','.join(categories)}"
    query = await _BuildQuery(config)
    return url + query


async def _BuildFlagBlacklist(flag_data: list[tuple[str, bool]]) -> str:
    extension = []
    for flag, boolean in flag_data:
        if not boolean:
            continue
        extension.append(flag)
    if not extension:
        return ""
    return f"blacklistFlags={','.join(extension)}"


async def _BuildQuery(config: Config) -> str:
    query = []
    flag_data = await config.flags.GetFlagData()
    flag_extension = await _BuildFlagBlacklist(flag_data)
    if config.safe_mode:
        query.append("safe-mode")
    elif flag_extension:
        query.append(flag_extension)
    if config.type:
        query.append(f"type={config.type.name.lower()}")
    if not query:
        return ""
    return f"?{'&'.join(query)}"

