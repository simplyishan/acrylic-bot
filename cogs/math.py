import discord
from discord.ext import commands


def subb(x: float, y: float):
    return x - y


def add(x: float, y: float):
    return x + y


def divv(x: float, y: float):
    return x / y


def multi(x: float , y: float):
    return x * y




class math(commands.Cog):
    def __init__(self ,bot:commands.Bot):
        self.bot = bot


    @commands.command()
    async def add(self,ctx,x: float , * , y: float ):
        addr = add(x=x,y=y)
        await ctx.send(addr)

    @commands.command()
    async def sub(self,ctx,x: float , * , y: float ):
        sub = subb(x=x,y=y)
        await ctx.send(sub)

    @commands.command()
    async def div(self,ctx,x: float , * , y: float ):
        divr = divv(x=x,y=y)
        await ctx.send(divr)

    @commands.command()
    async def multi(self,ctx,x: float , * , y: float ):
        multir = multi(x=x,y=y)
        await ctx.send(multir)



async def setup(bot:commands.Bot):
    await bot.add_cog(math(bot))