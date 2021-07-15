from discord.ext import commands
import random

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='minesweeper',
        aliases=['ms'])
    async def mineSweeper(self, ctx, rows=8, columns=8, mines=5):
        run = True
        row = int(rows)
        column = int(columns)
        mine = int(mines)
        if row > 11:
            run = False
        elif column > 9:
            run = False
        elif mine < 3:
            run = False
        elif mine >= row - 1 or mine >= column - 1:
            run = False
        if run:
            arr = [[0 for column in range(column)] for rows in range(row)]
            border_x = column - 1
            border_y = row - 1
            for num in range(mine):
                x = random.randint(0, border_x)
                y = random.randint(0, border_y)
                arr[y][x] = 'X'
                if x != border_x:
                    if arr[y][x + 1] != 'X':  # right
                        arr[y][x + 1] += 1
                if x != 0:
                    if arr[y][x - 1] != 'X':  # left
                        arr[y][x - 1] += 1
                if y != border_y:
                    if arr[y + 1][x] != 'X':  # up
                        arr[y + 1][x] += 1
                if y != 0:
                    if arr[y - 1][x] != 'X':  # down
                        arr[y - 1][x] += 1
                if y != border_y and x != border_x:
                    if arr[y + 1][x + 1] != 'X':  # up right
                        arr[y + 1][x + 1] += 1
                if y != 0 and x != border_x:
                    if arr[y - 1][x + 1] != 'X':  # down right
                        arr[y - 1][x + 1] += 1
                if y != border_y and x != 0:
                    if arr[y + 1][x - 1] != 'X':  # up left
                        arr[y + 1][x - 1] += 1
                if y != 0 and x != 0:
                    if arr[y - 1][x - 1] != 'X':  # down left
                        arr[y - 1][x - 1] += 1
            ms = ''
            for row in arr:
                if ms:
                    ms = f'{ms}\n' + " ".join(str(cell) for cell in row)
                else:
                    ms = " ".join(str(cell) for cell in row)
            replace = {'X': '||:boom:||', '0': '||:zero:||', '1': '||:one:||', '2': '||:two:||', '3': '||:three:||',
                       '4': '||:four:||'}
            for item in replace:
                ms = ms.replace(item, replace[item])
            await ctx.send(ms)
        else:
            await ctx.send(
                'Max rows is 11, max columns is 9 and minumum bombs is 3, and no weird numbers\nSyntax is `minesweeper [rows] [columns] [mines]`')
def setup(bot):
    bot.add_cog(games(bot))