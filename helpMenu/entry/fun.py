import asyncio

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
            Name="Ree",
            Brief="Ree's out of frustration",
            Desc="A command that will send *REEEE* with a random amount of E's",
            Aliases=['re', 'reee', 'reeee']
        ),
        entry.Create(
            Name="Yeye",
            Brief="Issi asked for it so yeah, it does the same as ree but yeye",
            Desc="Sends *YEEYEE* with random amount of E's as REE",
            Aliases=["yeeyee", "yeyee", "yeeye"]
        ),
        entry.Create(
            Name="Wallpaper",
            Brief="Sends a Random image from internet [1920x1080]",
            Desc="Will send a random HD image that can be used as a wallpaper"
        ),
        entry.Create(
            Name="Cat",
            Brief="Get Cat Pic",
            Desc="Sends a random cat pic from the internet"
        ),
        entry.Create(
            Name="Dog",
            Brief="Get Dog Pic",
            Desc="Sends a random dog pic from the internet"
        ),
        entry.Create(
            Name="Quote",
            Brief="Sends anime quote",
            Desc="Sends a random anime quote from the internet"
        ),
        entry.Create(
            Name="Say",
            Brief="Will repeat after you",
            Desc="Repeats anything you say",
            Aliases=["speak"],
            Syntax="[Message]"
        ),
        entry.Create(
            Name="Joke",
            Brief="Tells a joke",
            Desc="Sends a random joke\n\n**Flags:**\n`-ex` sends any jokes, even explicit and dark jokes",
            Aliases=["getjoke", "jk"],
            Syntax="[Flags]"
        ),
        entry.Create(
            Name="DadJoke",
            Brief="Gives you a random dadjoke",
            Desc="Will get a random dadjoke, enjoy :)"
        ),
        entry.Create(
            Name="YoMomma",
            Brief="Yomomma so dumb she didnt realize this will output random mom jokes",
            Desc="Will send out random Yomomma jokes"
        ),
        entry.Create(
            Name="Wikipedia",
            Brief="Searches for a wikipedia query",
            Desc="Will search up a wikipedia page for what you entered",
            Aliases=["wiki"],
            Syntax="[Search]"
        ),
        entry.Create(
            Name="UrbanDict",
            Brief="Searches definition for a word",
            Desc="Will search [UrbanDictionary](https://www.urbandictionary.com/) for a word",
            Aliases=["dict", 'urban', 'define'],
            Syntax="[Word/Phrase]"
        ),
        entry.Create(
            Name="MovieQuotes",
            Brief="Sends a random moviequote",
            Desc="Will search our database for a random moviequote",
            Aliases=['mq', 'moviequote'],
            Syntax="[Explicit][Nsfw]"
        )
    )
