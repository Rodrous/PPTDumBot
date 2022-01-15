from discord.ext import commands
import discord, random
from build.generalPurpose import Dumbot
from build import checks

import re as reg


private_embed_color = 6724095
bot_avatar = Dumbot.avatar()

class Personal(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(
        name="ily",
        brief="Draf is tooo lazy to type it",
        help="ily * num + name")
    async def sendIly(self, ctx):
        allowed_ids = [323457305855262721, 579036541238640731]
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

    """    HELP MENU    """
    @checks.private()
    @commands.command(
        name="personalhelp",
        aliases=["phelp", "pershelp", "privhelp", "privatehelp"])
    async def personalHelp(self, ctx, *, args= ''):
        await ctx.message.channel.purge(limit=1)
        args = args.split()
        pf = await Dumbot.get_prefix(ctx, self.bot)
        prefix = pf[2]
        if not args:
            embed = discord.Embed(
                title="Private Help Menu",
                description=
                f"**For more info on each commands do** `{prefix}phelp [command]`\n*There you will also find Syntax, Aliases and Flags for commands*\n\n"
                f"`{prefix}ily`: Sends ily cause Draf do be lazy\n"
                f"`{prefix}vc`: Pings people to vc (On a list, ask to be removed or added)"
                , color=private_embed_color)
            embed.set_footer(text="This message will self destruct in 1 minute", icon_url=bot_avatar)
            await ctx.send(embed=embed, delete_after=60)
        else:
            cmd = args[0].lower()
            aliased_commands = {
                reg.compile(pattern="FILLER"): "REMOVE WHEN FIRST ALIASED COMMAND IS HERE"
            }
            for val in aliased_commands:
                if reg.match(val, string=cmd):
                    cmd = aliased_commands.get(val)
            switch_case = {
                'ily': {
                    'desc': 'Sends ily cause Draf is lazy',
                    'color': private_embed_color
                },
                'vc': {
                    'desc': 'Pings people to vc (On a list, ask to be removed or added)',
                    'color': private_embed_color
                },

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
                embed.set_footer(text="This message will self destruct in 1 minute", icon_url=bot_avatar)
                await ctx.send(embed=embed, delete_after=60)
            else:
                await ctx.send('Not a valid command', delete_after=6)

def setup(bot):
    bot.add_cog(Personal(bot))