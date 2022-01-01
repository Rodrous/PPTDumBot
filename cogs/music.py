import asyncio
import random

import discord
from discord.ext import commands
import youtube_dl
from build.generalPurpose import dumbot
from typing import List,Optional


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue: List = []

    @commands.command(name="join")
    async def hopinvc(self, ctx):
        try:
            channel = ctx.author.voice.channel

            if channel:
                await channel.connect()

            else:
                await ctx.send("I am already in a channel")
        except Exception as e:
            print(e)

    @commands.command(name="leave")
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

    @commands.command(name="play", aliases=['p'] )
    async def queueCreator(self, ctx, url) -> None:
        self.addMusic(url)
        if ctx.voice_client is None:
            await self.hopinvc(ctx)
            if self.queue:
                await self.musicPlayer(ctx,self.getMusic())
                pass

        else:
            while self.queue:
                currentUrl = self.getMusic()
                await self.musicPlayer(ctx,currentUrl)

        #Todo Make bot Leave if nothing is playing for 2 minutes

        if not ctx.voice_client.is_playing():

            await asyncio.sleep(120)
            ctx.send("Bot will leave for Now!")
            await self.leave(ctx)




    async def musicPlayer(self,ctx,url) -> None:
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        ydl_options = {'format': 'bestaudio'}

        try:
            with youtube_dl.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
                ctx.voice_client.play(source)
        except Exception as e:
            await self.leave()
            print(f"Exception -> {e}")

    def addMusic(self, url) -> None:
        self.queue.append(url)

    def getMusic(self) -> Optional[str]:
        if self.queue is not None:
            return self.queue.pop()
        else:
            return None

    @commands.command(name="pause")
    async def pause(self, ctx):
        if (ctx.voice_client):
            await ctx.voice_client.pause()

    @commands.command(name="resume")
    async def resume(self, ctx):
        if (ctx.voice_client):
            await ctx.voice_client.resume()
    
    @commands.command(name="shuffle")
    async def shuffle(self,ctx):
        random.shuffle(self.queue)
        await ctx.send(f"Shuffled {len(self.queue)} track's")

def setup(bot):
    bot.add_cog(music(bot))
