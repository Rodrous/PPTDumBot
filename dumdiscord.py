import discord
from discord.ext import commands
import base64

with open("config/client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8')
restrictedChannels = ["database"]

customPrefix = {}
defaultPrefix = '$'

def determinePrefix(bot, msg):
    guild = msg.guild
    if guild:     #Only allow custom prefixs in guild
        #return await bot.get_prefix(msg)
        return commands.when_mentioned_or(str(customPrefix.get(guild.id, defaultPrefix)[0]))(bot,msg)
    else:
        return commands.when_mentioned_or(defaultPrefix)(bot,msg)

# This is the same as a client initialization, but bot has more functionalities.
bot = commands.Bot(command_prefix=determinePrefix, 
    case_insensitive = True, activity=discord.Activity(type=discord.ActivityType.listening, name='$ (Why do I exist, father?)'))

@bot.command(
            name = "setprefix",
            brief = "Set your own prefixes.",
            help = "Use this to set your own custom Prefixes for the Bot to listen to.")
async def setPrefix(msg, *,prefixes = ''):
    if msg.channel.type is not discord.ChannelType.private:
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
            customPrefix[msg.guild.id] = prefixes.split() or defaultPrefix
            bot.command_prefix = determinePrefix(bot, msg)
            await msg.send(f"Prefixes set as : {bot.command_prefix}")
        else: 
            await msg.channel.send(content = 'You cant use that here yet.', delete_after=6)
    else :
        await msg.channel.send(content = 'This is a Server-Only command.', delete_after=6)

@bot.command(
            name = "prefix",
            brief = "Check the default prefix.")
async def sendPrefix(msg):
    if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
        await msg.channel.send(f'Current default prefix is : {defaultPrefix} or {await bot.get_prefix(msg)}')
    else : 
        await msg.channel.send(content = 'You cant use that here yet.', delete_after = 6)

@bot.command(
            name = "resetprefix",
            brief = "Reset the prefix to the default.",
            help = "Use this to reset the Prefix the bot listens to, to the default.")
async def resetPrefix(msg):
    if bot.get_guild(msg.guild.id):
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels):
            await setPrefix(msg,prefixes=defaultPrefix)
            await msg.channel.send(f'Reset the prefix to : {defaultPrefix}')
        else : 
            await msg.channel.send('You cant use that here yet.', delete_after=6)
    else:
        await msg.channel.send('This is a Server-Only command.', delete_after=6)

@bot.event
async def on_message(msg):
    # Add stuff here, but DO NOT DELETE THE LINE BELOW!! or nothing will work

    await bot.process_commands(msg)

# @bot.event
# async def on_member_join(member):
#     bot.get_channel(826555270155075634).send(f"<a:blobjoin:858349179893710905> {member.mention}")

# @bot.event
# async def on_member_remove(member):
#     bot.get_channel(826555270155075634).send(f"<a:blobleave:858349192169652255> {member.name}")


if __name__ == "__main__":
    bot.load_extension('cogs.fun')
    bot.load_extension('cogs.systemcommands')
    bot.load_extension('cogs.help')
    bot.load_extension('cogs.moderation')
    bot.run(id)
