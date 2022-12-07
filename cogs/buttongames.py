import asyncio
import time
import discord
import random
from discord.ext import commands
from discord import app_commands
from typing import List
from discord.ui import Button, View





truth = ["Have you ever kissed an animal?","Have you ever cheated on a test?","What was the last thing you ate?","Do you have any unusual talents?","Do you have any phobias?","Have you ever used someone else's password?","Have you ever ridden the bus without paying the fare?","Do you message people during your classes?","Have you ever fallen asleep during a class?","Have you ever bitten a toenail?","Have you ever stolen something?","Are you a hard-working student?","What was the best day of you life?","What was the strangest dream you ever had?","What is the most annoying thing to you (pet peeve)?","If you could have a superpower, what would it be?","Who is most important to you?"]


dare = ["Have you ever kissed an animal?", "Have you ever cheated on a test?", "What was the last thing you ate?", "Do you have any unusual talents?", "Do you have any phobias?", "Have you ever used someone else's password?", "Have you ever ridden the bus without paying the fare?", "Do you message people during your classes?", "Have you ever fallen asleep during a class?", "Have you ever bitten a toenail?", "What is the most annoying thing to you (pet peeve)?", "Have you ever stolen something?", "Are you a hard-working student?", "What was the best day of you life?", "What was the strangest dream you ever had?","If you could have a superpower, what would it be?", "Who is most important to you?"]
class btngames(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

   
       
    @commands.command(aliases=["tnd",'Tnd','truthandare'])
    async def TnD(self, ctx):
       

        randomt = random.choice(truth)
        randomd = random.choice(dare)
        btn = Button(label='Truth', style=discord.ButtonStyle.green, emoji="<:Truth:1039997179420483585>")

        async def btncl(interaction):
            tembed = discord.Embed(
                title='Truthh.!', description=randomt, color=0000)
            await interaction.response.send_message(embed=tembed, ephemeral=True)

        btn2 = Button(
            label='Dare', style=discord.ButtonStyle.danger, emoji="<:Dare:1039997515434577920>")

        async def btncl2(interaction):
            dembed = discord.Embed(
                title='Daree.!', description=randomd, color=0000)
            await interaction.response.send_message(embed=dembed, ephemeral=True)
        btn2.callback = btncl2
        btn.callback = btncl
        view = View()
        view.add_item(btn)
        view.add_item(btn2)
        await ctx.send('**CHOOSE**', view=view , delete_after=5)


    
        
    @commands.command(name='rps', aliases=['rockpaperscissors'])
    async def rps(self, ctx):
        """Play Rock, Paper, Scissors game"""
        def check_win(p, b):
            if p=='🌑':
                return False if b=='📄' else True
            if p=='📄':
                return False if b=='✂' else True
            # p=='✂'
            return False if b=='🌑' else True

        async with ctx.typing():
            reactions = ['🌑', '📄', '✂']
            game_message = await ctx.send("**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
            for reaction in reactions:
                await game_message.add_reaction(reaction)
            bot_emoji = random.choice(reactions)

        def check(reaction, user):
            return user != self.bot.user and user == ctx.author and (str(reaction.emoji) == '🌑' or '📄' or '✂')
        try:
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's Up! :stopwatch:")
        else:
            await ctx.send(f"**:man_in_tuxedo_tone1:\t{reaction.emoji}\n:robot:\t{bot_emoji}**")
            # if conds
            if str(reaction.emoji) == bot_emoji:
                await ctx.send("**It's a Tie :ribbon:**")
            elif check_win(str(reaction.emoji), bot_emoji):
                await ctx.send("**You win :sparkles:**")
            else:
                await ctx.send("**I win :robot:**")





async def setup(bot: commands.Bot):
    await bot.add_cog(btngames(bot))
