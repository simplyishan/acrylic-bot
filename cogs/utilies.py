import discord
from discord.ext import commands


class utilities(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "ping")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def ping(self, ctx:commands.Context):
        await ctx.send(f"Pong.! {round(self.bot.latency * 1000)} ms..!" )

    @commands.command(name = "invite")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def invite(self, ctx:commands.Context):
        embed = discord.Embed(title="Invite", description="[Invite Link With Admin](https://discord.com/api/oauth2/authorize?client_id=934760667234336798&permissions=8&scope=bot)", color=0000)
        button = discord.ui.Button(label=f'Invite Me',
                                   style=discord.ButtonStyle.url,
                                   url='https://discord.com/api/oauth2/authorize?client_id=934760667234336798&permissions=8&scope=bot')
        buttonz = discord.ui.Button(label=f'Invite Me(0 Perms)',
                                   style=discord.ButtonStyle.url,
                                   url='https://discord.com/api/oauth2/authorize?client_id=934760667234336798&permissions=0&scope=bot')
        view = discord.ui.View()
        view.add_item(button)
        view.add_item(buttonz)
        await ctx.send(embed=embed , view=view)


   


    @commands.command(aliases=['serverinfo' , 'si'])
    async def info(self, ctx: commands.Context):
        nsfw_level = ''
        button = discord.ui.Button(label=f'Server icon',
                                   style=discord.ButtonStyle.url,
                                   url=f'{ctx.guild.icon}')
        button2 = discord.ui.Button(label=f'Roles',
                                    style=discord.ButtonStyle.grey)
        view = discord.ui.View()
        view.add_item(button)
        view.add_item(button2)
        if ctx.guild.nsfw_level.name == 'default':
            nsfw_level = '**Default**'
        if ctx.guild.nsfw_level.name == 'explicit':
            nsfw_level = '**Explicit**'
        if ctx.guild.nsfw_level.name == 'safe':
            nsfw_level = '**Safe**'
        if ctx.guild.nsfw_level.name == 'age_restricted':
            nsfw_level = '**Age Restricted**'

        async def button2_callback(interaction: discord.Interaction):
            roles = ""
            for i in ctx.guild.roles:
                roles += "• " + str(i.mention) + "\n"
            embed1 = discord.Embed(title=f'{ctx.guild.name}',
                                   description=f'{roles}',
                                   color=0000)
            await interaction.response.send_message(embed=embed1,
                                                    ephemeral=True)

        embed = discord.Embed(title=f'{ctx.guild.name} | {ctx.guild.id}',
                              color=0000)
        embed.add_field(
            name=f'**__General Information__**',
            value=
            f'**Owner:** {ctx.guild.owner.mention} | {ctx.guild.owner.id}\n**Members:**: {ctx.guild.member_count}\n**Created**: <t:{int(ctx.guild.created_at.timestamp())}:D>\n**Server Channels**: {len(ctx.guild.channels)}\n**Server Roles**: {len(ctx.guild.roles)}'
        )
        embed.add_field(
            name=f'**__Additional__**',
            value=
            f'NSFW level: **{nsfw_level}**\nVerification level: **{ctx.guild.verification_level.name}**\nExplicit Content Filter: **{ctx.guild.explicit_content_filter.name}**\n**Boost Teir**: {ctx.guild.premium_tier}\nMax Talk Bitrate: **{int(ctx.guild.bitrate_limit)}** kbps\nEmojis: {len(ctx.guild.emojis)}\nStickers: {len(ctx.guild.stickers)}\nBoost count: {ctx.guild.premium_subscription_count}'
        )
        embed.set_footer(text="made with love by team alpha", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
        button2.callback = button2_callback
        await ctx.send(embed=embed, view=view)



async def setup(bot:commands.Bot):
    await bot.add_cog(utilities(bot))