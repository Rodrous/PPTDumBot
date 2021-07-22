import discord
from discord.ext import commands, tasks
import base64, random
from build import generalPurpose as gp

with open("config/client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8')
restrictedChannels = ["database"]

customPrefix = {}
defaultPrefix = '$'


# You dont care about this a lot, only about the first return, that finds in the dictionary 'customPrefix' the prefix with
# the key of the guild that called it. This will need rework when we add db so dont care about this too much.
def determinePrefix(bot, msg):
    guild = msg.guild
    if guild:     #Only allow custom prefixs in guild
        #return await bot.get_prefix(msg)
        return commands.when_mentioned_or(str(customPrefix.get(guild.id, defaultPrefix)[0]))(bot,msg)
    else:
        return commands.when_mentioned_or(defaultPrefix)(bot,msg)

# This is the same as a client initialization, but bot has more functionalities.
bot = commands.Bot(command_prefix=determinePrefix,
    case_insensitive = True, help_command=None)

# Im sorting them via numbers, so when i do 1: explanation, the explanation is for the line 1 (and its else statement if it exists)
# 1 : Checks if the command was called inside a server
# 2 : Checks if the command was called from an allowed server (in this case Nerds&Karma) and from outside a restricted channel
# 3 : Sets the key-value pair inside the dictionary 'customPrefix' to be key = server id and value = its current prefix
#     If the server hasnt set any custom prefixes while calling the command, then this line :
#          prefixes.split() or defaultPrefix
#     has the values :
#           None or {defaultPrefix}
#     and it defaults to the default prefix
# 4 : Sets the current servers prefix to be the new (or default) prefix.
# We may need to add fragmented Bot functionality for this to work properly, but not sure, havent read the docs about it.
# 5 : Sends what the new prefixes are in the chat
@bot.command(
            name = "setprefix",
            brief = "Set your own prefixes.",
            help = "Use this to set your own custom Prefixes for the Bot to listen to.")
async def setPrefix(msg, *,prefixes = ''):
    if msg.channel.type is not discord.ChannelType.private: # 1
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels): # 2
            customPrefix[msg.guild.id] = prefixes.split() or defaultPrefix # 3
            bot.command_prefix = determinePrefix(bot, msg) # 4
            await msg.send(f"Prefixes set as : {await gp.getPrefix(msg, bot, True)}") # 5
        else:
            await msg.channel.send(content = 'You cant use that here yet.', delete_after=6)
    else :
        await msg.channel.send(content = 'This is a Server-Only command.', delete_after=6)


# Sends the current prefix in the chat
@bot.command(
            name = "prefix",
            brief = "Check the default prefix.")
async def sendPrefix(msg):
    if msg.channel.type is not discord.ChannelType.private: # Same as the 'setprefix'
        if msg.guild.id == 826148528870129675 and (str(msg.channel) not in restrictedChannels): # Same as the 'setprefix'
            await msg.channel.send(f"Current default prefix is : {await gp.getPrefix(msg, bot, True)}") # Same as the 'setprefix'
        else : 
            await msg.channel.send(content = 'You cant use that here yet.', delete_after = 6)
    else :
        await msg.channel.send(content = f'Prefix for DMs is : {defaultPrefix} or by Mentioning me.')

# Resets the prefix by calling the 'setprefix' command but with the default prefix as an argument
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

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    changeDescription.start()

# add various descriptions here
descriptions = ['aWYgeW91IGRlY29kZWQgdGhpcyB5b3UncmUgYSBuZXJk', 'Why do i exist, father?',
                'Serving 7 servers lmao', "ctx.send(f'fuck you {member.mention}')",
                'Running on biodiesel', "I'm one hell of a butler",
                "The number of members that I serve isnt accurate but I cant be assed to fix it right now."]

@tasks.loop(minutes=30)
async def changeDescription():
    totalMembers = []
    for guild in bot.guilds:
        totalMembers.extend(guild.members)
    totalMembersCount = len(totalMembers)
    randStr = random.choice(descriptions)
    serving =  f"Serving {totalMembersCount} members in {len(bot.guilds)} servers."
    print(f'{totalMembersCount} and {len(bot.guilds)}')
    #print(totalMembers)
    randChoice = str(random.choice([randStr, serving]))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{defaultPrefix}help | {randChoice}'))

if __name__ == "__main__":
    bot.load_extension('cogs.fun')
    bot.load_extension('cogs.systemcommands')
    bot.load_extension('cogs.help')
    bot.load_extension('cogs.moderation')
    bot.load_extension('cogs.games')
    bot.run(id)
