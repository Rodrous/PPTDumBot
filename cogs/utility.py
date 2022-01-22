from discord.ext import commands
import discord,os, requests
import re as reg
from general.generalPurpose import Dumbot, get_data_from_link
from general import checks
from general import notion
from general.library import loadingFunnyMessages

allowedguilds = [os.environ.get('allowedGuild')]

restrictedChannels = ["database"]

class syscom(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    #YOOOOOO

    @commands.command(
        name='ping',
        brief='Pong',
        help='Returns the delay of the bot')
    async def ping(self,msg):
        embed = discord.Embed()
        embed.add_field(name="Pong", value=f"{round(self.bot.latency * 1000)}ms")
        await msg.send(embed=embed)

    # ------------------------------------------------------------------------------

    @commands.command(
        name = 'steal',
        brief = 'FBI OPEN UP',
        help = 'Yoink an emoji, with the given name or the emoji name')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_emojis = True)
    @commands.has_permissions(manage_emojis=True)
    async def stealEmoji(self, ctx, *, args = ''):
        #gLimit = ctx.guild.emoji_limit
        #gCurr = len(await ctx.guild.fetch_emojis())
        #print(str(gCurr)+'/'+str(gLimit)+' emojis')
        # if gCurr >= gLimit:
        #         return await ctx.send("This server is already at the limit and cant have more emojis **):**\n(If you think this is an error,contact Blackfinix/EvilGiraffes/PPT)")
        turl = 'https://cdn.discordapp.com/emojis/'
        if args == '':
            return await ctx.send("No emoji or link detected.")
        try:
            msg = args.split()
            if reg.match(pattern='https://cdn.discordapp.com/emojis/', string=msg[0]):
                data = await get_data_from_link(link=str(msg[0]), fileName='WhyAreYouLookingAtThis')
                name = '_'.join(msg[1:]) or 'RandomName'
                newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

            else:
                if reg.match(pattern='<a?:.*:\d*>',string=msg[0]):
                    name = '_'.join(msg[1:]) or (''.join(reg.findall(pattern='(?<=:)[a-zA-Z1-9~_]*(?=:)', string=msg[0])))
                else:
                    return await ctx.send("Wrong Input detected. Not an emoji.")

                eid = int(''.join(reg.findall(pattern='(?<=:)\d*(?=>)', string=msg[0])))

                if reg.match(pattern='<a:',string=msg[0]) is not None:
                    turl += str(eid) + '.gif'
                else:
                    turl += str(eid) + '.png'
                    #url = f"https://cdn.discordapp.com/emojis/853662523843674112.png"

                data = await get_data_from_link(link=turl, fileName="WhyAreYouLookingAtThis")

                newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

        except Exception as e:
                print(f"There is some Error Here, error is defined by: {e}")
                await Dumbot.send_error_to_channel(self, ctx, "Steal", e)
                await ctx.send("Some error occured, please try again or ping the devs **):**")
    
    # ------------------------------------------------------------------------------

    @checks.feedback_n_bug_blacklist()
    @commands.command(
        name="feedback",
        aliases= ["fb"])
    async def feedBack(self,ctx,*,args):
        loading_msg = await loadingFunnyMessages()
        msg = await ctx.send(loading_msg)
        headers, post_content = await notion.feedback_n_bugs_json(ctx, str(args), selectName="Feedback")
        post_url = "https://api.notion.com/v1/pages"
        response = requests.post(url=post_url, headers=headers, json=post_content)
        if response.status_code == 200:
            await msg.edit(content="Feedback sent!")
        else:
            await msg.edit(content="Something happened, please try again or contact staff")

    # ------------------------------------------------------------------------------

    @checks.feedback_n_bug_blacklist()
    @commands.command(
        name="bugreport",
        aliases=["bugs", "bugrep", "bug-report", "bug-rep"])
    async def bugReport(self, ctx, *, args):
        loading_msg = await loadingFunnyMessages()
        msg = await ctx.send(loading_msg)
        headers, post_content = await notion.feedback_n_bugs_json(ctx, str(args), selectName="Bugs")
        post_url = "https://api.notion.com/v1/pages"
        response = requests.post(url=post_url, headers=headers, json=post_content)
        if response.status_code == 200:
            await msg.edit(content="Bug Report sent!")
        else:
            await msg.edit(content="Something happened, please try again or contact staff")

    # ------------------------------------------------------------------------------

    @commands.Cog.listener()
    async def on_message(self, msg):
        # Cross channel message linking command
        ctx = msg.channel
        crossChannelLinkRegex = reg.compile(r"https://discord.com/channels/(\d*)/(\d*)/(\d*)")
        if matches := reg.match(pattern=crossChannelLinkRegex, string=msg.content):
            args = msg.content.split()
            messageLink = matches[0]
            channelid = int(matches[2])
            messageid = int(matches[3])
            fetchedMessage = await commands.Bot.get_channel(self.bot, channelid).fetch_message(messageid)
            fetchedAuthor = fetchedMessage.author
            messageAuthor = msg.author
            pfp = fetchedAuthor.avatar
            sameGuild = msg.guild.id == fetchedMessage.guild.id
            if len(args) <= 1 and sameGuild:
                await ctx.purge(limit=1)
            if fetchedMessage.embeds and sameGuild:
                fetchedEmbed = fetchedMessage.embeds[0]
                info = discord.Embed(description= f"[Embed Link]({messageLink})")
                info.set_author(name=fetchedAuthor, icon_url=pfp)
                info.set_footer(text=f"Triggered by: {messageAuthor}", icon_url=messageAuthor.avatar)
                await ctx.send(embed=fetchedEmbed)
                await ctx.send(embed=info)
            elif sameGuild:
                description = f"[Message]({messageLink}) **in** {msg.channel.mention}\n{fetchedMessage.content}"
                embed = discord.Embed(description=description)
                embed.set_author(name=fetchedAuthor, icon_url=pfp)
                embed.set_footer(text=f"Triggered by: {messageAuthor}", icon_url=messageAuthor.avatar)
                await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(syscom(bot))