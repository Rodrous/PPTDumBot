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
        embed = discord.Embed(title="Bot help perhaps",
        description="Some useful commands. If a command has <:white_check_mark:857551644546826250> it works, if it has <:x:857551644546826250>, you cant use it in a server")
        #FUN HERE
        embed.add_field(name="Fun", value="_ _", inline=False)
        embed.add_field(name="ree", value="Rees out of frustration (<:white_check_mark:857551644546826250>)")
        embed.add_field(name="s", value="Sends a Random image from internet [1920x1080] (<:white_check_mark:857551644546826250>)")
        embed.add_field(name= "cat", value = "Sends a Cat pic \U0001F408 (<:white_check_mark:857551644546826250>)")
        embed.add_field(name= "quote", value = "Sends a random anime quote! (<:white_check_mark:857551644546826250>)")
        embed.add_field(name= "dog", value="Get a Dog pic \U0001F436 (<:white_check_mark:857551644546826250>)")
        embed.add_field(name="ily", value="Sends ily cuz draf do be lazy(<:white_check_mark:857551644546826250>)")
        #todo remove the complex bs
        #UTILITY HERE
        embed.add_field(name="Utility", value="_ _", inline=False)
        embed.add_field(name="steal", value="Steals emojis (<:white_check_mark:857551644546826250>)")
        embed.add_field(name="ping", value="Pings the bot or as a IT guy would say, ' Sends a ICMP packet to check the performance of connection between a server ' (<:white_check_mark:857551644546826250>)")
        #MODERATION HERE
        embed.add_field(name="Moderation", value="_ _", inline=False)
        embed.add_field(name="clear", value="Purges the chat (<:white_check_mark:857551644546826250>)")
        embed.add_field(name="invite", value="Sends 'add bot to server' link (<:x:857551644546826250>)")
        await ctx.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(gethelp(bot))