import time
import discord
import logging
import requests
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color

logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour.default()




    @commands.group(name="status",
                      description="Shows users status",
                      usage="status <member>")
    async def status(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        status = member.status
        if status == discord.Status.offline:
            status_location = "Not Applicable"
        elif member.mobile_status != discord.Status.offline:
            status_location = "Mobile"
        elif member.web_status != discord.Status.offline:
            status_location = "Browser"
        elif member.desktop_status != discord.Status.offline:
            status_location = "Desktop"
        else:
            status_location = "Not Applicable"
        await ctx.send(embed=discord.Embed(title="<:reply3:1003377442553081887> | status",
                                           description="`%s`: `%s`" %
                                           (status_location, status),
                                           color=000000))


    @commands.group(name="user",
                      description="Shows user syntax",
                      usage="user [user]")
    async def user(self, ctx, user: discord.Member = None):
        return await ctx.send(
            embed=discord.Embed(title="user",
                                description="user: %s\nid: **`%s`**" %
                                (user.mention, user.id),
                                color=000000))

    @commands.group(name="role",
                      description="Shows role syntax",
                      usage="role [role]")
    async def role(self, ctx, role: discord.Role):
        return await ctx.send(
            embed=discord.Embed(title="role",
                                description="role: %s\nid: **`%s`**" %
                                (role.mention, role.id),
                                color=000000))

    @commands.group(name="channel",
                      description="Shows channel syntax",
                      usage="channel [channel]")
    async def channel(self, ctx, channel: discord.TextChannel):
        return await ctx.send(
            embed=discord.Embed(title="channel",
                                description="channel: %s\nid: **`%s`**" %
                                (channel.mention, channel.id),
                                color=000000))

    @commands.group(name="boosts",
                      description="Shows boosts count",
                      usage="boosts",
                      aliases=["bc"])
    async def boosts(self, ctx):
        await ctx.send(
            embed=discord.Embed(title="boosts",
                                description="**`%s`**" %
                                (ctx.guild.premium_subscription_count),
                                color=000000))

    @commands.command(aliases=['mc', 'members'])
    async def membercount(self, ctx):
        embedmem = discord.Embed(title=f"**Members**",
                                 description=f"{ctx.guild.member_count}",
                                 color=000000,
                                 timestamp=ctx.message.created_at)
        embedmem.set_footer(text=f"{ctx.guild.name}")
        await ctx.send(embed=embedmem)

    @commands.command()
    async def servericon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=000000,
            title=f"{server}'s Icon",
            description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
            if not server.icon.is_animated() else
            f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)



    @commands.command(aliases=["whois", "ui"])
    async def userinfo(self,
                       ctx: commands.Context,
                       member: discord.Member = None):
        button = discord.ui.Button(label=f'Badges',
                                   style=discord.ButtonStyle.grey)
        if member == None:
            member = ctx.author

        async def button_callback(interaction: discord.Interaction):
            badges = ""
            if ctx.author.public_flags.hypesquad:
                badges = "Hypesquad"
            elif ctx.author.public_flags.hypesquad_balance:
                badges = "Hypesquad Balance"
            elif ctx.author.public_flags.hypesquad_bravery:
                badges = "Hypesquad Bravery"
            elif ctx.author.public_flags.hypesquad_brilliance:
                badges = "Hypesquad Brilliance"
            elif ctx.author.public_flags.early_supporter:
                badges = "Early Supporter"
            elif ctx.author.public_flags.verified_bot_developer:
                badges = "Verified Bot Developer"
            elif ctx.author.public_flags.partner:
                badges = "Partner"
            elif ctx.author.public_flags.bug_hunter:
                badges = "Bug Hunter"
            for i in badges:
                embed1 = discord.Embed(title='Badges', color=000000)
                embed1.set_author(name=f'{member}',
                                  icon_url=f'{member.avatar}')                
                await interaction.response.send_message(embed=embed1,
                                                        ephemeral=True)

        embed = discord.Embed(color=member.color)
        bannerUser = await self.bot.fetch_user(member.id)
        embed.add_field(
            name=f"__**General Information**__",
            value=
            f"**Name:** {member.name}#{member.discriminator}\n **ID**: {member.id}\n **Account Created:** <t:{int(member.created_at.timestamp())}:D>\n **Joined Server On:** <t:{int(member.joined_at.timestamp())}:D>\n **Highest Role:** {member.top_role.mention}"
        )
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
        embed.set_thumbnail(url=member.avatar)
        if not bannerUser.banner:
            pass
        else:
            embed.set_image(url=bannerUser.banner)
        await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(general(bot))
