import random
"""
Feel free to add as many moviequotes as you want, if there is no character leave it blank but dont remove it
"""
async def moviequotes():
    mq = [
        {"movie": "Dirty Harry [1971]", "character": "Harry", "quote": "You've got to ask yourself one question; Do you feel lucky? well, do ya, punk?"},
        {"movie": "The Godfather [1972]", "character": "Don Vito Corleone", "quote": "I'm gonna make him an offer he cant refuse"},
        {"movie": "Psycho[1960]", "character": "", "quote": "A boy's best friend is his mother"},
        # {"movie": "", "character": "", "quote": ""},
    ]
    return random.choice(mq)