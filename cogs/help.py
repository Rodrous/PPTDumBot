from discord.ext import commands
import discord
import re as reg
from typing import List
from build.generalPurpose import dumbot
from helpMenu.helpMenuEntry import HelpMenuEntry
from helpMenu.commands import CommandCategory

bot_avatar = dumbot.avatar()


async def CreateCommands():
    """
    Entry For Commands
    HelpMenuEntry:
        :Param Category: Category of type CommandCategory
        :Param Name: Name of the command
        :Param Brief: A brief desc about the command
        :Param Desc: A detailed description of the command
        :Param Aliases: Optional list of aliases
        :Param Syntax: Optional Syntax details, will only need the flags at the end example [User: Id, Name] [Number] [Message -> Optional]
    """

    """  FUN COMMANDS  """
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Ree",
        Brief="Ree's out of frustration",
        Desc="A command that will send *REEEE* with a random amount of E's",
        Aliases=['re', 'reee', 'reeee']
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Yeye",
        Brief="Issi asked for it so yeah, it does the same as ree but yeye",
        Desc="Sends *YEEYEE* with random amount of E's as REE",
        Aliases=["yeeyee", "yeyee", "yeeye"]
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Wallpaper",
        Brief="Sends a Random image from internet [1920x1080]",
        Desc="Will send a random HD image that can be used as a wallpaper"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Cat",
        Brief="Get Cat Pic",
        Desc="Sends a random cat pic from the internet"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Dog",
        Brief="Get Dog Pic",
        Desc="Sends a random dog pic from the internet"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Quote",
        Brief="Sends anime quote",
        Desc="Sends a random anime quote from the internet"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Say",
        Brief="Will repeat after you",
        Desc="Repeats anything you say",
        Aliases=["speak"],
        Syntax="[Message]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Joke",
        Brief="Tells a joke",
        Desc="Sends a random joke\n\n**Flags:**\n`-ex` sends any jokes, even explicit and dark jokes",
        Aliases=["getjoke", "jk"],
        Syntax="[Flags]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="DadJoke",
        Brief="Gives you a random dadjoke",
        Desc="Will get a random dadjoke, enjoy :)"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="YoMomma",
        Brief="Yomomma so dumb she didnt realize this will output random mom jokes",
        Desc="Will send out random Yomomma jokes"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="Wikipedia",
        Brief="Searches for a wikipedia query",
        Desc="Will search up a wikipedia page for what you entered",
        Aliases=["wiki"],
        Syntax="[Search]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="UrbanDict",
        Brief="Searches definition for a word",
        Desc="Will search [UrbanDictionary](https://www.urbandictionary.com/) for a word",
        Aliases=["dict", 'urban', 'define'],
        Syntax="[Word/Phrase]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Fun,
        Name="MovieQuotes",
        Brief="Sends a random moviequote",
        Desc="Will search our database for a random moviequote",
        Aliases=['mq', 'moviequote'],
        Syntax="[Explicit][Nsfw]"
    )

    """  Game Commands  """
    HelpMenuEntry(
        Category=CommandCategory.Game,
        Name="Minesweeper",
        Brief="Generates Minesweeper game",
        Desc="Will randomly generate a Minesweeper game to play with spoiler tags",
        Aliases=['ms','mines'],
        Syntax="[Rows] [Columns] [Mines]"
    )

    """  Utility Commands  """
    HelpMenuEntry(
        Category=CommandCategory.Utility,
        Name="Feedback",
        Brief="Sends us Feedback",
        Desc="Will send us Feedback, please do not abuse this or it will result in a ban from the command",
        Aliases=["fb"],
        Syntax="[Message]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Utility,
        Name="BugReport",
        Brief="Sends us a BugReport",
        Desc="Will send us a BugReport, please do not abuse this or it will result in a ban from the command",
        Aliases=["bugs", "bugrep", "bug-report", "bug-rep"],
        Syntax="[Message]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Utility,
        Name="Steal",
        Brief="Steals an emote",
        Desc="Will steal an emote from another server via the emote itself or via link",
        Syntax="[Emote/Link] [Name->Optional]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Utility,
        Name="Ping",
        Brief="Pong! Checks ping",
        Desc="Will check the current ping of the bot"
    )

    """  Moderation Commands  """
    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="Clear",
        Brief="Will clear the chat",
        Desc="Removed specified amount of messages from current chat",
        Aliases=['purge'],
        Syntax="[Amount]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="Mute",
        Brief="Will mute a person from speaking, reacting etc",
        Desc="Gives person mute role for a specified amount of time so they cant speak or react",
        Syntax="[User: Name, Id] [Time]"
    )
    HelpMenuEntry(
        Category=CommandCategory.Moderation,
        Name="UnMute",
        Brief="Will unmute a person",
        Desc="Removes the muted role so they can speak again",
        Syntax="[User: Name, ID]"
    )


async def CreateDescription(Prefix: str, Category: CommandCategory) -> str:
    desc = ''
    commands: List[HelpMenuEntry] = HelpMenuEntry.GetCategory(Category, AsList=True)
    for cmd in commands:
        desc += f"`{Prefix}{cmd.Name.lower()}` {cmd.Brief}\n"
    return desc


async def introMenu(prefix):
    embed = discord.Embed(
        title="Help Menu",
        description=
        f"**Server Prefix:** `{prefix}`"
        "\n\n**React with:**"
        "\n<:PepeLmao:865712134439436328> For Fun"
        "\n<:PepoGamer:865712213141356565> For Games"
        "\n<a:pepeAnimeCaught:865712704315850782> For Utility"
        "\n<a:pepeban:865714938667991091> For Moderation"
        , color=11187115)
    embed.set_author(name='Server Index',
                     icon_url=bot_avatar)
    reactions = ['<:PepeLmao:865712134439436328>', '<:PepoGamer:865712213141356565>', '<a:pepeAnimeCaught:865712704315850782>', '<a:pepeban:865714938667991091>']  # fun, games, utility, moderation
    return embed, reactions


# ------------------------------------------------------------------------------

async def funHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Fun)
    embed = discord.Embed(
        title='Fun Commands',
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Fun.value)
    embed.set_author(name="Server Index -> Fun Commands",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


# ------------------------------------------------------------------------------

async def gamesHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Game)
    embed = discord.Embed(
        title="Games",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Game.value)
    embed.set_author(name="Server Index -> Games",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


async def utilityHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Utility)
    embed = discord.Embed(
        title="Utility Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}\n"
        "If you send a message link in this server you can show the message Cross Channels"

        , color=CommandCategory.Utility.value)
    embed.set_author(name="Server Index -> Utility Commands",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


async def moderationHelp(Prefix):
    description = await CreateDescription(Prefix, CommandCategory.Moderation)
    embed = discord.Embed(
        title="Moderation Commands",
        description=
        f"**For more info on each commands do** `{Prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n{description}"
        , color=CommandCategory.Moderation.value)
    embed.set_footer(text="\U00002193 React to return")
    embed.set_author(name="Server Index -> Moderation Commands",
                     icon_url=bot_avatar)
    reactions = ['<:return:867101369814745099>']
    return embed, reactions


class getHelp(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='help',
        aliases=['helpme'],
        brief='This is like help, but better.',
        help='What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx, *, args=''):
        await CreateCommands()
        args = args.split()
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            intro, reactions = await introMenu(prefix)
            embed = await ctx.send(embed=intro)
            for react in reactions:
                await embed.add_reaction(emoji=react)
        else:
            requestedCommand = args[0]
            foundCommand: HelpMenuEntry = None
            commands = HelpMenuEntry.GetAll()
            for cmd in commands:
                if requestedCommand in cmd:
                    foundCommand = cmd
                    break
            if not foundCommand:
                embed = discord.Embed(
                    title="404: Not Found",
                    description=f"Command {requestedCommand} not found",
                    color=discord.Colour.red()
                )
                await ctx.send(embed=embed)
                return
            desc = f"**Category:** {foundCommand.Category.name}\n" \
                   f"**Brief:** {foundCommand.Brief}"
            if foundCommand.Aliases:
                desc += f"\n**Aliases:** {', '.join(foundCommand.Aliases)}"
            if foundCommand.Syntax:
                desc += "\n**Syntax:** `" + foundCommand.Syntax.format(Prefix=prefix) + "`"
            embed = discord.Embed(
                title=foundCommand.Name,
                description=desc + f"\n\n{foundCommand.Desc}",
                color=foundCommand.Category.value
            )
            await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_reaction_add(self, react, un):
        # fixme reaction bug, need event handler to get latest event on message
        await CreateCommands()
        ctx = react.message
        emote = str(react.emoji)
        if ctx.embeds:
            embed = ctx.embeds[0]
            embedAuthorField = embed.author.name
            if not un.bot and ctx.author.id == 852977382016024646 and reg.search(pattern=r'\AServer Index', string=embedAuthorField):
                pf = await dumbot.getPrefix(ctx, self.bot)
                prefix = pf[2]
                if emote == "<:return:867101369814745099>":  # return
                    embed, reactions = await introMenu(prefix)
                elif emote == '<:PepeLmao:865712134439436328>':  # fun
                    embed, reactions = await funHelp(prefix)
                elif emote == '<:PepoGamer:865712213141356565>':  # games
                    embed, reactions = await gamesHelp(prefix)
                elif emote == '<a:pepeAnimeCaught:865712704315850782>':  # utility
                    embed, reactions = await utilityHelp(prefix)
                elif emote == '<a:pepeban:865714938667991091>':  # moderation
                    embed, reactions = await moderationHelp(prefix)
                else:
                    embed, reactions = None, None
                if embed and reactions:
                    await ctx.clear_reactions()
                    await ctx.edit(embed=embed)
                    for react in reactions:
                        await ctx.add_reaction(emoji=react)


def setup(bot):
    bot.add_cog(getHelp(bot))
