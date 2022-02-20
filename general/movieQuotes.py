from dataclasses import dataclass

from config import FLAG_PREFIX
from general.backEnd import getRandomQuote


@dataclass
class MovieQuotes:
    explicit: bool
    nsfw: bool
    quote: str = ""
    movie_name: str = ""
    character: str = ""
    image_url: str = ""
    type: str = ""

    async def GetMovieQuote(self) -> None:
        mq = await getRandomQuote()
        for quote in mq["quote"]:
            is_explicit: bool = quote[1]["Explicit"]
            is_nsfw: bool = quote[1]["NSFW"]
            if not self.explicit == is_explicit or not self.nsfw == is_nsfw:
                await self.GetMovieQuote()
                return
            self.quote = quote[0]
            self.movie_name = mq["movie"]
            self.character = mq["character"]
            self.image_url = mq["imageUrl"]
            self.type = mq["type"]


@dataclass
class ArgsHandler:
    args: str

    async def HasExplicit(self, *, explicit_flag: str = f"{FLAG_PREFIX}explicit"):
        return explicit_flag in self.args

    async def HasNsfw(self, *, nsfw_flag: str = f"{FLAG_PREFIX}nsfw"):
        return nsfw_flag in self.args
