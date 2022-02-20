import asyncio

from helpMenu.commands import CommandFlags
from helpMenu.commands import PublicCategory
from helpMenu.helpMenuEntry import EntryFactory


async def Init():
    """
    Entry For Commands
    HelpMenuEntry:
        :Param Name: Name of the command
        :Param Brief: A brief desc about the command
        :Param Desc: A detailed description of the command
        :Param Aliases: Optional list of aliases
        :Param Syntax: Optional Syntax details, will only need the flags at the end example [User: Id, Name] [Number] [Message -> Optional]
    """
    entry = EntryFactory(PublicCategory.Fun)
    await asyncio.gather(
        entry.Create(
            name="Ree",
            brief="Ree's out of frustration",
            desc="A command that will send *REEEE* with a random amount of E's",
            aliases=['re', 'reee', 'reeee']
        ),
        entry.Create(
            name="Yeye",
            brief="Issi asked for it so yeah, it does the same as ree but yeye",
            desc="Sends *YEEYEE* with random amount of E's as REE",
            aliases=["yeeyee", "yeyee", "yeeye"]
        ),
        entry.Create(
            name="Wallpaper",
            brief="Sends a Random image from internet [1920x1080]",
            desc="Will send a random HD image that can be used as a wallpaper"
        ),
        entry.Create(
            name="Cat",
            brief="Get Cat Pic",
            desc="Sends a random cat pic from the internet"
        ),
        entry.Create(
            name="Dog",
            brief="Get Dog Pic",
            desc="Sends a random dog pic from the internet"
        ),
        entry.Create(
            name="Quote",
            brief="Sends anime quote",
            desc="Sends a random anime quote from the internet"
        ),
        entry.Create(
            name="Say",
            brief="Will repeat after you",
            desc="Repeats anything you say",
            aliases=["speak"],
            syntax="[Message]"
        ),
        entry.Create(
            name="Joke",
            brief="Tells a joke",
            desc="Sends a random joke",
            flags=[
                CommandFlags("any", "will remove everything from blacklist"),
                CommandFlags("nsfw", "will remove {name} from blacklist"),
                CommandFlags("religious", "will remove {name} from blacklist"),
                CommandFlags("political", "will remove {name} from blacklist"),
                CommandFlags("racist", "will remove {name} from blacklist"),
                CommandFlags("sexist", "will remove {name} from blacklist"),
                CommandFlags("explicit", "will remove {name} from blacklist"),
                CommandFlags("misc", "category specific will include {name}"),
                CommandFlags("programming", "category specific will include {name}"),
                CommandFlags("dark", "category specific will include {name}"),
                CommandFlags("pun", "category specific will include {name}"),
                CommandFlags("spooky", "category specific will include {name}"),
                CommandFlags("christmas", "category specific will include {name}")
            ],
            aliases=["getjoke", "jk"],
            syntax="[Flags]"
        ),
        entry.Create(
            name="DadJoke",
            brief="Gives you a random dadjoke",
            desc="Will get a random dadjoke, enjoy :)"
        ),
        entry.Create(
            name="YoMomma",
            brief="Yomomma so dumb she didnt realize this will output random mom jokes",
            desc="Will send out random Yomomma jokes"
        ),
        entry.Create(
            name="Wikipedia",
            brief="Searches for a wikipedia query",
            desc="Will search up a wikipedia page for what you entered",
            aliases=["wiki"],
            syntax="[Search]"
        ),
        entry.Create(
            name="UrbanDict",
            brief="Searches definition for a word",
            desc="Will search [UrbanDictionary](https://www.urbandictionary.com/) for a word",
            aliases=["dict", 'urban', 'define'],
            syntax="[Word/Phrase]"
        ),
        entry.Create(
            name="MovieQuotes",
            brief="Sends a random moviequote",
            desc="Will search our database for a random moviequote",
            aliases=['mq', 'moviequote'],
            syntax="[Explicit][Nsfw]"
        )
    )
