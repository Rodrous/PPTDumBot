from discord.ext import commands
import discord
import re as reg
from build.generalPurpose import getPrefix

async def introMenu(prefix):
    intro = discord.Embed(
        title="Bot Help Perhaps",
        description=
        f"**Server Prefix:** `{prefix}`"
        "\n*If you need help on a specific command you can type:* `help [command]`"
        "\n\n**React with:**"
        "\n<:PepeLmao:865712134439436328> For Fun"
        "\n<:PepoGamer:865712213141356565> For Games"
        "\n<a:pepeAnimeCaught:865712704315850782> For Utility"
        "\n<a:pepeban:865714938667991091> For Moderation"
        , color=11187115)
    return intro

class gethelp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass

    #todo make into a flipbook
    @commands.command(
                name = 'help',
                aliases = ['helpme'],
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def sendHelp(self, ctx, *, args = ''):
        fun_color = 52382
        utility_color = 16375162
        moderation_color = 13524060
        args = args.split()
        pf = await getPrefix(ctx, self.bot)
        prefix = pf[2]
        intro = await introMenu(prefix)
        if not args:
            #GENERAL HERE
            #general = discord.Embed(title="", description="", color=)
            #FUN HERE
            fun = discord.Embed(title="Fun Commands", color=fun_color)
            fun.add_field(name="ree", value="Rees out of frustration")
            fun.add_field(name="yeye", value="Issi asked for it so yeah it does the same as ree but yeye")
            fun.add_field(name="wallpaper", value="Sends a Random image from internet [1920x1080]")
            fun.add_field(name= "cat", value = "Sends a Cat pic \U0001F408")
            fun.add_field(name= "quote", value = "Sends a random anime quote!")
            fun.add_field(name= "dog", value="Get a Dog pic \U0001F436")
            fun.add_field(name="ily", value="Sends ily cuz draf do be lazy\nOnly allowed for Draf & Nissy")
            fun.add_field(name="say", value="Basically repeats after you")
            fun.add_field(name="joke", value="Gives you random jokes, you can use the flag `-ex` to get explicit jokes but beware may be offensive")
            fun.add_field(name="dadjoke", value="Gives you a random dadjoke, enjoy :)")
            fun.add_field(name="yomomma", value="yomomma so dumb she didnt realize this will output random mom jokes")
            fun.add_field(name="minesweeper", value="A fun game of minesweeper will be generated\nsyntax is; `minesweeper [rows] [columns] [mines]`\nMax rows is 11, max columns is 9 and minimum mines is 3")
            fun.set_footer(text="A bot by; itsPPT#9651, Blackfinix#3706 & EvilGiraffes#7300", icon_url="https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048")
            #todo remove the complex bs
            #UTILITY HERE
            utility = discord.Embed(title="Utility Commands", color=utility_color)
            utility.add_field(name="steal", value="Steals emojis")
            utility.add_field(name="ping", value="Pings the bot")
            utility.set_footer(text="A bot by; itsPPT#9651, Blackfinix#3706 & EvilGiraffes#7300", icon_url="https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048")
            #MODERATION HERE
            moderation = discord.Embed(title="Moderation Commands", color=moderation_color)
            moderation.add_field(name="clear", value="Purges the chat")
            moderation.add_field(name="mute", value="Mutes someone, default is 10 minutes")
            moderation.add_field(name="unmute", value="Unmute someone")
            moderation.set_footer(text="A bot by; itsPPT#9651, Blackfinix#3706 & EvilGiraffes#7300", icon_url="https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048")
            embeds=[intro, fun, utility, moderation]
            embed = await ctx.send(embed=intro)
            reactions = ['<:PepeLmao:865712134439436328>', '<:PepoGamer:865712213141356565>', '<a:pepeAnimeCaught:865712704315850782>', '<a:pepeban:865714938667991091>'] #fun, games, utility, moderation
            for react in reactions:
                await embed.add_reaction(emoji=react)
            # for embed in embeds:
            #     await ctx.send(content=None, embed=embed)
        else:
            aliases = ''
            syntax = ''
            cmd = args[0].lower()
            aliased_commands = {
                reg.compile(pattern=r're+') : 'ree',
                reg.compile(pattern=r'ye+ye+') : 'yeye',
                reg.compile(pattern=r'(get)?joke|jk') : 'joke',
                reg.compile(pattern=r'yomom|yourmom') : 'yomomma',
                reg.compile(pattern=r'clear|purge') : 'clear',
                reg.compile(pattern=r'm(ine)?s(weeper)?') : 'minesweeper'
            }
            for val in aliased_commands:
                if reg.match(val, string=cmd):
                    cmd = aliased_commands.get(val)

            #GENERAL HERE
            #Remember to change the first if statement in FUN to an elif when general is added lmao
            #FUN HERE
            if cmd == 'ree':
                aliases = 're|reee|reeee'
                desc = 'The bot will *REEEEEEEE* out of frustration'
                color = fun_color
            elif cmd == 'yeye':
                aliases = 'yeeye|yeeyee|yeyee'
                desc = 'Same as ree but *YEEEEEEYEEEEEE*'
                color = fun_color
            elif cmd == 'wallpaper':
                desc = 'Sends a random wallpaper in the size of `1920x1080`'
                color = fun_color
            elif cmd == 'cat':
                desc = 'Sends a random catpic so you can apprieciate all the ADORBS'
                color = fun_color
            elif cmd == 'quote':
                desc = 'Sends a random quote from an anime character'
                color = fun_color
            elif cmd == 'dog':
                desc = 'Sends a random dogpic so you can apprieciate all the ADORBS'
                color = fun_color
            elif cmd == 'ily':
                desc = 'This sends Ily * num\nOnly for Draf and Nissen'
                color = fun_color
            elif cmd == 'say':
                syntax = 'say [message]'
                desc = 'Repeats everything you say, you cannot use this to bypass `@everyone|@here`'
                color = fun_color
            elif cmd == 'joke':
                aliases = 'getjoke|jk'
                desc = 'Sends a random joke\n\n**Flags:**\n`-ex` sends any jokes, even explicit and dark jokes'
                color = fun_color
            elif cmd == 'dadjoke':
                desc = 'I hate my life, also sends a dadjoke'
                color = fun_color
            elif cmd == 'yomomma':
                aliases = 'yourmom|yomom'
                desc = 'Sends a random yomomma joke'
                color = fun_color
            elif cmd == 'minesweeper':
                aliases = 'ms'
                syntax = 'minesweeper [rows] [columns] [mines]'
                desc = 'A fun game of minesweeper will be generated\nMax rows is 11, max columns is 9 and minimum mines is 3'
                color = fun_color
            #UTILITY HERE
            elif cmd == 'steal':
                syntax = 'steal [emoji]|steal [emojilink]'
                desc = 'Steals an emoji and adds it to your server'
                color = utility_color
            elif cmd == 'ping':
                desc = 'Pong! sends the latency of the bot'
                color = utility_color
            #MODERATION HERE
            elif cmd == 'clear':
                aliases = 'purge'
                syntax = 'clear [num]'
                desc = 'Clears the chat\nwill be bettered in the feature, will add more flags and make it more advanced'
                color = moderation_color
            elif cmd == 'mute':
                syntax = 'mute [@user] [minutes]'
                desc = 'Mutes a bitch, default is 10 minutes'
                color = moderation_color
            elif cmd == 'unmute':
                syntax = 'unmute [@user]'
                desc = 'Unmutes a bitch'
                color = moderation_color
            # elif cmd == '':
            #     aliases = ''
            #     syntax = ''
            #     desc = 'REQUIRED'
            #     color = REQUIRED
            else:
                desc = ''

            desc_final = f"**Name:** `{cmd.capitalize()}`"
            if aliases:
                desc_final = desc_final + f"\n**Aliases:** `{aliases}`"
            if syntax:
                desc_final = desc_final + f"\n**Syntax:** `{syntax}`"
            if desc:
                desc_final = desc_final + f"\n\n{desc}"
                embed = discord.Embed(title="Command Help", description=desc_final, color = color)
                await ctx.send(embed=embed)
            else:
                await ctx.send('Not a valid command')

def setup(bot):
    bot.add_cog(gethelp(bot))