import random
async def moviequotes():
    mq = [
        {"movie": "Dirty Harry [1971]", "character": "Harry", "quote": "You've got to ask yourself one question; Do you feel lucky? well, do ya, punk?"},
        {"movie": "The Godfather", "character": "Don Vito Corleone", "quote": "I'm gonna make him an offer he cant refuse"},
        # {"movie": "", "character": "", "quote": ""},
    ]
    return random.choice(mq)