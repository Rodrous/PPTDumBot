from discord.ext import commands
import discord, random

def devsOnly(ctx):
    devs = {
        "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
    }
    devs = list(devs.values())
    return devs.__contains__(ctx.author.id)

def private(ctx):
    whitelist = {
        # Devs
        "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
        # Dev Alts
        "Giraffe | Gif": 701049734382485615,

        # Friends
        "Karma": 564921559836393481,
        "Artsy": 793706755950903306,
        "Nissy": 579036541238640731,
        "Ayça": 581249861429493782,
        "Xan": 307210893144621068,
        "Gabo": 480170339335143426,
        # Friend Alts
        "Karma | EllaJD": 845876972222808065
    }
    whitelist = list(whitelist.values())
    return whitelist.__contains__(ctx.author.id)

devsonly = commands.check(devsOnly)
private = commands.check(private)

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
        pinged_people_list = list(pinged_people.values())
        AUTHOR = ctx.author.id
        if pinged_people_list.__contains__(AUTHOR):
            pinged_people_list.remove(AUTHOR)
            string = f"**{ctx.author.name}:** Wanna vc?\n\n"
            for person in pinged_people_list:
                string += f"<@{str(person)}> "
            await ctx.send(string)

def setup(bot):
    bot.add_cog(personal(bot))