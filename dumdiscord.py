import os
from typing import List, Dict

import discord
from discord import Intents
from discord.ext import commands, tasks
from dotenv import load_dotenv

from general.backEnd import getRandomDescription
from general.generalPurpose import Dumbot

load_dotenv()

bot_id: str = os.environ.get("clientId")
restrictedChannels: List = ["database"]
intents: Intents = discord.Intents.default()
intents.members: bool = True
intents.voice_states: bool = True
customPrefix: Dict = {}
defaultPrefix: str = "!"


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
    if bot.get_guild(msg.guild.clientId):
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
    # embed = discord.Embed(title="Bot Restarted Successfully!",
    #                       color=52382)
    # await commands.Bot.get_channel(bot, 934244768651833344).send(embed=embed)
    change_description.start()


@tasks.loop(hours=5)
async def change_description() -> None:
    """ Changes Description every 5 hours """
    description = await getRandomDescription()
    await bot.change_presence(activity=discord.Game(
        name=f"{description}"))


if __name__ == "__main__":
    bot.load_extension("cogs.fun")
    bot.load_extension("cogs.utility")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.moderation")
    bot.load_extension("cogs.games")
    bot.load_extension("cogs.private")
    bot.load_extension("cogs.database")
    bot.run(bot_id)
