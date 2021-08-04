import requests,random
from bs4 import BeautifulSoup


def searchitem(item):
    url = f"https://www.urbandictionary.com/define.php?term={item}"
    request = requests.get(url).content
    soupObj = BeautifulSoup(request, features='html.parser')
    try:
        meaning = soupObj.find('div',class_="meaning").text

        return meaning

    except Exception:
        return "This word doesn't exist in database"


def randomword():
    number = random.randint(1,1000)
    url = f"https://www.urbandictionary.com/define.php?term={number}"
    request = requests.get(url).content
    soupObj = BeautifulSoup(request, features='html.parser')
    try:
        word = soupObj.find('a',class_ = "word").text
        meaning = soupObj.find('div', class_="meaning").text

        return f"{word}:{meaning}"


    except Exception:
        return "Something Happened"


