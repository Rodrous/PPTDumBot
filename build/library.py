import random
import re as reg

"""
Feel free to add as many moviequotes as you want, if there is no character or image leave it blank but dont remove it
"""

class moviequotes:
    mq = [
        {"movie": "Dirty Harry [1971]", "character": "Dirty Harry",
         "quote": "You've got to ask yourself one question; Do you feel lucky? well, do ya, punk?",
         "image": "https://prod.cdn.bbaws.net/TDC_Blockbuster_-_Production/79/16/WB-0008_po-reg-medium_orig.jpg"},
        {"movie": "Sudden Impact [1983]", "character": "Dirty Harry",
         "quote": "Go ahead. Make my day.",
         "image": "https://images-na.ssl-images-amazon.com/images/S/pv-target-images/8f7c63364fbd9d1b804c755ca7cd93309aa4f44e95ee87c1a341413a1486ffbe._RI_V_TTW_.jpg"},
        {"movie": "The Godfather [1972]", "character": "Don Vito Corleone",
         "quote": "I'm gonna make him an offer he cant refuse",
         "image": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
        {"movie": "Psycho[1960]", "character": "Norman Bates",
         "quote": "A boy's best friend is his mother",
         "image": "https://tuploads.s3.eu-west-1.amazonaws.com/production/uploads/event/image/107693/default_5404___7979721490.jpg"},
        {"movie": "Ace Ventura Pet Detective [1994]", "character": "Ace Ventura",
         "quote": "Captain's Log, stardate 23.9, rounded off to the... nearest decimal point. We've... traveled back in time to save an ancient species from... total annihilation. SO FAR... no... signs of aquatic life, but I'm going to find it. If I have to tear this universe another black hole, I'm going to find it. I've... GOT TO, MISTER.",
         "image": "https://m.media-amazon.com/images/M/MV5BYmVhNmFmOGYtZjgwNi00ZGQ0LThiMmQtOGZjMDUzNzJhMGIzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"movie": "Ace Ventura Pet Detective [1994]", "character": "Ace Ventura",
         "quote": "Once you get inside my head, there's no turning back baby.",
         "image": "https://m.media-amazon.com/images/M/MV5BYmVhNmFmOGYtZjgwNi00ZGQ0LThiMmQtOGZjMDUzNzJhMGIzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"},
        {"movie": "Groundhog Day [1993]", "character": "Larry",
         "quote": "People just don't understand what is involved in this. This is an art-form! You know, I think that most people just think that I hold a camera and point at stuff, but there is a heck of a lot more to it than just that.",
         "image": "https://resizing.flixster.com/BpqNxyKbd_9M2NmFo_XEIAT6yPw=/206x305/v2/https://flxt.tmsimg.com/assets/p14569_p_v10_ay.jpg"},
        {"movie": "The Mask [1994]", "character": "The Mask",
         "quote": "Our love is like a red, red rose... and I am a little thorny.",
         "image": "https://cdn.cdon.com/media-dynamic/images/product/movie/dvd/image4/the_mask_nordic-17812141-frntl.jpg?impolicy=product&w=340&h=340"},
        {"movie": "The Mask [1994]", "character": "Peggy Brandt",
         "quote": "Do you know how hard it is to find a decent man in this town? Most of them think monogamy is some kind of wood.",
         "image": "https://cdn.cdon.com/media-dynamic/images/product/movie/dvd/image4/the_mask_nordic-17812141-frntl.jpg?impolicy=product&w=340&h=340"},
        {"movie": "Police Academy [1984]", "character": "Cadet Eugene Tackleberry",
         "quote": "Drop that stereo before I blow your goddamn nuts off, asshole.",
         "image": "https://m.media-amazon.com/images/M/MV5BMjNiMWVhNjAtMzgyYS00NzRhLWJmNGUtNzdiOGFhMmY5NDUwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"},
        {"movie": "Austin Powers: The Spy Who Shagged Me [1999]", "character": "Austin Powers",
         "quote": "So, shall we shag now, or shall we shag later? How do you like to do it? Do you like to wash up first? Top and tails? A whore's bath? Personally, before I'm on the JOB, I like to give my undercarriage a bit of a \"how's-your-father\".",
         "image": "https://flxt.tmsimg.com/assets/p23153_p_v10_aa.jpg"},
        {"movie": "Austin Powers: The Spy Who Shagged Me [1999]", "character": "Austin Powers",
         "quote": "I can't believe Vanessa, my bride, my one true love, the woman who taught me the beauty of monogamy, was a fembot all along. Wait a tick, that means I'm single again! Oh behave!",
         "image": "https://flxt.tmsimg.com/assets/p23153_p_v10_aa.jpg"},
        {"movie": "Austin Powers: In Goldmember [2002]", "character": "Nigel Powers",
         "quote": "There are only two things I can't stand in this world: People who are intolerant of other people's cultures, and the Dutch.",
         "image": "https://lh3.googleusercontent.com/proxy/ZJMqjotntOWvKAwjs2wMiKs5mIgwBz_eCarGjuQPOMfzYWxx-6rWI-ZCHmsu1Vx4vu6PilzRGBrhHR-VhoChqg3kzaY7zpyWm3ZXf6cuxSNEmVRwRgi0X2aVVzaue1gnOmp3-4tz6YObNlP2b0xpOy_Q"},
        {"movie": "Austin Powers: In Goldmember [2002]", "character": "Dr Evil",
         "quote": "I never knew my birth parents. There was a car accident. My birth mother was incinerated, and I only survived because her smoking carcass had formed a protective cocoon of slaughtered human effluence. A Belgian man and his fifteen year-old love slave were looting the accident scene, and came across a blood soaked baby, moi. They raised me to be evil. You know, that old chestnut.",
         "image": "https://lh3.googleusercontent.com/proxy/ZJMqjotntOWvKAwjs2wMiKs5mIgwBz_eCarGjuQPOMfzYWxx-6rWI-ZCHmsu1Vx4vu6PilzRGBrhHR-VhoChqg3kzaY7zpyWm3ZXf6cuxSNEmVRwRgi0X2aVVzaue1gnOmp3-4tz6YObNlP2b0xpOy_Q"},
        {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
         "quote": "Don't talk like one of them. You're not! Even if you'd like to be. To them, you're just a freak, like me! They need you right now, but when they don't, they'll cast you out, like a leper! You see, their morals, their code, it's a bad joke. Dropped at the first sign of trouble. They're only as good as the world allows them to be. I'll show you. When the chips are down, these... these civilized people, they'll eat each other. See, I'm not a monster. I'm just ahead of the curve.",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
         "quote": "You know what I've noticed? Nobody panics if things go \"according to plan…\" even if that plan is horrifying. If tomorrow, I tell the press that, like, a gang-banger will get shot, or a truckload of soldiers will be blown up, nobody panics because it's all \"part of the plan.\" But if I say that one little old mayor will die…well then everyone loses their minds!",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
         "quote": "I believe whatever doesn't kill you simply makes you… stranger.",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
         "quote": "I took Gotham's white knight and I brought him down to our level. It wasn't hard. You see, madness, as you know, is like gravity. All it takes is a little push!",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"movie": "Batman The Dark Knight [2008]", "character": "Batman",
         "quote": "Sometimes the truth isn't good enough, sometimes people deserve more. Sometimes people deserve to have their faith rewarded...",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        {"movie": "Batman The Dark Knight [2008]", "character": "Harvey Dent",
         "quote": "You either die a hero, or you live long enough to see yourself become the villain.",
         "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"},
        # {"movie": "", "character": "",
        # "quote": "",
        # "image": ""},
    ]
    id = 1
    for item in mq:
        item['id'] = id
        id += 1

    @classmethod
    async def random(cls):
        mq = cls.mq
        return random.choice(mq)

    @classmethod
    async def GET(cls, ID: int):
        mq = cls.mq
        num = ID - 1
        return mq[num]

    @classmethod
    async def per(cls, Type: str, Regex: str):
        mq = cls.mq
        Type = Type.lower()
        choices = []
        for item in mq:
            if reg.search(pattern=Regex, string=item[Type], flags=reg.I):
                choices.append(item)
        if choices:
            return random.choice(choices)

    @classmethod
    async def search(cls, String: str):
        pass