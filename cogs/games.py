import random

from discord.ext import commands


class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------------------------------

    @commands.command(
        name='minesweeper',
        aliases=['ms','mines'])
    async def mineSweeper(self, ctx, inputRows=8, inputColumns=8, inputMines=5):
        rows = int(inputRows)
        columns = int(inputColumns)
        mines = int(inputMines)
        if ((rows < 5 or columns > 9 or columns < 3 or mines < 1 or (mines >= (rows - 1) * (columns - 1) - 2)) or (rows * columns > 99)):
            return await ctx.send(
                'Range of rows : [5,..]\nRange of columns : [3,9]\nRange of bombs : [1,..]\n**No weird numbers**'+
                '\nSyntax is `minesweeper|ms|mines [rows] [columns] [mines]`\n'+
                '**Careful of character limit!** `Rows` times `Columns` must be lower than 100.\n'+
                'For example, `ms 10 10` is bad, but `ms 10 9` is fine')

        msMap = [[0 for column in range(columns)] for row in range(rows)]
        borderX = columns - 1
        borderY = rows - 1
        ms = ''
        for num in range(mines):
            x = 0
            y = 0
            while True:
                tx = random.randint(0, borderX)
                ty = random.randint(0, borderY)
                if (msMap[ty][tx] != 'X'):
                    msMap[ty][tx] = 'X'
                    x = tx
                    y = ty
                    #print(f'{x},{y}')
                    break
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if (i < 0 or j < 0):
                        continue
                    try:
                        if (msMap[j][i] != 'X'):
                            msMap[j][i] += 1
                            #print(f'{i} and {j}')
                    except Exception as e:
                        continue
        for row in msMap:
           ms += " ".join(str(cell) for cell in row) + "\n"
        print(ms)
        # print(msMap)

        replace = {'X': '||:boom:||', '0': '||:zero:||', '1': '||:one:||', '2': '||:two:||', '3': '||:three:||',
                    '4': '||:four:||','5': '||:five:||','6': '||:six:||','7': '||:seven:||','8': '||:eight:||'}
        for item in replace:
            ms = ms.replace(item, replace[item])

        await ctx.send(ms)

# ------------------------------------------------------------------------------

def setup(bot):
    bot.add_cog(games(bot))