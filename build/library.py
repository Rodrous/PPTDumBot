import random
"""
Feel free to add as many moviequotes as you want, if there is no character or image leave it blank but dont remove it
"""
async def moviequotes():
    mq = [
        {"movie": "Dirty Harry [1971]", "character": "Harry", "quote": "You've got to ask yourself one question; Do you feel lucky? well, do ya, punk?", "image": "https://prod.cdn.bbaws.net/TDC_Blockbuster_-_Production/79/16/WB-0008_po-reg-medium_orig.jpg"},
        {"movie": "The Godfather [1972]", "character": "Don Vito Corleone", "quote": "I'm gonna make him an offer he cant refuse", "image": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"},
        {"movie": "Psycho[1960]", "character": "", "quote": "A boy's best friend is his mother", "image": "https://tuploads.s3.eu-west-1.amazonaws.com/production/uploads/event/image/107693/default_5404___7979721490.jpg"},
        # {"movie": "", "character": "", "quote": "", "image": ""},
    ]
    return random.choice(mq)