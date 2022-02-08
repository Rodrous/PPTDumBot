import random
import requests
from bs4 import BeautifulSoup


def searchitem(item) -> str:
    url: str = f"https://www.urbandictionary.com/define.php?term={item}"
    request = requests.get(url).content
    soupObj: BeautifulSoup = BeautifulSoup(request, features='html.parser')
    try:
        meaning = soupObj.find('div', class_="meaning").text
        return meaning
    
    except Exception as e:
        return "This word doesn't exist in Database"


def randomword() -> str:
    number: int = random.randint(1, 1000)
    url: str = f"https://www.urbandictionary.com/define.php?term={number}"
    request = requests.get(url).content
    soupObj: BeautifulSoup = BeautifulSoup(request, features='html.parser')
    try:
        word: str = soupObj.find('a', class_="word").text
        meaning: str = soupObj.find('div', class_="meaning").text
        
        return f"{word}:{meaning}"
    
    
    except Exception as e:
        return "Something Happened"
