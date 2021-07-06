from discord.ext import commands
import discord

class gethelp(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(
                name = 'helpme',
                brief = 'This is like help, but better.',
                help = 'What else do you need to know bro, just run the command')
    async def sendHelp(self,ctx):
        #GENERAL HERE
        general = discord.Embed(title="Bot Help Perhaps", description="Some useful commands. If a command has <:white_check_mark:857551644546826250> it works, if it has <:x:857551644546826250>, you cant use it in a server", color=11187115)
        #FUN HERE
        fun = discord.Embed(title="Fun Commands", color=52382)
        fun.add_field(name="ree", value="Rees out of frustration (<:white_check_mark:857551644546826250>)")
        fun.add_field(name="s", value="Sends a Random image from internet [1920x1080] (<:white_check_mark:857551644546826250>)")
        fun.add_field(name= "cat", value = "Sends a Cat pic \U0001F408 (<:white_check_mark:857551644546826250>)")
        fun.add_field(name= "quote", value = "Sends a random anime quote! (<:white_check_mark:857551644546826250>)")
        fun.add_field(name= "dog", value="Get a Dog pic \U0001F436 (<:white_check_mark:857551644546826250>)")
        fun.add_field(name="ily", value="Sends ily cuz draf do be lazy\nOnly allowed for Draf & Nissy(<:white_check_mark:857551644546826250>)")
        #todo remove the complex bs
        #UTILITY HERE
        utility = discord.Embed(title="Utility Commands", color=16375162)
        utility.add_field(name="steal", value="Steals emojis (<:white_check_mark:857551644546826250>)")
        utility.add_field(name="ping", value="Pings the bot or as a IT guy would say:\n' Sends a ICMP packet to check the performance of connection between a server ' (<:white_check_mark:857551644546826250>)")
        #MODERATION HERE
        moderation = discord.Embed(title="Moderation Commands", color=13524060)
        moderation.add_field(name="clear", value="Purges the chat (<:white_check_mark:857551644546826250>)")
        moderation.add_field(name="invite", value="Sends 'add bot to server' link (<:x:857551644546826250>)")
        embeds=[general, fun, utility, moderation]
        for embed in embeds:
            await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(gethelp(bot))