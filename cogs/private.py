import random

from discord.ext import commands


class personal(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

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


def setup(bot):
    bot.add_cog(personal(bot))