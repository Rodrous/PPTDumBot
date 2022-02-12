"""  API: https://animechan.vercel.app/  """
from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class AnimeQuote:
    anime: str
    character: str
    quote: str
