from discord.ext import commands
import discord
import re as reg
from build.generalPurpose import getPrefix

fun_color = 52382
utility_color = 16375162
moderation_color = 13524060
games_color = 6724095
bot_avatar = 'https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048'

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
    reactions = ['<:PepeLmao:865712134439436328>', '<:PepoGamer:865712213141356565>', '<a:pepeAnimeCaught:865712704315850782>', '<a:pepeban:865714938667991091>'] #fun, games, utility, moderation
    return embed, reactions

async def funHelp(prefix):
    embed = discord.Embed(
        title='Fun Commands',
        description=
        f"**For more info on each commands do** `{prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n"
        f"`{prefix}ree`: Ree's out of frustration\n"
        f"`{prefix}yeye`: Issi asked for it so yeah, it does the same as ree but yeye\n"
        f"`{prefix}wallpaper`: Sends a Random image from internet [1920x1080]\n"
        f"`{prefix}cat`: Sends a Cat pic \U0001F408\n"
        f"`{prefix}dog`: Get a Dog pic \U0001F436\n"
        f"`{prefix}quote`: Sends a random anime quote\n"
        f"`{prefix}say`: Repeats what you say\n"
        f"`{prefix}joke`: Gives you random jokes\n"
        f"`{prefix}dadjoke`: Gives you a random dadjoke, enjoy :)\n"
        f"`{prefix}yomomma`: Yomomma so dumb she didnt realize this will output random mom jokes\n"
        f"`{prefix}wikipedia`: Searches for a wikipedia query\n"
        f"`{prefix}urbandict`: Searches definition for a word\n"
        f"`{prefix}moviequotes`: Sends a random moviequote\n"
        # f"`{prefix}`:\n"
        , color=fun_color)
    embed.set_author(name="Server Index -> Fun Commands",
                     icon_url= bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions

async def gamesHelp(prefix):
    embed = discord.Embed(
        title= "Games",
        description=
        f"**For more info on each commands do** `{prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n"
        f"`{prefix}minesweeper`: Generates a game of minesweeper\n"
        # f"`{prefix}`:\n"
    , color=games_color)
    embed.set_author(name="Server Index -> Games",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions

async def utilityHelp(prefix):
    embed = discord.Embed(
        title= "Utility Commands",
        description=
        f"**For more info on each commands do** `{prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n"
        f"`{prefix}feedback [message]`: Send us feedback!\n"
        f"`{prefix}bugs [message]`: Report bugs you find\n"
        f"`{prefix}steal`: Grabs emoji's and puts it in your server\n"
        f"`{prefix}ping`: Pings the bot\n"
        # f"`{prefix}`:\n"
    , color=utility_color)
    embed.set_author(name="Server Index -> Utility Commands",
                     icon_url=bot_avatar)
    embed.set_footer(text="\U00002193 React to return")
    reactions = ['<:return:867101369814745099>']
    return embed, reactions

async def moderationHelp(prefix):
    embed = discord.Embed(
        title= "Moderation Commands",
        description=
        f"**For more info on each commands do** `{prefix}help [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n"
        f"`{prefix}clear`: Purges chat\n"
        f"`{prefix}mute`: Mutes a bitch\n"
        f"`{prefix}unmute`: Unmutes a bitch\n"
        # f"`{prefix}`:\n"
    , color=moderation_color)
    embed.set_footer(text="\U00002193 React to return")
    embed.set_author(name="Server Index -> Moderation Commands",
                     icon_url=bot_avatar)
    reactions = ['<:return:867101369814745099>']
    return embed, reactions

class gethelp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(
                name = 'help',
                aliases = ['helpme'],
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx, *, args = ''):
        args = args.split()
        pf = await getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            intro, reactions = await introMenu(prefix)
            embed = await ctx.send(embed=intro)
            for react in reactions:
                await embed.add_reaction(emoji=react)
        else:
            cmd = args[0].lower()
            aliased_commands = {
                reg.compile(pattern=r're+') : 'ree',
                reg.compile(pattern=r'ye+ye+') : 'yeye',
                reg.compile(pattern=r'(get)?joke|jk') : 'joke',
                reg.compile(pattern=r'yomom|yourmom') : 'yomomma',
                reg.compile(pattern=r'clear|purge') : 'clear',
                reg.compile(pattern=r'm(ine)?s(weeper)?') : 'minesweeper',
                reg.compile(pattern=r'say|speak') : 'say',
                reg.compile(pattern=r'wiki(pedia)?') : 'wikipedia',
                reg.compile(pattern=r'm(ovie)?q(uotes?)?') : 'moviequotes',
                reg.compile(pattern=r'f(eed)?b(ack)?'): 'feedback',
                reg.compile(pattern=r'bug-?rep(ort)?|bugs'): 'bugreport',
                reg.compile(pattern=r'(urban)?dict|urban|define'): 'dict'
            }
            for val in aliased_commands:
                if reg.match(val, string=cmd):
                    cmd = aliased_commands.get(val)

            switch_case = {
                #FUN HERE
                'ree': {
                    'aliases': 're|reee|reeee',
                    'desc': 'The bot will *REEEEEEEE* out of frustration',
                    'color': fun_color
                },
                'yeye': {
                    'aliases': 'yeeye|yeeyee|yeyee',
                    'desc': 'Same as ree but *YEEEEEEYEEEEEE*',
                    'color': fun_color
                },
                'wallpaper': {
                    'desc': 'Sends a random wallpaper in the size of `1920x1080`',
                    'color': fun_color
                },
                'cat': {
                    'desc': 'Sends a random catpic so you can apprieciate all the ADORBS',
                    'color': fun_color
                },
                'quote': {
                    'desc': 'Sends a random quote from an anime character',
                    'color': fun_color
                },
                'dog': {
                    'desc': 'Sends a random dogpic so you can apprieciate all the ADORBS',
                    'color': fun_color
                },
                'say': {
                    'aliases': 'speak',
                    'syntax': f'{prefix}say [message]',
                    'desc': 'Repeats everything you say, you cannot use this to bypass `@everyone|@here`',
                    'color': fun_color
                },
                'joke': {
                    'aliases': 'getjoke|jk',
                    'desc': 'Sends a random joke\n\n**Flags:**\n`-ex` sends any jokes, even explicit and dark jokes',
                    'color': fun_color
                },
                'dadjoke': {
                    'desc': 'I hate my life, also sends a dadjoke',
                    'color': fun_color
                },
                'yomomma': {
                    'aliases': 'yourmom|yomom',
                    'desc': 'Sends a random yomomma joke',
                    'color': fun_color
                },
                'wikipedia': {
                    'aliases': 'wiki',
                    'syntax': f'{prefix}wikipedia [query]',
                    'desc': 'Searches for something on wikipedia',
                    'color': fun_color
                },
                'moviequotes': {
                    'aliases': 'moviequote|mq',
                    'syntax': f'{prefix}moviequotes [type: OPTIONAL]',
                    'desc': 'Displays a random moviequote by default\n\n'
                            '**Types:**\n'
                            '`random`: Displays a random quote `[default]`\n'
                            '`get [ID]`: Searches for a quote based on its ID\n'
                            '`per [type: Movie|Character] [search]`: Gives a random quote based on type'
                            '\n\n__**This will be added later and explicit is not shown by default**__\n'
                            '**Blacklist:**\n'
                            f'By doing: `{prefix}moviequotes [blacklist|bl] [flag: Explicit|NSFW]`\n'
                            'You can blacklist certain tags in the server:\n'
                            '`Explicit [Off by default]`: This toggles slurs\n'
                            '`NSFW [On by default]`: This toggles NSFW quotes',
                    'color': fun_color
                },
                'dict': {
                    'aliases': 'urban|urbandict|define',
                    'syntax': f'{prefix}dict [words]',
                    'desc': 'Will give you the urban dictionary definition of something',
                    'color': fun_color
                },
                #GAMES HERE
                'minesweeper': {
                    'aliases': 'ms',
                    'syntax': f'{prefix}minesweeper [rows] [columns] [mines]',
                    'desc': 'Generates a random game of Minesweeper\n'
                            'Max rows is 11, max columns is 9 and minumum bombs is 3, and no weird numbers',
                    'color': games_color
                },
                #UTILITY HERE
                'steal': {
                    'syntax': f'{prefix}steal [emoji]|steal [emojilink]',
                    'desc': 'Steals an emoji and adds it to your server',
                    'color': utility_color
                },
                'ping': {
                    'desc': 'Pong! sends the latency of the bot',
                    'color': utility_color
                },
                'feedback': {
                    'aliases': 'fb',
                    'syntax': f'{prefix}feedback [message]',
                    'desc': 'This allows you to send us feedback, if you wish to add a command or whatever you feel you want to tell us devs!',
                    'color': utility_color
                },
                'bugreport': {
                    'aliases': 'bugrep|bug-rep|bug-report|bugs',
                    'syntax': f'{prefix}bugreport [message]',
                    'desc': 'Here you can report bugs to us',
                    'color': utility_color
                },
                #MODERATION HERE
                'clear': {
                    'aliases': 'purge',
                    'syntax': f'{prefix}clear [num]',
                    'desc': 'Clears the chat\nwill be bettered in the feature, will add more flags and make it more advanced',
                    'color': moderation_color
                },
                'mute': {
                    'syntax': f'{prefix}mute [@user] [minutes]',
                    'desc': 'Mutes a bitch, default is 10 minutes',
                    'color': moderation_color
                },
                'unmute': {
                    'syntax': f'{prefix}unmute [@user]',
                    'desc': 'Unmutes a bitch',
                    'color': moderation_color
                },
                # '': {
                #     'aliases': '{prefix}',
                #     'syntax': f'',
                #     'desc': 'REQUIRED',
                #     'color': REQUIRED
                # },
            }
            case = switch_case.get(cmd, None)
            if case:
                desc_final = f"**Prefix:** `{prefix}`\n**Name:** `{cmd.capitalize()}`"
                if case.get('aliases', None):
                    desc_final = desc_final + f"\n**Aliases:** `{case['aliases']}`"
                if case.get('syntax', None):
                    desc_final = desc_final + f"\n**Syntax:** `{case['syntax']}`"

                desc_final = desc_final + f"\n\n{case['desc']}"
                embed = discord.Embed(title="Command Help", description=desc_final, color=case['color'])
                await ctx.send(embed=embed)
            else:
                await ctx.send('Not a valid command')

    @commands.Cog.listener()
    async def on_reaction_add(self, react, un):
        ctx = react.message
        emote = str(react.emoji)
        if ctx.embeds:
            embed = ctx.embeds[0]
            embedAuthorField = embed.author.name
            if not un.bot and ctx.author.id == 852977382016024646 and reg.search(pattern=r'\AServer Index', string=embedAuthorField):
                pf = await getPrefix(ctx, self.bot)
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
    bot.add_cog(gethelp(bot))