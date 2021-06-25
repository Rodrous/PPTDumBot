import discord
from discord.ext import commands
import aiohttp
import requests
import io
import base64
import random

with open("client.txt") as file:
    f = file.readline()

id = base64.b64decode(f).decode('utf-8') 
#client = discord.Client()               # This will be deprecated soon enough.
restrictedChannels = ["database"]

customPrefix = {}
defaultPrefix = ['!']


bot = commands.Bot(command_prefix='!')  # This is the same as a client initialization, but bot has more functionalities.

@bot.command()
async def hello(ctx,*,arg):
    await ctx.send(arg)


if __name__ == "__main__":
    bot.run(id)
