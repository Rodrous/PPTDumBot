from discord.ext import commands
import discord, random
import re as reg
from build.generalPurpose import dumbot
from build.customDecorators import private, devsOnly
from helpMenu import initialize, menus
from helpMenu.commands import RestrictedCategory
from helpMenu.helpMenuEntry import HelpMenuEntry

devsonly = commands.check(devsOnly)
private = commands.check(private)
private_embed_color = 6724095
bot_avatar = dumbot.avatar()


class personal(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @private
    @commands.command(
        name="ily",
        brief="Draf is tooo lazy to type it",
        help="ily * num + name")
    async def sendIly(self, ctx):
        allowed_ids = [323457305855262721, 579036541238640731]  # [DRAF, NISSY]
        AUTHOR = ctx.author.id
        if allowed_ids.__contains__(AUTHOR):
            randomint = "1" + "0" * random.randint(10, 100)
            num = random.randint(10, int(randomint))
            DRAF = allowed_ids[0]
            NISSY = allowed_ids[1]
            if AUTHOR == DRAF:
                name = NISSY
            elif AUTHOR == NISSY:
                name = DRAF
            await ctx.send("ily " + str(num) + f" <@{name}>")

    @private
    @commands.command(
        name="vc")
    async def wannaVc(self, ctx):
        pinged_people = {
            "Artsy": 793706755950903306,
            "Giraffe": 323457305855262721,
            "Nissy": 579036541238640731,
            "Ayça": 581249861429493782,
            "Xan": 307210893144621068,
            "Gabo": 480170339335143426
        }
        pinged_people_list = set(pinged_people.values())
        AUTHOR = ctx.author.id
        if pinged_people_list.__contains__(AUTHOR):
            pinged_people_list.remove(AUTHOR)
            string = f"**{ctx.author.name}:** Wanna vc?\n\n"
            for person in pinged_people_list:
                string += f"<@{str(person)}> "
            await ctx.send(string)

    """    HELP MENU    """
    @private
    @commands.command(
        name="personalhelp",
        aliases=["phelp", "pershelp", "privhelp", "privatehelp"])
    async def personalHelp(self, ctx, *, args= ''):
        await initialize.PrivateCommands()
        await ctx.message.channel.purge(limit=1)
        args = args.split()
        pf = await dumbot.getPrefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            embed = await menus.Private(prefix)
            await ctx.send(embed=embed, delete_after=60)
        else:
            requestedCommand = args[0]
            foundCommand: HelpMenuEntry = HelpMenuEntry.PrivateSearch(requestedCommand, RestrictedCategory.Private)
            if not foundCommand:
                embed = discord.Embed(
                    title="404: Not Found",
                    description=f"Command {requestedCommand} not found",
                    color=discord.Colour.red()
                )
                await ctx.send(embed=embed)
                return
            desc = str(foundCommand).format(Prefix=prefix)
            embed = discord.Embed(
                title=foundCommand.Name,
                description=desc,
                color=foundCommand.Category.value
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(personal(bot))