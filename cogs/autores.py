import discord
from discord.ext import commands
import json


class autoresponse(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener() 
  async def on_message(self, message: discord.Message) -> None:
        if message.author == self.client.user:
                return
        try:
            if message is not None:
                print('loadded file autoresponse.json')
                with open("autoresponse.json", "r") as f:
                    autoresponse = json.load(f)
                if str(message.guild.id) in autoresponse:
                    ans = autoresponse[str(message.guild.id)][message.content.lower()]
                    return await message.channel.send(ans)
        except:
            print('cant load autoresponse.json file try again..!')
            pass

  @commands.hybrid_group(description='show the help menu of autoresponse',aliases=['aut' , 'ar'])
  async def autoresponse(self, ctx):
        ...


    
  @autoresponse.command(aliases=["add",'a'],description='create autoresponse in the server')  
  @commands.cooldown(1, 2, commands.BucketType.user)
     
  @commands.has_permissions(administrator=True)
  async def create(self, ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        numbers = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              numbers.append(autoresponsecount)
            if len(numbers) >= 10:
                return await ctx.send(f'<:aio_cross:1006293791562530876> | You can\'t add more than 10 autoresponses in a server.')
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                return await ctx.send(f'<:aio_cross:1006293791562530876> | The autoresponse `{name}` is already in the server.')
        if str(ctx.guild.id) in autoresponse:
            autoresponse[str(ctx.guild.id)][name] = message
            with open("autoresponse.json", "w") as f:
              json.dump(autoresponse, f, indent=4)
            return await ctx.send(f'<:aio_tick:1006293769068482560> | Created a autoresponse with the name : `{name}`.')

        data = {
            name : message,
        }
        autoresponse[str(ctx.guild.id)] = data

        with open("autoresponse.json", "w") as f:
            json.dump(autoresponse, f, indent=4)
            return await ctx.send(f'<:aio_tick:1006293769068482560> | Created a autoresponse with the name : `{name}`.')

  @autoresponse.command(aliases=["remove",'del','r'],description='delete autoresponse in the server')
  @commands.cooldown(1, 5, commands.BucketType.user)    
  @commands.has_permissions(administrator=True)
  async def delete(self, ctx, name):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
            
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                del autoresponse[str(ctx.guild.id)][name]
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.send(f'<:aio_tick:1006293769068482560> | Deleted the `{name}` autoresponse in the server.')
            else:
                return await ctx.send(f'<:aio_cross:1006293791562530876> | No autoresponse found with the name `{name}`.')
        else:
            return await ctx.send(f'<:aio_cross:1006293791562530876> | There is no autoresponses in the server.')
  @autoresponse.command(description='edit the old created autoresponse of server')
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(administrator=True)
  async def edit(self, ctx, name , *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                return await ctx.send(f'<:aio_tick:1006293769068482560> | Edited the `{name}` autoresponse.')
        else:
            return await ctx.send(f'<:aio_cross:1006293791562530876> | There is no autoresponses in the server.')
  @autoresponse.command(aliases=["count"],description='count all autoresponses of server')
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(administrator=True)
  async def list(self, ctx):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
              autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0000)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                    st += f"**[ {'0' + str(count) if count < 10 else count} ]** Name <:arrow_next:1006293699854082049> {autoresponse}\n"
                    test = count
                    count += 1
            embed.title = f"Total autoresponses - {test}"
        embed.description = st
        await ctx.send(embed=embed) 
    
async def setup(client):
    await client.add_cog(autoresponse(client))