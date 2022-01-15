import os
import random
from typing import List, Dict
import discord
from discord import Intents
from discord.ext import commands, tasks
from build.generalPurpose import Dumbot

guildId: str = os.environ.get("id")
restrictedChannels: List = ["Database"]
intents: Intents = discord.Intents.default()
intents.members: bool = True
intents.voice_states: bool = True
customPrefix: Dict = {}
defaultPrefix: str = "$"


def determine_prefix(bot, msg) -> list[str]:
    """
    Gets the prefix for the bot in specific guild
    """
    guild = msg.guild
    if guild:
        return commands.when_mentioned_or(
            str(customPrefix.get(guild.id, defaultPrefix)[0])
        )(bot, msg)
    else:
        return commands.when_mentioned_or(defaultPrefix)(bot, msg)


bot = commands.Bot(command_prefix=determine_prefix,
                   case_insensitive=True,
                   help_command=None,
                   intents=intents)


@bot.command(
    name="setprefix",
    brief="Set your own prefixes.",
    help="Use this to set your own custom Prefixes for the Bot to listen to.")
async def set_prefix(msg, *, prefixes="") -> None:
    if msg.channel.type is not discord.ChannelType.private:
        if msg.guild.id == 826148528870129675 and \
                (str(msg.channel) not in restrictedChannels):
            customPrefix[msg.guild.id] = prefixes.split() or defaultPrefix
            bot.command_prefix = determine_prefix(bot, msg)
            await msg.send(f"Prefixes set as : "
                           f"{await Dumbot.get_prefix(msg, bot, True)}")
        else:
            await msg.channel.send(content="You cant use that here yet.",
                                   delete_after=6)
    else:
        await msg.channel.send(content="This is a Server-Only command.",
                               delete_after=6)


@bot.command(
    name="prefix",
    brief="Check the default prefix.")
async def send_prefix(msg) -> None:
    """Sends prefix of the bot for specific guild"""
    if msg.channel.type is not discord.ChannelType.private:
        if msg.guild.id == 826148528870129675 and (
                str(msg.channel) not in restrictedChannels):
            await msg.channel.send(
                f"Current default prefix is : "
                f"{await Dumbot.get_prefix(msg, bot, True)}")
        else:
            await msg.channel.send(content="You cant use that here yet.",
                                   delete_after=6)
    else:
        await msg.channel.send(content=f"Prefix for DMs is : "
                                       f"{defaultPrefix} or by Mentioning me.")


@bot.command(
    name="resetprefix",
    brief="Reset the prefix to the default.",
    help="Use this to reset the Prefix the bot listens to, to the default.")
async def reset_prefix(msg) -> None:
    """ Reset bot prefix """
    if bot.get_guild(msg.guild.id):
        if msg.guild.id == 826148528870129675 and \
                (str(msg.channel) not in restrictedChannels):
            await set_prefix(msg, prefixes=defaultPrefix)
            await msg.channel.send(f"Reset the prefix to : {defaultPrefix}")
        else:
            await msg.channel.send("You cant use that here yet.",
                                   delete_after=6)
    else:
        await msg.channel.send("This is a Server-Only command.",
                               delete_after=6)


@bot.event
async def on_message(msg) -> None:
    await bot.process_commands(msg)


@bot.event
async def on_ready() -> None:
    await bot.wait_until_ready()
    embed = discord.Embed(title="Bot Restarted Successfully!",
                          color=52382)
    await commands.Bot.get_channel(bot, 879773094561083492).send(embed=embed)
    change_description.start()


@tasks.loop(hours=5)
async def change_description() -> None:
    """ Changes Description every 5 hours """

    # Todo Migrate this to Database
    descriptions = ["Serving", "aWYgeW91IGRlY29kZWQgdGhpcyB5b3UncmUgYSBuZXJk",
                    "ctx.send(f'fuck you {member.mention}')",
                    "Running on biodiesel",
                    "I'm one hell of a butler", "Why do i exist, father?",
                    "Waiting for Hot Topic to sell 'Distressed iPhones'",
                    "What is love? Baby dont hurt me",
                    "Blackfinix codes this bot too",
                    "Never make the same mistake twice; there are so many new ones to make",
                    "Life is beautiful… from Friday to Sunday",
                    "Time is precious. Waste it wisely",
                    "Ill be back before you can pronounce actillimandataquerin altosapaoyabayadoondib",
                    "I’m right 90% of the time, so why worry about the other 3%?",
                    "I’d grill your cheese! ~Me when flirting",
                    "When life gives you lemonade, make lemons.",
                    ]
    
    members_list: List = []
    
    for guild in bot.guilds:
        iterable_obj: list = await guild.fetch_members().flatten()
        for members in iterable_obj:
            members_list.append(members)
    
    total_members: int = len(set(members_list))
    
    serving: str = f"Serving {total_members} members " \
                   f"in {len(bot.guilds)} servers."
    descriptions.__setitem__(0, serving)
    
    rand_choice: str = str(random.choice(descriptions))
    await bot.change_presence(activity=discord.Game(
        name=f"{rand_choice}"))


if __name__ == "__main__":
    bot.load_extension("cogs.fun")
    bot.load_extension("cogs.systemcommands")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.Moderation")
    bot.load_extension("cogs.games")
    bot.load_extension("cogs.Personal")
    bot.load_extension("cogs.Database")
    bot.run(guildId)
