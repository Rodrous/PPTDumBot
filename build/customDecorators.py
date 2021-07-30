"""    Personal    """
def devsOnly(ctx):
    devs = {
        "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
    }
    devs = set(devs.values())
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
    whitelist = set(whitelist.values())
    return whitelist.__contains__(ctx.author.id)

"""      Specific     """
def Feedback_n_bug_blacklist(ctx):
    blacklist = {
        #Devs
        # "Giraffe": 323457305855262721,
        "Ppt": 311919809895858177,
        "Finix": 239762173440557057,
        #Devs Alts
        "Giraffe | Gif": 701049734382485615

        #Actual Blacklist
    }
    blacklist = set(blacklist.values())
    return ctx.author.id not in blacklist