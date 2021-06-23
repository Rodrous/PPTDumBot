import discord
import aiohttp
import requests
import io
import base64
import random

with open("client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8')
client = discord.Client()
channels_to_send = ["database"]
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Your Mum.'))
@client.event
async def on_message(message):

    if str(message.channel) not in channels_to_send: 
     # Everything Working from Down here
        if message.content.lower() == "!quote":
            url = requests.get('https://animechan.vercel.app/api/random').json()
            await message.channel.send(f"A quote from {url['character']} : {url['quote']}")

        if message.content.lower() == "!cat":
            get_image_url = requests.get(f"https://aws.random.cat/meow").json()
            url = get_image_url['file']
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return await message.channel.send("Couldn't download the file")
                    data = io.BytesIO(await response.read())
                    await message.channel.send("From PPT with \U0001F49A")
                    await message.channel.send(file=discord.File(data,"Cat.png"))
        removed_stuff = ['!waifu','nsfw-fu','wamen']
        if message.content.lower() in removed_stuff:
            await message.channel.send("Functionaliy Removed, will be added in Dumbot1.1")

        if message.content.lower() == "!dog":
            get_image_url = requests.get(f"https://dog.ceo/api/breeds/image/random").json()
            url = get_image_url['message']
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return await message.channel.send("Couldn't download the file")
                    data = io.BytesIO(await response.read())
                    await message.channel.send("From PPT with \U0001F49A")
                    await message.channel.send(file=discord.File(data,"dog.png"))

        if message.content.lower() == "!ree":
            num = random.randint(1,100)
            await message.channel.send("*R"+"E"*num + "*")

        if message.content.lower() == "!help":
            embed = discord.Embed(title="Bot help perhaps", description="Some useful commands")
            embed.add_field(name="!ree", value="Rees out of frustration")
            embed.add_field(name="!s", value="Sends a Random image from internet [1920x1080]")
            embed.add_field(name= "!cat", value = "Sends a Cat pic \U0001F408")
            embed.add_field(name= "!quote", value = "Sends a random anime quote!")
            embed.add_field(name= "!invite", value = "Sends 'add bot to server' link")
            embed.add_field(name= "!dog", value="Get a Dog pic \U0001F436")
            await message.channel.send(content=None, embed=embed)

        if message.content.lower() == "!clear":
            await message.channel.purge(limit=1)
            await message.channel.send("Command Depricated UwU")
        if message.content.lower() == "!s":
            url = f"https://picsum.photos/1920/1080"
            async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status != 200:
                            return await message.channel.send("Couldn't download the file..")
                        data = io.BytesIO(await response.read())
                        await message.channel.send(file=discord.File(data,"Some Image.png"))
        if message.content.lower() == "!invite":
            await message.channel.send("This was a mistake")
            await message.channel.send("<https://discordapp.com/oauth2/authorize?client_id=852977382016024646&scope=bot&permissions=0>")

if __name__ == "__main__":
    client.run(id)
