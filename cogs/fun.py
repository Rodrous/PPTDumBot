import asyncio
import random
import re as reg

import discord
import requests
import wikipedia
from discord.ext import commands

from api.animeQuote import AnimeQuote
from api.jokeApi.argsHandler import ArgsHandler as JokeArgsHandler
from api.jokeApi.jokeApi import JokeApi, Config
from api.jokeApi.url import BuildRequestUrl
from general import colors
from general.errors import ApiError
from general.generalPurpose import Dumbot, get_data_from_link
from general.loadingMessages import sendLoadingMessage
from general.movieQuotes import ArgsHandler as MqArgsHandler
from general.movieQuotes import MovieQuotes
from general.urbanDict import searchitem

CATEGORY_EMBED_COLOR = colors.Category.FUN_GREEN


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="cat"
    )
    async def sendCat(self, ctx: commands.Context):
        await ctx.send("Command Disabled Until Further Update")

    @commands.command(
        name="dog"
    )
    async def sendDog(self, ctx: commands.Context):
        data = await get_data_from_link(link="https://dog.ceo/api/breeds/image/random", json=True, jsonType='message',
                                        returnFile=True, fileName='Dog.png')
        if data:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(content="From PPT with \U0001F49A", file=data)

    @commands.command(
        name="wallpaper"
    )
    async def sendWallpaper(self, ctx: commands.Context):
        data = await get_data_from_link(link="https://picsum.photos/1920/1080", returnFile=True,
                                        fileName='Why are you looking at this.png')
        if data:
            return await ctx.send("Couldnt Retrieve image from server.")
        await ctx.send(file=data)

    @commands.command(
        aliases=["animequote", "aq", "anime"]
    )
    async def sendQuote(self, ctx: commands.Context):
        msg = await sendLoadingMessage(ctx, embed=True, embed_color=CATEGORY_EMBED_COLOR)
        url = requests.get('https://animechan.vercel.app/api/random').json()
        anime_quote = AnimeQuote(**url)
        embed = discord.Embed(
            description=f"{anime_quote.quote}\n-{anime_quote.character}",
            color=CATEGORY_EMBED_COLOR
        )
        embed.set_author(name=anime_quote.anime)
        await msg.edit(embed=embed)

    @commands.command(
        aliases=["re", "ree", "reee", "reeee"]
    )
    async def sendRee(self, ctx: commands.Context):
        num = random.randint(10, 100)
        await ctx.send("*R" + "E" * num + "*")

    @commands.command(
        aliases=["say", "speak"]
    )
    async def repeat(self, ctx: commands.Context, *, args: str):
        if reg.search(pattern='@everyone|@here', string=args, flags=reg.I):
            await ctx.send('Fuck you, you cant loophoel dis')
            return
        await ctx.message.channel.purge(limit=1)
        await ctx.send(args)

    @commands.command(
        aliases=["yeye", "yeeyee", "yeyee", "yeeye"]
    )
    async def sendYeye(self, ctx: commands.Context):
        await ctx.send("*Y" + "E" * random.randint(10, 50) + "Y" + "E" * random.randint(10, 50) + "*")

    @commands.command(
        aliases=["joke", "getjoke", "jk"]
    )
    async def sendJoke(self, ctx: commands.Context, *, args: str = ""):
        msg: discord.Message = await sendLoadingMessage(ctx, embed=True, embed_color=CATEGORY_EMBED_COLOR)
        args_handler = JokeArgsHandler(args.lower())
        flags, categories, safe_mode = await asyncio.gather(
            args_handler.GetFlags(inverse=True),
            args_handler.GetCategories(),
            args_handler.SafeMode()
        )
        config = Config(flags, categories, safe_mode=safe_mode)
        url = await BuildRequestUrl(config)
        data = requests.get(url).json()
        try:
            joke = await JokeApi.FromJson(data)
        except ApiError as e:
            error_embed = discord.Embed(description=e)
            await msg.edit(embed=error_embed)
            return
        embed = discord.Embed(
            description=await joke.BuildJoke(),
            colour=CATEGORY_EMBED_COLOR
        )
        current_flags = f", Flags: {await joke.flags.BuildString()}" if joke.flags else ""
        embed.set_footer(text=f"Category: {joke.category.name}{current_flags}")
        await msg.edit(embed=embed)

    @commands.command(
        name="dadjoke"
    )
    async def sendDadJoke(self, ctx: commands.Context):
        msg: discord.Message = await sendLoadingMessage(ctx, embed=True, embed_color=CATEGORY_EMBED_COLOR)
        url = requests.get("https://icanhazdadjoke.com/", headers={"accept": "application/json"}).json()
        embed = discord.Embed(
            description=url["joke"],
            color=CATEGORY_EMBED_COLOR
        )
        await msg.edit(embed=embed)

    @commands.command(
        aliases=["yomomma", "yourmom", "yomom"],
        )
    async def sendMomJoke(self, ctx: commands.Context):
        msg: discord.Message = await sendLoadingMessage(ctx, embed=True, embed_color=CATEGORY_EMBED_COLOR)
        url = requests.get("https://api.yomomma.info/").json()
        embed = discord.Embed(
            description=url["joke"],
            color=CATEGORY_EMBED_COLOR
        )
        await msg.edit(embed=embed)

    @commands.command(
        name="wikipedia",
        aliases=["wiki"]
    )
    async def wikipedia(self, ctx: commands.Context, *, search: str):
        # fixme make this cleaner
        msg: discord.Message = await sendLoadingMessage(ctx)
        try:
            data = wikipedia.summary(search, sentences=7, auto_suggest=False)
            await msg.edit(content=data)
        except wikipedia.exceptions.DisambiguationError as e:
            await msg.edit(
                content="The Search is highly vague, it gave multiple outputs which I cannot send. Try Something on-point"
            )
        except Exception as e:
            await msg.edit(content="Idk what the fuck happened, ping PPT/Finix/Draf")
            await Dumbot.send_error_to_channel(self, ctx, "Wikipedia", e)

    @commands.command(
        name="dict",
        aliases=["urban", "urbandict", "define"]
    )
    async def urban(self, ctx: commands.Context, *, search: str):
        msg: discord.Message = await sendLoadingMessage(ctx)
        found = searchitem(search)
        await msg.edit(content=found)

    @commands.command(name='MovieQuotes', aliases=['mq'])
    async def movieQuote(self, ctx: commands.Context, *, args: str = "") -> None:
        # fixme improve code
        color = discord.Color.random()
        args_handler = MqArgsHandler(args.lower())
        explicit, nsfw = await asyncio.gather(
            args_handler.HasExplicit(),
            args_handler.HasNsfw()
        )
        msg = await sendLoadingMessage(ctx, embed=True, embed_color=color)
        quote = MovieQuotes(explicit, nsfw)
        try:
            await asyncio.wait_for(quote.GetMovieQuote(), timeout=10)
        except asyncio.TimeoutError:
            error_embed = discord.Embed(
                title="404: NOT FOUND",
                description="Whoops it took too long! please try again",
                color=colors.Fault.ERROR
            )
            await msg.edit(embed=error_embed)
            return
        embed = discord.Embed(
            title=quote.movie_name,
            description=quote.quote,
            color=color
        )
        character = quote.character + "\n" if quote.character != "None" else ""
        embed.set_footer(text=f"{character}Type: {quote.type}")
        embed.set_thumbnail(url=quote.image_url)
        await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
