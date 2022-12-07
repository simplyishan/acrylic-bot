import discord
from discord.ext import commands


class on_ready(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =f"+help | { str(len(self.bot.guilds))} Servers | {len(self.bot.users)} Users"))



    @commands.command()
    @commands.is_owner()
    async def setactivity(self,ctx,*,act):
        activity = discord.Game(name=act, type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)
        await ctx.send(f'Activity Has Been Set To {act}')


    @commands.command()
    @commands.is_owner()
    async def idle(self,ctx):
       
        await self.bot.change_presence(status=discord.Status.idle)
        await ctx.send(f'status set to idle')

    @commands.command()
    @commands.is_owner()
    async def online(self,ctx):
       
        await self.bot.change_presence(status=discord.Status.online)
        await ctx.send(f'status set to online')

    @commands.command()
    @commands.is_owner()
    async def invisable(self,ctx):
       
        await self.bot.change_presence(status=discord.Status.invisible)
        await ctx.send(f'status set to invisable')

    @commands.command()
    @commands.is_owner()
    async def dnd(self,ctx):
       
        await self.bot.change_presence(status=discord.Status.do_not_disturb)
        await ctx.send(f'status set to dnd')

    @commands.command()
    @commands.is_owner()
    async def resetac(self,ctx):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name =f"+help | { str(len(self.bot.guilds))} Servers | {len(self.bot.users)} Users"))
        await ctx.send(f'Activity has Been Reset')


    @commands.command()
    @commands.is_owner()
    async def listac(self,ctx):
        await ctx.send("""
        ```
        1 - idle
        2 - online
        3 - invisable
        4 - dnd
        5 - resetac
        6 - setactivity
        ```
        """)


async def setup(bot:commands.Bot):
    await bot.add_cog(on_ready(bot))