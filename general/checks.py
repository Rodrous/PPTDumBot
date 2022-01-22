from typing import Dict, Set

from discord.ext import commands

devList: Dict[str, int] = {
        # Devs
        "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
        # Alts
        "Giraffe | Gif": 701049734382485615,
    }


def devsOnly(*args):
    def predicate(ctx) -> bool:
        devs: Set = set(devList.values())
        return ctx.author.id in devs
    
    return commands.check(predicate)


def private(*args):
    def predicate(ctx) -> bool:
        whitelist: Dict[str, int] = {
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
        whitelist.update(devList)
        whitelist: Set = set(whitelist.values())
        return ctx.author.id in whitelist
    
    return commands.check(predicate)


def feedback_n_bug_blacklist(*args):
    def predicate(ctx):
        blacklist: Dict = {}
        blacklist: Set = set(blacklist.values())
        return ctx.author.id not in blacklist
    
    return commands.check(predicate)
