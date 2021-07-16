# PPTDumBot

## Things to keep in mind

- DO NOT make any changes to the `Procfile` or to `client`
- requirements will consist of all the external libraries you would use.
- Code is messy, i will soon implement DRY, so it will be bit better to read.
- The only thing needed to be edited is the `dumdiscord.py` script and whatever is in cogs

---

## How to Add Emojis?
There are 2 ways.

- 1)

  Go [here](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjIjuWghq3xAhXEwzgGHWAiDvkQFnoECAQQAw&url=https%3A%2F%2Funicode.org%2Femoji%2Fcharts%2Ffull-emoji-list.html&usg=AOvVaw2Y8ixSqM60XYhs6auuOUsB), copy the unicode

  replace “+” with “000” 

  ![PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled.png](PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled.png)

  For example :

  “U+1F911” will become “U0001F911” and add a `\` in front of it before printing.

  ![PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled%201.png](PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled%201.png)

- 2)

  Having 'Developer Mode' enabled for discord, right click the emoji you want and copy its ID.
  To make the bot print it, use this format : 
  `(<:emojiName:emojiID>)`
  If your emoji is animated, you just need to add one thing to the string :
  `(<a:emojiName:emojiID>)`


## Confused on how to make PRs?

See this [video](https://www.youtube.com/watch?v=rgbCcBNZcdQ) or read [this](https://scotch.io/tutorials/creating-your-first-pull-request-in-github) article.

Github cheatsheet: [Git CheatSheet](https://www.notion.so/Git-CheatSheet-914296aee4fc4003b9ae19f3de598ba5) 

---

![PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled%202.png](PPTDumBot%2017652a0bcf3846aca49dc48d4229374d/Untitled%202.png)
