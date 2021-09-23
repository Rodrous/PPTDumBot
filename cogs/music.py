import discord
from discord.ext import commands
import youtube_dl
from build.generalPurpose import dumbot


class music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="join")
    async def hopinvc(self,ctx):
        try:
            channel = ctx.author.voice.channel
            print(channel)
            if channel:
                await channel.connect()

            else:
                await ctx.send("I am already in a channel")
        except Exception as e:
            print(e)

    @commands.command(name="leave")
    async def leave(self,ctx):
        if ctx.voice_client :
            await ctx.voice_client.disconnect()

    @commands.command(name = "play")
    async def play(self,ctx,url):
        if ctx.voice_client is None:
            await self.hopinvc(ctx)
        ctx.voice_client.stop()
        ffmpeg_options = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        ydl_options = {'format':'bestaudio'}

        try:
            with youtube_dl.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**ffmpeg_options)
                ctx.voice_client.play(source)
        except Exception as e:
            print(e)

    @commands.command(name="pause")
    async def pause(self, ctx):
        if (ctx.voice_client):
            await ctx.voice_client.pause()

    @commands.command(name="resume")
    async def resume(self, ctx):
        if (ctx.voice_client):
            await ctx.voice_client.resume()

def setup(bot):
    bot.add_cog(music(bot))