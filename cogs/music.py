import discord, wavelink, asyncio
from discord.ext import commands

OPTIONS = {
    "1️⃣": 0,
    "2⃣": 1,
    "3⃣": 2,
    "4⃣": 3,
    "5⃣": 4,
}

class music(commands.Cog):
    emoji = "💖"
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.connect_nodes())


    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        try:
          await wavelink.NodePool.create_node(
            bot=self.bot,
            host="node2.lewdhutao.tech",
            port=443,
            password="lewdhutao",
            https=True
        )
          print("Node Created!")
        except Exception as e:
          print(e)
    
    async def choose_one(self, ctx, tracks):
        def _check(r, u):
            return (
                r.emoji in OPTIONS.keys()
                and u == ctx.author
                and r.message.id == msg.id
            )

        embed = discord.Embed(
            title="Choose a song",
            description=(
                "\n".join(f"**`[{i+1}]` | {t.title}**" for i, t in enumerate(tracks[:5]))
            ),
            color=0000
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        msg = await ctx.send(embed=embed)
        for emoji in list(OPTIONS.keys())[:min(len(tracks), len(OPTIONS))]:
            await msg.add_reaction(emoji)
        
        try: 
            reaction, _ = await self.bot.wait_for('reaction_add', timeout=60.0, check=_check)
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.message.delete()
        else:
            await msg.delete()
            return tracks[OPTIONS[reaction.emoji]]

    @commands.hybrid_command(name="volume", usage="volume int", description="Sets the volume of the player")
    @commands.cooldown(1,2,commands.BucketType.user)
    async def _volume(self, ctx, volume: int):
      embed = discord.Embed(color=0000)
      if volume < 1 or volume > 100:
        embed.description = "<:tick_bdcord:1036550407641649152>  | Choose the volume limit between 1 to 100"
        embed.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
        return await ctx.reply(embed=embed)
      if ctx.voice_client == None:
        embed.description = "<:crossss:1037681327564140664> | You are not connected to the voice channel"
        return await ctx.reply(embed=embed)
      chnl: wavelink.Player = ctx.voice_client
      if not chnl.is_playing():
        embed.description = "<:crossss:1037681327564140664> | Play the music to use volume command"
        return await ctx.reply(embed=embed)
      await chnl.set_volume(volume)
      embed.description = f"<:tick_bdcord:1036550407641649152>  | The volume level has been set to {volume}%"
      await ctx.send(embed=embed)

    @commands.hybrid_command(name="connect", aliases=["join","j","jvc"], usage="connect <channel>")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def connect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Connects to a voice channel."""
        if not getattr(ctx.author, "voice", None):
            nv = discord.Embed(description=f'<:crossss:1037681327564140664> | You are not connected to a voice channel.', color=0000)
            nv.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=nv)
            return
        if channel is None:
            channel = ctx.author.voice.channel
        elif ctx.voice_client:
            av = discord.Embed(description=f"<:crossss:1037681327564140664> | I am already connected to a voice channel.", color=0000)
            av.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=av)
            return
        vc: wavelink.Player = await channel.connect(cls=wavelink.Player)
        sc = discord.Embed(description=f"<:tick_bdcord:1036550407641649152>  | Successfully connected to `{channel.name}`.", color=0000)
        sc.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
        await ctx.send(embed=sc)
    
    @commands.hybrid_command(name="disconnect", aliases=['leave','dc'], usage="[disconnect|leave] <channel>")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def disconnect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Disconnects from a voice channel."""
        if not getattr(ctx.author, "voice", None):
            mnv = discord.Embed(description=f"<:crossss:1037681327564140664> | You are not connected to a voice channel.", color=0000)
            mnv.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=mnv)
            return
        if channel == None:
            channel = ctx.author.voice.channel
        elif not ctx.voice_client:
            mnc = discord.Embed(description=f"<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000)
            mnc.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=mnc)
            return
        elif ctx.author.voice.channel != ctx.voice_client.channel:
            svc = discord.Embed(description=f"<:crossss:1037681327564140664> | You should be in the same voice channel that I'm in.", color=0000)
            svc.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=svc)
            return
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()
        await ctx.send(embed=discord.Embed(description=f"<:tick_bdcord:1036550407641649152>  | Successfully disconnected from `{vc.channel.name}`", color=0000))
    
    @commands.hybrid_command(name="play", aliases=['p'], usage="[play|p] [query]", description="Play songs in your voice channel.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def play(self, ctx: commands.Context, *, query: str):
        """Listen to lag-free music."""
        if not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<:crossss:1037681327564140664> | You are not connected to a voice channel.", color=0000)
            await ctx.send(embed=nvc)
            return
        elif not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            svc = discord.Embed(description=f"<:tick_bdcord:1036550407641649152>  | Successfully connected to {ctx.author.voice.channel.name}", color=0000)
            svc.set_footer(text="Made With Wavelink By ishan.notfound#0071", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
            await ctx.send(embed=svc)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        tracks = await wavelink.YouTubeTrack.search(query=query)
        song = await self.choose_one(ctx, tracks)
        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(song)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{song.title} [{ctx.author.mention}]", color=0000))
        else:
            await vc.queue.put_wait(song)
            await ctx.send(embed=discord.Embed(title="Music Queue", description=f"Added {song.title} to the queue.", color=0000))
        vc.ctx = ctx
        setattr(vc, "loop", False)
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.Track, reason):
        ctx = player.ctx
        vc: player = ctx.voice_client

        if player.loop:
            await player.play(track)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{track.title} [{ctx.author.mention}]", color=0000))
        
        if not player.queue.is_empty:
            next_track = await vc.queue.get_wait()
            await vc.play(next_track)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{next_track.title} [{ctx.author.mention}]", color=0000))

    @commands.hybrid_command(name="loop", usage="loop", description="Toggle looping your currently playing track.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def loop(self, ctx: commands.Context):
        if not ctx.voice_client:
            svc = discord.Embed(description=f"<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000)
            await ctx.send(embed=svc)
            return
        elif not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000)
            await ctx.send(embed=nvc)
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if not vc.is_playing():
            bvc = discord.Embed(description=f"<:crossss:1037681327564140664> | I am not playing anything.", color=0000)
            await ctx.send(embed=bvc)
            return
        vc.loop = True if not vc.loop else False
        mvc = discord.Embed(description=f"<:tick_bdcord:1036550407641649152>  | Looping set to {'**true**.' if vc.loop else '**false**.'}", color=0000)
        await ctx.send(embed=mvc)
    
    @commands.hybrid_command(name="stop", usage="stop", description='Stop the player & clear the whole queue.')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description=f"<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if vc.is_playing() is False:
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | I am not playing anything.", color=0000))
            return

        await vc.stop()
        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description=f"<:tick_bdcord:1036550407641649152>  | Destroyed the player.", color=0000))
    
    @commands.group(name="queue", usage="queue", description="Display the queue lf this server.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def queue(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            if not ctx.voice_client:
                await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | There is nothing playing yet.", color=0000))
            elif not getattr(ctx.author.voice, "channel", None):
                await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            else:
                vc: wavelink.Player = ctx.voice_client
            
            if vc.queue.is_empty:
                return await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | There are no more tracks in the queue.", color=0000))
            
            embed = discord.Embed(title="Music Queue", color=0000)
            queue = vc.queue.copy()
            description = ""
            for num, track in enumerate(queue):
                description += f"`[{num + 1}]` | " + f"{track.title}" + "\n"
            embed.description = description
            await ctx.send(embed=embed)

    @queue.command(name="clear", usage="queue clear", description='Clears the queue of the server.')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def clear(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description="Cleared the queue.", color=0000))
    
    @commands.hybrid_command(name="pause", usage="pause", description="Pause the player.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | There is nothing playing yet.", color=0000))
        await vc.pause()
        await ctx.send(embed=discord.Embed(description="Paused the player.", color=0000))
    
    @commands.hybrid_command(name="resume", usage="resume", description="Resume the current paused song.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | There is nothing playing yet.", color=0000))
        await vc.resume()
        await ctx.send(embed=discord.Embed(description="<:tick_bdcord:1036550407641649152>  | Resumed the player.", color=0000))
     
    @commands.hybrid_command(name="skip", usage="skip", description="Skip the current playing track.")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def skip(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | I am not connected to a voice channel.", color=0000))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | You are not connected to a voice channel to do this.", color=0000))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            await ctx.send(embed=discord.Embed(description="<:crossss:1037681327564140664> | There is nothing playing yet.", color=0000))
            return
        track = await vc.queue.get_wait()
        await vc.play(track)
        await ctx.send(embed=discord.Embed(description="<:tick_bdcord:1036550407641649152>  | Skiped the track.", color=0000))
        await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{track.title} [{ctx.author.mention}]", color=0000))

async def setup(bot):
    await bot.add_cog(music(bot))