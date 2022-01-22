from dataclasses import dataclass
from general.backEnd import getRandomLoadingMessage,getRandomQuote

async def loadingFunnyMessages(StartMsg: str = "Please wait,") -> str:
    loading_message_end = await getRandomLoadingMessage()
    return f"{StartMsg} {loading_message_end}..."

@dataclass
class MovieQuotes:
    explicit:bool
    nsfw:bool
    shouldRecurse:bool = False
    quote: str = "Nil"
    movieName:str = "Nil"
    character:str = "Nil"
    imageUrl:str =  "https://media.tenor.co/videos/4eb9ebe6faabbd76cf1c5c6bfb56cfef/mp4"
    type:str = "Nil"

    async def get_movie_quote(self) -> None:
        mq = await getRandomQuote()
        target = mq["quote"]
        for i in target:
            is_explicit: bool = i[1]["Explicit"]
            is_nsfw: bool = i[1]["NSFW"]
            if self.explicit == is_explicit and self.nsfw == is_nsfw:
                self.quote = i[0]
                self.movieName = mq["movie"]
                self.character = mq["character"]
                self.imageUrl = mq["imageUrl"]
                self.type = mq["type"]
                self.shouldRecurse = False
            else:
                self.shouldRecurse = True

        if self.shouldRecurse:
            await self.get_movie_quote()