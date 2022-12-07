import discord
import os
import asyncio
from discord.ext import commands
import humanfriendly
import datetime
from discord.ext import commands
import aiohttp
from io import BytesIO

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []

    @commands.command(aliases=['sb'])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member: discord.Member, *, reason=None):

        if reason is None:
            reason = f"No reason given.\nBanned by {ctx.author}"

        await member.ban(reason=reason)
        await member.unban(reason=reason)
        await ctx.send(f"$ Sucessfully soft-banned {member}.")

    
    @commands.group(invoke_without_command=True)
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx,amount:int=10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)-1} messages", delete_after=5)

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)}/{amount} message(s) which started with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)}/{amount} message(s) which ended with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)}/{amount} message(s) which contained the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)}/{amount} message(s) which were sent by the mentioned user")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:tick_bdcord:1036550407641649152> | Deleted {len(deleted)}/{amount} message(s) which contained invites")

# TODO: add proper cooldowns to all the commands listed here
# TODO ability to 
#@commands.has_permissions(send_messages=True)
    
      
    @commands.command(aliases=['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, *, reason="No Reason Provided."):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        if ctx.author.top_role.position > member.top_role.position or ctx.author == guild.owner:
            await ctx.send(f" <:tick_bdcord:1036550407641649152> | Successfully muted {member.display_name}")
            await member.add_roles(mutedRole, reason=reason)
            await member.send(f"‼️ : | You have been muted from: {guild.name} reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"**<:crossss:1037681327564140664>  | You cannot mute someone with a higher role than you!")

    @commands.command(aliases=['out'])
    @commands.guild_only()
    @commands.has_permissions(moderate_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def timeout(self, ctx, member: discord.Member, duration, *, reason=None):
        if reason is None:
            reason = f"Action done by {ctx.author}"

        humanly_duration = humanfriendly.parse_timespan(duration)

        await member.timeout(
            discord.utils.utcnow() + datetime.timedelta(seconds=humanly_duration),
            reason=reason
        )
        await ctx.send(f"{self.bot.yes} {member} has been timed out for {duration}.\nReason: {reason}")

    @commands.command(aliases=['unm'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await ctx.send(f"<:tick_bdcord:1036550407641649152> | {member.display_name} has been unmuted")
        await member.remove_roles(mutedRole)
        await member.send(f"‼️ | You are have been unmuted from: {ctx.guild.name}")



    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send(f"🤡 You cannot kick me!")
        if ctx.author.top_role.position > member.top_role.position or member == ctx.guild.owner:
            await member.kick(reason=reason)
            await ctx.send(f"<:tick_bdcord:1036550407641649152> | {member.display_name} has been kicked from this guild, for: {reason}")
            await member.send(f"‼️ | You have been kicked from {ctx.guild.name} for: {reason}!")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"**<:crossss:1037681327564140664>  | You cannot kick someone with a higher role than you!")

    @commands.command()
    async def enlarge(self, ctx, emoji: discord.Emoji):
        ''' Enlarge any emoji '''
        # url = ctx.emoji.url_as(self,format='png')
        url = emoji.url
        await ctx.send(url)
      
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveallhumans(self,ctx,role:discord.Role):
        ''' Gives all the humans any role '''
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Adding {role.name} to all humans!")

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.add_roles(role)
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Successfully given {role.name} to all members!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveallbots(self,ctx,role:discord.Role):
        ''' Give all bots any role '''
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Adding {role.name} to all bots!")

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.add_roles(role)
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Successfully given {role.name} to all bots!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeallhumans(self,ctx,role:discord.Role):
        ''' Removes a role from all human members '''
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Removing {role.name} from all humans!")

        humans = [mem for mem in ctx.guild.members if not mem.bot]
        for h in humans:
            await h.remove_roles(role)
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Successfully removed {role.name} from all members!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeallbots(self,ctx,role:discord.Role):
        ''' Removes a role from all the bots '''
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Removing  {role.name} from all bots!")

        humans = [mem for mem in ctx.guild.members if mem.bot]
        for h in humans:
            await h.remove_roles(role)
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Successfully removed {role.name} from all bots!")

  
    @commands.command(aliases=['w'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, * , reason="No Reason Provided!"):
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | {member.display_name} has been warned for: {reason}")
        await member.send(f"‼️ | You have been warned in {ctx.guild.name} for: {reason}")

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def delemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Emoji has been deleted.")

    @commands.command()
    async def steal(self, ctx, url:str, *, name = None):
        if name == None:
            name == "stolen-emoji"
        if url == discord.Emoji:
            url = discord.Emoji.url
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    imgOrGif = BytesIO(await r.read())
                    bValue = imgOrGif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=bValue, name=name)
                        await ctx.send(f"<:tick_bdcord:1036550407641649152> | Sucessfully added Emoji `:{name}:`")
                        await ses.close()
                    else:
                        await ctx.send(f"**<:crossss:1037681327564140664>  | Something went wrong** | {r.status}")
                except discord.HTTPException:
                    await ctx.send(f"**<:crossss:1037681327564140664>  | The file is too big.**")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send('You cannot ban the bot!')
        if ctx.author.top_role.position > member.top_role.position or ctx.author == ctx.guild.owner:
            await member.ban(reason=reason)
            await ctx.send(f"**<:tick_bdcord:1036550407641649152> | {member.display_name} has been successfully banned**")
            await member.send(f"‼️ | You have been banned from {ctx.message.guild.name} for reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"**<:crossss:1037681327564140664>  | You cannot ban someone with a higher role than you.**")


    @commands.command()
  	#@commands.has_permissions(kick_members=True)
    async def block(self, ctx, user):
        """
        Blocks a user from chatting in current channel.
           
        Similar to mute but instead of restricting access
        to all channels it restricts in current channel.
        """
                                
        if not user: # checks if there is user
            return await ctx.send("**<:crossss:1037681327564140664> | You must specify a user**")
                                
        await ctx.set_permissions(user, send_messages=False) # sets permissions for current channel
    
    @commands.command()
  	#@commands.has_permissions(kick_members=True)
    async def unblock(self, ctx, user):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("**<:crossss:1037681327564140664>  | You must specify a user**")
        
        await ctx.set_permissions(user, send_messages=True) # gives back send messages permissions
        await ctx.send(f'**<:tick_bdcord:1036550407641649152> | {user} has been unblocked**')


    
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | {user.name} has been successfully unbanned")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: discord.TextChannel):
        await channel.clone()
        await ctx.send(f"<:tick_bdcord:1036550407641649152> | {channel.name} has been successfully cloned")


    

async def setup(bot):
   await bot.add_cog(moderation(bot))