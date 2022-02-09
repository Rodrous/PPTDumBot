import asyncio

from api.jokeApi.category import Category
from api.jokeApi.jokeApi import Config

BASE_URL = "https://v2.jokeapi.dev/joke/"


async def BuildRequestUrl(config: Config) -> str:
    """
    Will build an url for the joke api to request
    :param config: the config to create the correct url specifications
    :return: string containing an api url
    """
    tasks = await asyncio.gather(
        _BuildCategories(config.categories),
        _BuildQuery(config)
    )
    categories = tasks[0]
    query = tasks[1]
    return f"{BASE_URL}{categories}{query}"


async def _BuildCategories(categories: list[Category]):
    if not categories:
        return "Any"
    categories = [category.name for category in categories]
    return ','.join(categories)


async def _BuildFlagBlacklist(flag_data: list[tuple[str, bool]], safe_mode: bool = False) -> str:
    if safe_mode:
        return "safe-mode"
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
    flag_extension = await _BuildFlagBlacklist(flag_data, safe_mode=config.safe_mode)
    if flag_extension:
        query.append(flag_extension)
    if config.type:
        query.append(f"type={config.type.name.lower()}")
    if not query:
        return ""
    return f"?{'&'.join(query)}"
