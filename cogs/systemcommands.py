from discord.ext import commands
import discord,base64,typing, requests
import re as reg
from build import generalPurpose as gp


with open("config/allowedguildIds.txt") as file:
    f = file.readlines()

allowedguilds = [base64.b64decode(i).decode('utf-8')  for i in f]

restrictedChannels = ["database"]

def Feedback_n_bug_blacklist(ctx):
    blacklist = {}
    blacklist = set(blacklist.values())
    return ctx.author.id not in blacklist

fbnbug_bl = commands.check(Feedback_n_bug_blacklist)

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

    @commands.command(
        name = 'steal',
        brief = 'FBI OPEN UP',
        help = 'Yoink an emoji, with the given name or the emoji name')
    @commands.guild_only()
    @commands.has_guild_permissions(manage_emojis = True)
    @commands.has_permissions(manage_emojis=True)
    async def stealEmoji(self, ctx, *, args = ''):
        gLimit = ctx.guild.emoji_limit
        gCurr = len(await ctx.guild.fetch_emojis())
        print(str(gCurr)+'/'+str(gLimit)+' emojis')
        # if gCurr >= gLimit:
        #         return await ctx.send("This server is already at the limit and cant have more emojis **):**\n(If you think this is an error,contact Blackfinix/EvilGiraffes/PPT)")
        turl = 'https://cdn.discordapp.com/emojis/'
        if args == '':
            return await ctx.send("No emoji or link detected.")
        try:
            msg = args.split()
            if reg.match(pattern='https://cdn.discordapp.com/emojis/', string=msg[0]):
                data = await gp.getDataFromLink(url=str(msg[0]), fileName='WhyAreYouLookingAtThis')
                name = '_'.join(msg[1:]) or 'RandomName'
                newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

            else:
                print('got in else')
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

                data = await gp.getDataFromLink(url=turl, fileName="WhyAreYouLookingAtThis")

                newEm = await ctx.guild.create_custom_emoji(name=name, image=data.getvalue(), reason=f'{ctx.author.mention} triggered the command : $steal')
                return await ctx.send(f'Added the emoji {newEm} to the server with the name : "{name}"')

        except Exception as e:
                print(f"There is some Error Here, error is defined by: {e}")
                await ctx.send("This server is already at the limit and cant have more emojis **):**")

    @fbnbug_bl
    @commands.command(
        name="feedback",
        aliases= ["fb"])
    async def feedBack(self,ctx,*,args):
        headers, post_content = await gp.feedback_n_bugs_json(ctx, str(args), selectName="Feedback")
        database = requests.get(url="https://api.notion.com/v1/pages/f3793c8657784e6498c5a1d06ecf1cd7", headers=headers).json()
        post_url = "https://api.notion.com/v1/pages"
        post = requests.post(url=post_url, headers=headers, json=post_content)




def setup(bot):
    bot.add_cog(syscom(bot))