import random
import re as reg

class moviequotes:

    @staticmethod
    async def movielist():
        """
        Feel free to add as many moviequotes as you want
        Flags:
            Explicit: racial slurs, or similar (swearing dont count)
            NSFW: Anything that mentions something sexual
        Quote type quotes: If you do not know the character or image leave it blank, do NOT remove it
        Dialogue type quotes: There is no character in this type so you need to HIGHLIGHT characters in this fashion:
                              **Peter:** Dialogue comes here\n
                              **Sofia:** Next Dialogue comes here
                              Remember the \n newline character after each except the last one
        Templates at the bottom of the list
        """
        mq = [
            # DIRTY HARRY
            {"movie": "Dirty Harry [1971]", "character": "Dirty Harry",
             "quote": "You've got to ask yourself one question; Do you feel lucky? well, do ya, punk?",
             "image": "https://prod.cdn.bbaws.net/TDC_Blockbuster_-_Production/79/16/WB-0008_po-reg-medium_orig.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Sudden Impact [1983]", "character": "Dirty Harry",
             "quote": "Go ahead. Make my day.",
             "image": "https://images-na.ssl-images-amazon.com/images/S/pv-target-images/8f7c63364fbd9d1b804c755ca7cd93309aa4f44e95ee87c1a341413a1486ffbe._RI_V_TTW_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # GODFATHER
            {"movie": "The Godfather [1972]", "character": "Don Vito Corleone",
             "quote": "I'm gonna make him an offer he cant refuse",
             "image": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # PSYCHO
            {"movie": "Psycho [1960]", "character": "Norman Bates",
             "quote": "A boy's best friend is his mother",
             "image": "https://tuploads.s3.eu-west-1.amazonaws.com/production/uploads/event/image/107693/default_5404___7979721490.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # ACE VENTURA
            {"movie": "Ace Ventura Pet Detective [1994]", "character": "Ace Ventura",
             "quote": "Captain's Log, stardate 23.9, rounded off to the... nearest decimal point. We've... traveled back "
                      "in time to save an ancient species from... total annihilation. SO FAR... no... signs of aquatic "
                      "life, but I'm going to find it. If I have to tear this universe another black hole, I'm going to "
                      "find it. I've... GOT TO, MISTER.",
             "image": "https://m.media-amazon.com/images/M/MV5BYmVhNmFmOGYtZjgwNi00ZGQ0LThiMmQtOGZjMDUzNzJhMGIzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Ace Ventura Pet Detective [1994]", "character": "Ace Ventura",
             "quote": "Once you get inside my head, there's no turning back baby.",
             "image": "https://m.media-amazon.com/images/M/MV5BYmVhNmFmOGYtZjgwNi00ZGQ0LThiMmQtOGZjMDUzNzJhMGIzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # GROUNDHOG DAY
            {"movie": "Groundhog Day [1993]", "character": "Larry",
             "quote": "People just don't understand what is involved in this. This is an art-form! You know, I think that "
                      "most people just think that I hold a camera and point at stuff, but there is a heck of a lot more "
                      "to it than just that.",
             "image": "https://resizing.flixster.com/BpqNxyKbd_9M2NmFo_XEIAT6yPw=/206x305/v2/https://flxt.tmsimg.com/assets/p14569_p_v10_ay.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # THE MASK
            {"movie": "The Mask [1994]", "character": "The Mask",
             "quote": "Our love is like a red, red rose... and I am a little thorny.",
             "image": "https://cdn.cdon.com/media-dynamic/images/product/movie/dvd/image4/the_mask_nordic-17812141-frntl.jpg?impolicy=product&w=340&h=340",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Mask [1994]", "character": "Peggy Brandt",
             "quote": "Do you know how hard it is to find a decent man in this town? Most of them think monogamy is some kind of wood.",
             "image": "https://cdn.cdon.com/media-dynamic/images/product/movie/dvd/image4/the_mask_nordic-17812141-frntl.jpg?impolicy=product&w=340&h=340",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # POLICE ACADEMY
            {"movie": "Police Academy [1984]", "character": "Cadet Eugene Tackleberry",
             "quote": "Drop that stereo before I blow your goddamn nuts off, asshole.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjNiMWVhNjAtMzgyYS00NzRhLWJmNGUtNzdiOGFhMmY5NDUwL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Police Academy 2: Their First Assignment [1985]", "character": "Mahoney",
             "quote": "You have the right to remain silent. You have the right to a court appointed attorney. You have "
                      "the right to sing the blues. You have the right to cable TV... that's very important. You have the "
                      "right to sublet. You have the right to paint the walls... no loud colors.",
             "image": "https://m.media-amazon.com/images/M/MV5BMzdlYmZiMDctMWNiZS00YmY5LWEzMjYtMTY4ZDg3NTg2MjUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # AUSTIN POWERS
            {"movie": "Austin Powers: The Spy Who Shagged Me [1999]", "character": "Austin Powers",
             "quote": "So, shall we shag now, or shall we shag later? How do you like to do it? Do you like to wash up "
                      "first? Top and tails? A whore's bath? Personally, before I'm on the JOB, I like to give my "
                      "undercarriage a bit of a \"how's-your-father\".",
             "image": "https://flxt.tmsimg.com/assets/p23153_p_v10_aa.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": True}
             },
            {"movie": "Austin Powers: The Spy Who Shagged Me [1999]", "character": "Austin Powers",
             "quote": "I can't believe Vanessa, my bride, my one true love, the woman who taught me the beauty of "
                      "monogamy, was a fembot all along. Wait a tick, that means I'm single again! Oh behave!",
             "image": "https://flxt.tmsimg.com/assets/p23153_p_v10_aa.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Austin Powers: In Goldmember [2002]", "character": "Nigel Powers",
             "quote": "There are only two things I can't stand in this world: People who are intolerant of other people's cultures, and the Dutch.",
             "image": "https://lh3.googleusercontent.com/proxy/ZJMqjotntOWvKAwjs2wMiKs5mIgwBz_eCarGjuQPOMfzYWxx-6rWI-ZCHmsu1Vx4vu6PilzRGBrhHR-VhoChqg3kzaY7zpyWm3ZXf6cuxSNEmVRwRgi0X2aVVzaue1gnOmp3-4tz6YObNlP2b0xpOy_Q",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Austin Powers: In Goldmember [2002]", "character": "Dr Evil",
             "quote": "I never knew my birth parents. There was a car accident. My birth mother was incinerated, "
                      "and I only survived because her smoking carcass had formed a protective cocoon of slaughtered "
                      "human effluence. A Belgian man and his fifteen year-old love slave were looting the accident "
                      "scene, and came across a blood soaked baby, moi. They raised me to be evil. You know, "
                      "that old chestnut.",
             "image": "https://lh3.googleusercontent.com/proxy/ZJMqjotntOWvKAwjs2wMiKs5mIgwBz_eCarGjuQPOMfzYWxx-6rWI-ZCHmsu1Vx4vu6PilzRGBrhHR-VhoChqg3kzaY7zpyWm3ZXf6cuxSNEmVRwRgi0X2aVVzaue1gnOmp3-4tz6YObNlP2b0xpOy_Q",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # BATMAN
            {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
             "quote": "Don't talk like one of them. You're not! Even if you'd like to be. To them, you're just a freak, "
                      "like me! They need you right now, but when they don't, they'll cast you out, like a leper! You "
                      "see, their morals, their code, it's a bad joke. Dropped at the first sign of trouble. They're only "
                      "as good as the world allows them to be. I'll show you. When the chips are down, these... these "
                      "civilized people, they'll eat each other. See, I'm not a monster. I'm just ahead of the curve.",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
             "quote": "You know what I've noticed? Nobody panics if things go \"according to plan…\" even if that plan is "
                      "horrifying. If tomorrow, I tell the press that, like, a gang-banger will get shot, or a truckload "
                      "of soldiers will be blown up, nobody panics because it's all \"part of the plan.\" But if I say "
                      "that one little old mayor will die…well then everyone loses their minds!",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
             "quote": "I believe whatever doesn't kill you simply makes you… stranger.",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Batman The Dark Knight [2008]", "character": "The Joker",
             "quote": "I took Gotham's white knight and I brought him down to our level. It wasn't hard. You see, "
                      "madness, as you know, is like gravity. All it takes is a little push!",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Batman The Dark Knight [2008]", "character": "Batman",
             "quote": "Sometimes the truth isn't good enough, sometimes people deserve more. Sometimes people deserve to have their faith rewarded...",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Batman The Dark Knight [2008]", "character": "Harvey Dent",
             "quote": "You either die a hero, or you live long enough to see yourself become the villain.",
             "image": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # SCARFACE
            {"movie": "Scarface [1983]", "character": "Tony Montana",
             "quote": "You wanna fuck with me? Okay. You wanna play rough? Okay. Say hello to my little friend!",
             "image": "https://m.media-amazon.com/images/M/MV5BNjdjNGQ4NDEtNTEwYS00MTgxLTliYzQtYzE2ZDRiZjFhZmNlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_FMjpg_UX1000_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # RAMBO
            {"movie": "Rambo V: Last Blood [2019]", "character": "John Rambo",
             "quote": "I've lived in a world of death. I've watched people I've loved die. Some fast with a bullet, "
                      "some not enough left to bury. All these years I've kept my secrets, but the time has come to face "
                      "my past. And if they come looking for me, they will welcome death. I want revenge. I want them to "
                      "know that death is coming. And there's nothing they can do to stop it.",
             "image": "https://p3.no/filmpolitiet/wp-content/thumbs/?src=https://p3.no/filmpolitiet/wp-content/uploads/2019/09/Rambo-V-Last-Blood-plakat.jpg&w=750",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Rambo [2008]", "character": "John Rambo",
             "quote": "Any of you boys want to shoot, now's the time. There isn't one of us that doesn't want to be "
                      "someplace else. But this is what we do, who we are. Live for nothing, or die for something. Your call.",
             "image": "http://www.platekompaniet.no//globalassets/imported-images/dvd/2001676149.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # PULP FICTION
            {"movie": "Pulp Fiction [1994]", "character": "Jules",
             "quote": "There's a passage I got memorized. Ezekiel 25:17. \"The path of the righteous man is beset on all "
                      "sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name "
                      "of charity and good will, shepherds the weak through the valley of the darkness, for he is truly "
                      "his brother's keeper and the finder of lost children. And I will strike down upon thee with great "
                      "vengeance and furious anger those who attempt to poison and destroy My brothers. And you will know "
                      "I am the Lord when I lay My vengeance upon you.\" Now... I been sayin' that shit for years. And if "
                      "you ever heard it, that meant your ass. You'd be dead right now. I never gave much thought to what "
                      "it meant. I just thought it was a cold-blooded thing to say to a motherfucker before I popped a "
                      "cap in his ass. But I saw some shit this mornin' made me think twice. See, now I'm thinking: maybe "
                      "it means you're the evil man. And I'm the righteous man. And Mr. 9mm here... he's the shepherd "
                      "protecting my righteous ass in the valley of darkness. Or it could mean you're the righteous man "
                      "and I'm the shepherd and it's the world that's evil and selfish. And I'd like that. But that shit "
                      "ain't the truth. The truth is you're the weak. And I'm the tyranny of evil men. But I'm tryin', "
                      "Ringo. I'm tryin' real hard to be the shepherd.",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]", "character": "Jules",
             "quote": "English, motherfucker, do you speak it?",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]", "character": "Jules",
             "quote": "Say 'what' again. Say 'what' again, I dare you, I double dare you motherfucker, say what one more Goddamn time!",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]", "character": "Marsellus",
             "quote": "What now? Let me tell you what now. I'ma call a coupla hard, pipe-hittin' niggers, who'll go to "
                      "work on the homes here with a pair of pliers and a blow torch. You hear me talkin', hillbilly boy? "
                      "I ain't through with you by a damn sight. I'ma get medieval on your ass.",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "quote", "flags": {"Explicit": True, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]", "character": "Jules",
             "quote": "Well, I'm a mushroom-cloud-layin' motherfucker, motherfucker! Every time my fingers touch brain, "
                      "I'm Superfly T.N.T., I'm the Guns of the Navarone! IN FACT, WHAT THE FUCK AM I DOIN' IN THE BACK? "
                      "YOU'RE THE MOTHERFUCKER WHO SHOULD BE ON BRAIN DETAIL! We're fuckin' switchin'! I'm washin' the "
                      "windows, and you're pickin' up this nigger's skull!",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "quote", "flags": {"Explicit": True, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]",
             "quote": "**Honey Bunny:** I love you, Pumpkin\n"
                      "**Pumpkin:** I love you, Honey Bunny\n"
                      "**Pumpkin:** All right, everybody be cool, this is a robbery!\n"
                      "**Honey Bunny:** Any of you fucking pricks move, and I'll execute every motherfucking last one of ya!",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Pulp Fiction [1994]",
             "quote": "**Mia:** Don't you hate that?\n"
                      "**Vincent:** What?\n"
                      "**Mia:** Uncomfortable silences "
                      "Why do we feel it's necessary to yak about bullshit in order to be comfortable?\n"
                      "**Vincent:** I don't know. That's a good question\n"
                      "**Mia:** That's when you know you've found somebody special,\n"
                      "When you can just shut the fuck up for a minute and comfortably enjoy the silence",
             "image": "https://static.posters.cz/image/750/plakater/pulp-fiction-cover-i1288.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            # THE BALLAD OF BUSTER SCRUGGS
            {"movie": "The Ballad Of Buster Scruggs [2018]", "character": "Buster Scruggs",
             "quote": "There's just gotta be a place up ahead where men ain't low-down and poker's played fair. "
                      "If there weren't, what are all the songs about? I'll see y'all there. And we can sing together "
                      "and shake our heads over all the meanness in the used-to-be.",
             "image": "https://m.media-amazon.com/images/M/MV5BYjRkYTI3M2EtZWQ4Ny00OTA2LWFmMTMtY2E4MTEyZmNjOTMxXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Ballad Of Buster Scruggs [2018]", "character": "Buster Scruggs",
             "quote": "Sir, it seems that you're are a no better a judge of human beings than you are a specimen of one. "
                      "Just on a brief inventory I'd say you could use yourself a shave and a better disposition. "
                      "And lastly, if you don't my mind me aspersing your friends... a better class of drinking buddies.",
             "image": "https://m.media-amazon.com/images/M/MV5BYjRkYTI3M2EtZWQ4Ny00OTA2LWFmMTMtY2E4MTEyZmNjOTMxXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Ballad Of Buster Scruggs [2018]", "character": "Buster Scruggs",
             "quote": "I'm not a devious man by nature, but when you're unarmed, your tactics might gonna be downright Archimedean.",
             "image": "https://m.media-amazon.com/images/M/MV5BYjRkYTI3M2EtZWQ4Ny00OTA2LWFmMTMtY2E4MTEyZmNjOTMxXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # LOTR
            {"movie": "The Lord of the Rings: The Return of the King [2003]", "character": "Aragorn",
             "quote": "Hold your ground, hold your ground! Sons of Gondor, of Rohan, my brothers! I see in your eyes "
                      "the same fear that would take the heart of me. A day may come when the courage of men fails, "
                      "when we forsake our friends and break all bonds of fellowship, but it is not this day. An hour "
                      "of wolves and shattered shields, when the age of men comes crashing down! But it is not this "
                      "day! This day we fight! By all that you hold dear on this good Earth, I bid you *stand, "
                      "Men of the West!*",
             "image": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lord of the Rings: The Return of the King [2003]", "character": "Gimli",
             "quote": "Certainty of death. Small chance of success. What are we waiting for?",
             "image": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lord of the Rings: The Return of the King [2003]",
             "quote": "**Gimli:** Never thought I'd die fighting side by side with an Elf\n"
                      "**Legolas:** What about side by side with a friend?\n"
                      "**Gimli:** Aye, I could do that",
             "image": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lord of the Rings: The Return of the King [2003]",
             "quote": "**Sam:** Do you remember the Shire, Mr. Frodo? It'll be spring soon. And the orchards will be "
                      "in blossom. And the birds will be nesting in the hazel thicket. And they'll be sowing the "
                      "summer barley in the lower fields... and eating the first of the strawberries with cream. Do "
                      "you remember the taste of strawberries?\n"
                      "**Frodo:** No, Sam. I can't recall the taste of food... nor the sound of water... nor the "
                      "touch of grass. I'm... naked in the dark, with nothing, no veil... between me... and the wheel "
                      "of fire! I can see him... with my waking eyes!\n"
                      "**Sam:** Then let us be rid of it... once and for all! Come on, Mr. Frodo. I can't carry it for you... but I can carry you!",
             "image": "https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            # BACK TO THE FUTURE
            {"movie": "Back to the Future [1985]", "character": "George McFly",
             "quote": "Last night, Darth Vader came down from Planet Vulcan and told me that if I didn't take Lorraine out, that he'd melt my brain.",
             "image": "https://static.posters.cz/image/750/plakater/back-to-the-future-i2795.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Back to the Future [1985]",
             "quote": "**Marty McFly:** Whoa. Wait a minute, Doc. Are you trying to tell me that my mother has got the hots for me?\n"
                      "**Dr.Emmett Brown:** Precisely\n"
                      "**Marty McFly:** Whoa, this is heavy\n"
                      "**Dr.Emmett Brown:** There's that word again. \"Heavy.\" Why are things so heavy in the "
                      "future? Is there a problem with the Earth's gravitational pull?",
             "image": "https://static.posters.cz/image/750/plakater/back-to-the-future-i2795.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            # THE LION KING
            {"movie": "The Lion King [1994]",
             "quote": "**Adult Simba:** I know what I have to do. But going back means I'll have to face my past. I've been running from it for so long.\n"
                      "[Rafiki hits Simba on the head with his stick]\n"
                      "**Adult Simba:** Ow! Jeez, what was that for?\n"
                      "**Rafiki:** It doesn't matter. It's in the past.\n"
                      "**Adult Simba:** Yeah, but it still hurts.\n"
                      "**Rafiki:** Oh yes, the past can hurt. But from the way I see it, you can either run from it, or... learn from it.\n"
                      "[swings his stick again at Simba, who ducks out of the way]\n"
                      "**Rafiki:** Ha. You see? So what are you going to do?\n"
                      "**Adult Simba:** First, I'm gonna take your stick.\n"
                      "**Rafiki:** No, no, no, no, not the stick! Hey, where you going?\n"
                      "**Adult Simba:** I'm going back!\n"
                      "**Rafiki:** Good! Go on! Get out of here!",
             "image": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_FMjpg_UX1000_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lion King [1994]",
             "quote": "**Mufasa:** Everything you see exists together in a delicate balance. As king, you need to "
                      "understand that balance and respect all the creatures, from the crawling ant to the leaping "
                      "antelope.\n"
                      "**Young Simba:** But, Dad, don't we eat the antelope?\n"
                      "**Mufasa:** Yes, Simba, but let me explain. When we die, our bodies become the grass, "
                      "and the antelope eat the grass. And so we are all connected in the great Circle of Life.",
             "image": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_FMjpg_UX1000_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lion King [1994]",
             "quote": "**Timon:** Gee. He looks blue\n"
                      "**Pumbaa:** I'd say brownish-gold.\n"
                      "**Timon:** No, no, no. I mean he's depressed.",
             "image": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_FMjpg_UX1000_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Lion King [1994]",
             "quote": "**Pumbaa:** You know, kid, in times like this my buddy Timon here says \"you got to put your behind in your past.\"\n"
                      "**Timon:** No, no, no. Amateur. Lie down before you hurt yourself. It's \"You got to put your past behind you.\"",
             "image": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_FMjpg_UX1000_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            # FIGHT CLUB
            {"movie": "Fight Club [1999]", "character": "Tyler Durden",
             "quote": "Man, I see in fight club the strongest and smartest men who've ever lived. I see all this "
                      "potential, and I see squandering. God damn it, an entire generation pumping gas, "
                      "waiting tables; slaves with white collars. Advertising has us chasing cars and clothes, "
                      "working jobs we hate so we can buy shit we don't need. We're the middle children of history, "
                      "man. No purpose or place. We have no Great War. No Great Depression. Our Great War's a "
                      "spiritual war... our Great Depression is our lives. We've all been raised on television to "
                      "believe that one day we'd all be millionaires, and movie gods, and rock stars. But we won't. "
                      "And we're slowly learning that fact. And we're very, very pissed off.",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Fight Club [1999]", "character": "Tyler Durden",
             "quote": "Listen up, maggots. You are not special. You are not a beautiful or unique snowflake. "
                      "You're the same decaying organic matter as everything else.",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Fight Club [1999]", "character": "Tyler Durden",
             "quote": "You're not your job. You're not how much money you have in the bank. You're not the car you "
                      "drive. You're not the contents of your wallet. You're not your fucking khakis. You're the "
                      "all-singing, all-dancing crap of the world.",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Fight Club [1999]", "character": "Tyler Durden",
             "quote": "Gentlemen, welcome to Fight Club. The first rule of Fight Club is: you do not talk about Fight "
                      "Club. The second rule of Fight Club is: you DO NOT talk about Fight Club! Third rule of Fight "
                      "Club: someone yells \"stop!\", goes limp, taps out, the fight is over. Fourth rule: only two "
                      "guys to a fight. Fifth rule: one fight at a time, fellas. Sixth rule: No shirts, "
                      "no shoes. Seventh rule: fights will go on as long as they have to. And the eighth and final "
                      "rule: if this is your first time at Fight Club, you have to fight.",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "Fight Club [1999]", "character": "Tyler Durden",
             "quote": "It could be worse. A woman could cut off your penis while you're sleeping and toss it out the window of a moving car.",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": True}
             },
            {"movie": "Fight Club [1999]", "character": "Narrator",
             "quote": "You wake up at Seatac, SFO, LAX. You wake up at O'Hare, Dallas-Fort Worth, BWI. Pacific, "
                      "mountain, central. Lose an hour, gain an hour. This is your life, and it's ending one minute "
                      "at a time. You wake up at Air Harbor International. If you wake up at a different time, "
                      "in a different place, could you wake up as a different person?",
             "image": "https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            # THE WOLF OF WALL STREET
            {"movie": "The Wolf Of Wall Street [2013]", "character": "Jordan Belfort",
             "quote": "Let me tell you something. There's no nobility in poverty. I have been a rich man and I have "
                      "been a poor man. And I choose rich every fuckin' time. Because, at least as a rich man, "
                      "when I have to face my problems, I show up in the back of the limo, wearing a $2000 suit and a "
                      "$40,000 gold fuckin' watch.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Wolf Of Wall Street [2013]", "character": "Jordan Belfort",
             "quote": "I fucked her brains out... for eleven seconds.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": True}
             },
            {"movie": "The Wolf Of Wall Street [2013]",
             "quote": "**Jordan Belfort:** Brad, show them how it's done. Sell me that pen. Watch. Go on.\n"
                      "**Brad:** You want me to sell you this fucking pen?\n"
                      "**Jordan Belfort:** That's my boy right there. Can fucking sell anything.\n"
                      "**Brad:** Why don't you do me a favor. Write your name down on that napkin for me.\n"
                      "**Jordan Belfort:** I don't have a pen.\n"
                      "**Brad:** Exactly. Supply and demand, my friend.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Wolf Of Wall Street [2013]",
             "quote": "**Jordan Belfort:** People say shit... I mean like, you married your cousin or some stupid shit.\n"
                      "**Donnie Azoff:** Yeah, my wife is my cousin or whatever, but it's not like what you think.\n"
                      "**Jordan Belfort:** Is she like, a first cousin?\n"
                      "**Donnie Azoff:** Her father is the brother of my mom. Like, we grew up together, and she grew "
                      "up hot, you know, she fucking grew up hot. And all my friends are trying to fuck her, "
                      "you know, and I'm not gonna let one of these assholes fuck my cousin. So I used the cousin "
                      "thing, as like, an in with her. I'm not like, gonna let someone else fuck my cousin, "
                      "you know? If anyone's gonna fuck my cousin, it's gonna be me. Out of respect.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": True}
             },
            {"movie": "The Wolf Of Wall Street [2013]", "character": "Jordan Belfort",
             "quote": "An I.P.O. is an initial public offering. It's the first time a stock is offered for sale to "
                      "the general population. Now as the firm taking the company public, we set the initial sales "
                      "price then sold those shares right back to our friends. Yet...\n"
                      "Look, I know you're not following what I'm saying anyway, right? That's... that's okay, "
                      "that doesn't matter. The real question is this: was all this legal? Absolutely fucking not. "
                      "But we were making more money than we knew what do with.",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Wolf Of Wall Street [2013]", "character": "Jordan Belfort",
             "quote": "So you listen to me and you listen well. Are you behind on your credit card bills? Good, "
                      "pick up the phone and start dialing! Is your landlord ready to evict you? Good! Pick up the "
                      "phone and start dialing! Does your girlfriend think you're a fucking worthless loser? Good! "
                      "Pick up the phone and start dialing! I want you to deal with your problems by becoming rich!",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "quote", "flags": {"Explicit": False, "NSFW": False}
             },
            {"movie": "The Wolf Of Wall Street [2013]",
             "quote": "**Donnie Azoff:** I check my messages every day when I come home from work... my answering "
                      "machine... zero! I got a blinkling light because I don't have shit from you. I got my wife... "
                      "I got my wife checking the messages every forty-five minutes calling the office saying. \"Has "
                      "Brad apologized yet? Is there an apology message on the machine?\" I don't have jack-shit. You "
                      "know what? That's not how you treat people.\n"
                      "**Brad:** You gotta be a fucking pal... You know what, I'm gonna give you a fucking pass, just give me the case.\n"
                      "**Donnie Azoff:** You're gonna give me a pass?\n"
                      "**Brad:** Look, it's a figure of fucking speech, just give me the fucking...\n"
                      "**Donnie Azoff:** Oh my God, the emperor of Fucksville came down from Fucksville to give me a "
                      "pass! Hey, what are the citizens of Fucksville doing today when their emperor's gone? Is it, "
                      "is it mayhem? Are people looting and raping? What are all the little fuckheads doing while "
                      "you're here?",
             "image": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg",
             "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
             },
            # Quote template
            # {"movie": "", "character": "",
            # "quote": "",
            # "image": "",
            # "type": "quote", "flags": {"Explicit": False, "NSFW": False}
            #  },
            # Dialogue template
            # {"movie": "",
            #  "quote": "",
            #  "image": "",
            #  "type": "dialogue", "flags": {"Explicit": False, "NSFW": False}
            #  },
        ]
        id = 1
        for item in mq:
            item['id'] = id
            id += 1
        return mq

    @staticmethod
    async def random(explicitFilter: bool = True, nsfwFilter: bool = False) -> dict:
        mq = await moviequotes.movielist()
        if explicitFilter is True or nsfwFilter is True:
            loop = True
            while loop == True:
                loop = False
                randChoice = random.choice(mq)
                explicit = randChoice["flags"]["Explicit"]
                nsfw = randChoice["flags"]["NSFW"]
                if explicitFilter is True and explicit is True:
                    loop = True
                if nsfwFilter is True and nsfw is True:
                    loop = True
        else:
            randChoice = random.choice(mq)
        return randChoice

    @staticmethod
    async def get(ID: int, explicitFilter: bool = True, nsfwFilter: bool = False) -> dict:
        mq = await moviequotes.movielist()
        num = ID - 1
        quote = mq[num]
        explicit = quote["flags"]["Explicit"]
        nsfw = quote["flags"]["NSFW"]
        if explicitFilter is True and explicit is True:
            quote = {"movie": "Explicit Filter", "character": "",
                     "quote": "This quote is explicit and the Explicit Filter is turned on\nTry another one",
                     "image": "",
                     "type": "quote", "id": "Contact PPT/BlackFinix/Giraffe if you think theres been a mistake"}
        if nsfwFilter is True and nsfw is True:
            quote = {"movie": "NSFW Filter", "character": "",
                     "quote": "This quote is not safe for work and the NSFW Filter is turned on\nTry another one",
                     "image": "",
                     "type": "quote", "id": "Contact PPT/BlackFinix/Giraffe if you think theres been a mistake"}
        return quote

    @staticmethod
    async def per(Type: str, Regex: str, explicitFilter: bool = True, nsfwFilter: bool = False) -> dict:
        mq = await moviequotes.movielist()
        Type = Type.lower()
        choices = []
        for item in mq:
            if reg.search(pattern=Regex, string=item[Type], flags=reg.I):
                choices.append(item)
        if explicitFilter is True or nsfwFilter is True:
            for item in choices:
                explicit = item["flags"]["Explicit"]
                nsfw = item["flags"]["NSFW"]
                if explicitFilter is True and explicit is True:
                    choices.remove(item)
                elif nsfwFilter is True and nsfw is True:
                    choices.remove(item)
        return random.choice(choices)

    @staticmethod
    async def search(String: str) -> dict:
        pass

async def loadingFunnyMessages(StartMsg: str = "Please wait,") -> str:
    """
    This is just a dum randomized loading message cause why not
    :param StartMsg: The start of the loading string
    :return: Full string
    """

    loading_message_end = [
    "reticulating splines",
    "generating witty dialog",
    "swapping time and space",
    "spinning violently around the y-axis",
    "tokenizing real life",
    "bending the spoon",
    "filtering morale",
    "the architects are still drafting",
    "the bits are breeding",
    "we're building the buildings as fast as we can",
    "and pay no attention to the man behind the curtain",
    "and enjoy the elevator music",
    "the little elves is drawing your map",
    "a few bits tried to escape",
    "checking the gravitational constant in your locale",
    "you're not in Kansas any more",
    "the server is powered by a lemon and two electrodes",
    "we're testing your patience",
    "as if you had any other choice",
    "and follow the white rabbit",
    "why don't you order a sandwich??",
    "the satellite is moving into position",
    "the bits are flowing slowly today",
    "it's still faster than you could draw it",
    "the last time I tried this the monkey didn't survive",
    "i should have had a V8 this morning",
    "testing on Timmy... We're going to need another Timmy",
    "reconfoobling energymotron",
    "Just count to 10",
    "counting backwards from Infinity",
    "Embiggening Prototypes",
    "so do you come here often??",
    "we're making you a cookie",
    "creating time-loop inversion field",
    "spinning the wheel of fortune",
    "loading the enchanted bunny",
    "computing chance of success",
    "looking for exact change",
    "all I really need is a kilobit",
    "what do you call 8 Hobbits? A Hobbyte",
    "should have used a compiled language",
    "adjusting flux capacitor",
    "until the sloth starts moving",
    "don't break your screen yet",
    "i swear it's almost done",
    "let's take a mindfulness minute",
    "unicorns are at the end of this road, I promise",
    "listening for the sound of one hand clapping",
    "keeping all the 1's and removing all the 0's",
    "putting the icing on the cake...",
    "cleaning off the cobwebs",
    "making sure all the i's have dots",
    "we need more dilithium crystals",
    "connecting Neurotoxin Storage Tank",
    "granting wishes",
    "get some coffee and come back in ten minutes",
    "spinning the hamster",
    "be careful not to step in the git-gui",
    "convincing AI not to turn evil..",
    "how did you get here",
    "wait... do you smell something burning",
    "computing the secret to life, the universe, and everything",
    "when nothing is going right, go left!!",
    "i’ve got problem for your solution",
    "constructing additional pylons",
    "roping some seaturtles",
    "locating Jebediah Kerman",
    "we are not liable for any broken screens as a result of waiting",
    "have you tried turning it off and on again??",
    "if you type Google into Google you can break the internet",
    "well, this is embarrassing",
    "hello, IT... Have you tried forcing an unexpected reboot??",
    "they just toss us away like yesterday's jam",
    "paint is drying",
    "dividing by zero...",
    "if I’m not back in five minutes, just wait longer",
    "we’re going to need a bigger boat",
    "web developers do it with <style>",
    "i need to git pull --my-life-together",
    "cracking military-grade encryption",
    "simulating traveling salesman",
    "proving P=NP",
    "entangling superstrings",
    "twiddling thumbs",
    "searching for plot device",
    "trying to sort in O(n)",
    "sending data to NS-i mean, our servers",
    "looking for sense of humour",
    "converting a bug into a feature",
    "winter is coming",
    "installing dependencies",
    "distracted by cat gifs",
    "finding someone to hold my beer",
    "#todo Insert witty loading message",
    "let's hope it's worth the wait",
    "ordering 1s and 0s",
    "updating dependencies",
    "consulting the manual",
    "loading funny message",
    "feel free to spin in your chair",
    "go ahead, hold your breath and do an ironman plank till loading complete",
    "help, I'm trapped in a loader!",
    "we're purging the Decepticons",
    "Mining some bitcoins",
    "downloading more RAM",
    "updating to Windows Vista",
    "deleting System32",
    "Alt-F4 speeds things up",
    "initializing the initializer",
    "optimizing the optimizer",
    "running swag sticker detection",
    "shovelling coal into the server",
    "pushing pixels",
    "how about this weather, eh??",
    "building a wall",
    "updating updater",
    "downloading downloader",
    "debugging debugger",
    "reading Terms and Conditions",
    "deleting all your hidden porn",
    "running with scissors",
    "you may call me Steve",
    "discovering new ways of making you wait",
    "sooooo... Have you seen my vacation photos yet??",
    "catching em' all",
    "#todo Insert elevator music",
    "still faster than Windows update",
    "grabbing extra minions",
    "waking up the minions",
    f"you are number {str(random.randint(1000,10000))} in the queue",
    "feeding unicorns",
    ]
    return f"{StartMsg} {random.choice(loading_message_end)}..."
