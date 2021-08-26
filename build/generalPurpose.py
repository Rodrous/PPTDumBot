from discord.ext.commands import bot
import requests,aiohttp,io, datetime
import discord, base64
from discord.ext import commands


async def getDataFromLink(url:str, json:bool=False, jsonType:str='', returnFile:bool=False, fileName:str='aRandomName.png'):
    link = url
    if json:
        imageUrl = requests.get(url).json()
        link = imageUrl[jsonType]
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            if response.status != 200:
                return None
            data = io.BytesIO(await response.read())
            if returnFile:
                return discord.File(data,fileName)
            return data

class dumbot:

    @staticmethod
    async def getPrefix(msg, bot, string:bool=False):
        # Returns the prefix...
        tp = await bot.get_prefix(msg)
        if string:
            return ' or '.join(tp[1:]) # ...either in a string as : "@PPTDumbBot or $"...
        return tp # ...or as a List type

    @staticmethod
    #todo make this actually find the bot av url and make it async, remember to uncuck it in help menues
    def avatar():
        return 'https://cdn.discordapp.com/avatars/852977382016024646/12f7f96521114553fc7f4b2766dd086f.png?size=2048'

    async def sendErrorToChannel(self, ctx, commandName: str, error : Exception):
        """
        :param self: self.bot
        :param ctx: context
        :param error: exception
        :return:
        """
        errorChannelID = 879773094561083492
        embed = discord.Embed(title="Error log",description=f"Command error was raised in: **{commandName}**" ,timestamp=datetime.datetime.now(),color=13524060)
        embed.add_field(name="Guild", value=ctx.guild, inline=True)
        embed.add_field(name="Channel", value=ctx.channel.mention, inline=True)
        embed.add_field(name="Channel ID", value=ctx.channel.id, inline=True)
        embed.add_field(name="Author Name", value=ctx.author, inline=True)
        embed.add_field(name="Author", value=ctx.author.mention, inline=True)
        embed.add_field(name="Author ID", value=ctx.author.id, inline=True)
        embed.add_field(name="In Message", value=ctx.message.content, inline=False)
        embed.add_field(name="Error", value=error, inline=False)
        await commands.Bot.get_channel(self.bot, errorChannelID).send(embed=embed)