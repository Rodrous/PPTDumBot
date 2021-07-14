from discord.ext import commands
import discord

class gethelp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    #todo make into a flipbook
    @commands.command(
                name = 'helpme',
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def sendHelp(self,ctx):
        #INTRO
        intro = discord.Embed(title="Bot Help Perhaps", description="Here you can find all the useful commands we have implemented", color=11187115)
        #GENERAL
        #general = discord.Embed(title="", description="", color=)
        #FUN HERE
        fun = discord.Embed(title="Fun Commands", color=52382)
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
        #todo remove the complex bs
        #UTILITY HERE
        utility = discord.Embed(title="Utility Commands", color=16375162)
        utility.add_field(name="steal", value="Steals emojis")
        utility.add_field(name="ping", value="Pings the bot")
        #MODERATION HERE
        moderation = discord.Embed(title="Moderation Commands", color=13524060)
        moderation.add_field(name="clear", value="Purges the chat")
        moderation.add_field(name="mute", value="Mutes someone")
        moderation.add_field(name="unmute", value="Unmute someone")
        moderation.set_footer(text="A bot by; itsPPT#9651, Blackfinix#3706 & EvilGiraffes#7300", icon_url="https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048")
        embeds=[intro, fun, utility, moderation]
        for embed in embeds:
            await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(gethelp(bot))