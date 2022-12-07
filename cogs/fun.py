import json
import discord
from discord.ext import commands
import requests




def quotes():
 response = requests.get("https://zenquotes.io/api/random")
 json_data = json.loads(response.text)
 quote = json_data[0]['q'] + " -" + json_data[0]['a']
 return(quote)



class funcmd(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "fban",aliases=["Fban" , 'fakeban' , 'Fakeban'])
    @commands.guild_only()
    async def fakeban(self,  ctx:commands.Context , * , user:discord.Member):
        embed = discord.Embed(description=f"**<:tick_bdcord:1036550407641649152> | {user} has been banned**" , color=0000)
        await ctx.send(embed=embed)
    
    @commands.group(invoke_without_command=True , aliases=["ava" , "av"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        memberav = member.avatar
        e = discord.Embed(description=f'[download..!]({memberav})')
        e.set_image(url=memberav)
        await ctx.send(embed=e)    

    @avatar.command(aliases=["ava" , "av"])
    async def server(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.author
        memberav = member.guild_avatar
        if memberav is None:
            await ctx.send(f'{member} has no server avatar..! ')
        else:

            e = discord.Embed(description=f'[download..!]({memberav})')
            e.set_image(url=memberav)
            await ctx.send(embed=e) 


    


    @commands.command(aliases=['cds'])
    async def codestats(self, ctx: commands.Context):
        code = discord.Embed(title='Code Stats' , description='```\n Files : 7 \n Lines : 50k+ \n Size : 25mb \n Developer : ishan.notfound#0071 \n Owner : obito.notabrand#1337 ```' , color=0000)
        await ctx.send(embed=code)

    @commands.command(aliases=['em'])
    async def embed(self, ctx: commands.Context , title , des , color ):
            embed = discord.Embed(title=title, description=des, color=int(color))
            await ctx.send(embed=embed)





    @commands.command()
    @commands.guild_only()
    async def quote(self,ctx):
     asa =  discord.Embed(description=quotes(),color=0000)
     await ctx.send(embed=asa)




    @commands.command()
    async def code(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('`' + message + "`")

    @commands.command()
    async def gender(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f"{member.mention}'s gender is None",
                              color=discord.Colour.default())
        await ctx.send(embed=embed)

    @commands.command()
    async def bold(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('**' + message + '**')

    @commands.command()
    async def censor(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('||' + message + '||')

    @commands.command()
    async def underline(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send('__' + message + '__')

    


async def setup(bot:commands.Bot):
    await bot.add_cog(funcmd(bot))