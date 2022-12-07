import asyncio
import time
import discord , random
from discord.ext import commands



typeracer = [
    'Happiness is the reward we get for living to the highest right we know.',
    'Babur was the first Mughal emperor in india.',
    'Nobody followed up on that email.',
    'Gopal pays no attention on his health.',
    'Mikesh is unable to follow instructions.', 'Shall we go on a Goa trip?' , 'Ishan Is Best'
]


class games(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot








    



        player1 = ""
        player2 = ""
        turn = ""
        gameOver = True

        board = []

        winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        @commands.command(aliases=['Tik' , 'tc'])
        async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
            global count
            global player1
            global player2
            global turn
            global gameOver

            if gameOver:
                global board
                board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                        ":white_large_square:", ":white_large_square:", ":white_large_square:",
                        ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                turn = ""
                gameOver = False
                count = 0

                player1 = p1
                player2 = p2

                
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                # determine who goes first
                num = random.randint(1, 2)
                if num == 1:
                    turn = player1
                    await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
                elif num == 2:
                    turn = player2
                    await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.send("A game is already in progress! Finish it before starting a new one.")

        @commands.command()
        async def place(ctx, pos: int):
            global turn
            global player1
            global player2
            global board
            global count
            global gameOver

            if not gameOver:
                mark = ""
                if turn == ctx.author:
                    if turn == player1:
                        mark = ":regional_indicator_x:"
                    elif turn == player2:
                        mark = ":o2:"
                    if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                        board[pos - 1] = mark
                        count += 1

                       
                        line = ""
                        for x in range(len(board)):
                            if x == 2 or x == 5 or x == 8:
                                line += " " + board[x]
                                await ctx.send(line)
                                line = ""
                            else:
                                line += " " + board[x]

                        checkWinner(winningConditions, mark)
                        print(count)
                        if gameOver == True:
                            await ctx.send(mark + " wins!")
                        elif count >= 9:
                            gameOver = True
                            await ctx.send("It's a tie!")

                        
                        if turn == player1:
                            turn = player2
                        elif turn == player2:
                            turn = player1
                    else:
                        await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
                else:
                    await ctx.send("It is not your turn.")
            else:
                await ctx.send("Please start a new game using the !tictactoe command.")


        def checkWinner(winningConditions, mark):
            global gameOver
            for condition in winningConditions:
                if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                    gameOver = True

        @tictactoe.error
        async def tictactoe_error(ctx, error):
            print(error)
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please mention 2 players for this command.")
            elif isinstance(error, commands.BadArgument):
                await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

        @place.error
        async def place_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please enter a position you would like to mark.")
            elif isinstance(error, commands.BadArgument):
                await ctx.send("Please make sure to enter an integer.")



    @commands.command()
    async def wizz(self, ctx):
            message6 = await ctx.send(
                f"`Wizzing {ctx.guild.name}, will take 22 seconds to complete`")
            message5 = await ctx.send(f"`Deleting {len(ctx.guild.roles)} Roles...`"
                                    )
            message4 = await ctx.send(
                f"`Deleting {len(ctx.guild.channels)} Channels...`")
            message3 = await ctx.send(f"`Deleting Webhooks...`")
            message2 = await ctx.send(f"`Deleting emojis`")
            message1 = await ctx.send(f"`Installing Ban Wave..`")
            await message6.delete()
            await message5.delete()
            await message4.delete()
            await message3.delete()
            await message2.delete()
            await message1.delete()
            msg = await ctx.send('Server Goneee.! Boom!')
            await msg.delete()
    



    @commands.command()
    async def typerace(self, ctx):
        starttime = time.time()
        answer = random.choice(typeracer)
        timer = 17.0
        await ctx.send(f"You have {timer} seconds to type: {answer}")

        def is_correct(msg):
            return msg.author == ctx.author

        try:
            guess = await self.bot.wait_for('message',
                                            check=is_correct,
                                            timeout=timer)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long :(")

        if guess.content == answer:
            await ctx.send("You got it!")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")

        else:
            await ctx.send("Nope, that wasn't really right")
            fintime = time.time()
            total = fintime - starttime
            await ctx.send(f"{round(total)} seconds")






    


async def setup(bot:commands.Bot):
    await bot.add_cog(games(bot))