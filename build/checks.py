from discord.ext import commands
import discord
"""    Personal    """
def devlist():
    return {
        #Devs
        "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
        #Alts
        "Giraffe | Gif": 701049734382485615,
    }

def devsOnly(*args):
    def predicate(ctx):
        devs = devlist()
        devs = set(devs.values())
        return devs.__contains__(ctx.author.id)
    return commands.check(predicate)

def private(*args):
    def predicate(ctx):
        devs = devlist()
        whitelist = {
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
        whitelist.update(devs)
        whitelist = set(whitelist.values())
        return whitelist.__contains__(ctx.author.id)
    return commands.check(predicate)

"""      Specific     """
def Feedback_n_bug_blacklist(*args):
    def predicate(ctx):
        blacklist = {"Giraffe | Gif": 701049734382485615}
        blacklist = set(blacklist.values())
        return ctx.author.id not in blacklist
    return commands.check(predicate)
