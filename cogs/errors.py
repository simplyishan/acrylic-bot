import discord
from discord.ext import commands

cross = "<:crosss:1008856652314849313>"

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        missing = ", ".join(error.args)
        await ctx.send(f"> | {missing}", delete_after=10)
      elif isinstance(error, commands.MissingPermissions):
        missing_perms = ",".join(error.missing_permissions)
        embed = discord.Embed(color = 0x2f3136, description = f"{cross} | You don't have the {missing_perms} permission to run the **{ctx.command.name}** command!")
        await ctx.send(embed = embed, delete_after=10)
      elif isinstance(error, commands.MemberNotFound):
          await ctx.send(f"{cross} | Please provide a member!", delete_after=10)
      elif isinstance(error, commands.NSFWChannelRequired):
        em6 = discord.Embed(description=f"> | Please first enable NSFW Channel in this channel!", color = discord.Colour.dark_red(), timestamp=ctx.message.created_at)
        em6.set_image(url=f"https://i.imgur.com/oe4iK5i.gif")

        await ctx.send(embed=em6, delete_after=10)
      elif isinstance(error, commands.BotMissingPermissions):
        missing = ", ".join(error.missing_permissions)
        embed = discord.Embed(color =0x2f3136, description = f"{cross} | Bot requires {missing}  permission(s) to run this command")
        await ctx.send(embed = embed, delete_after=10)
      elif isinstance(error, commands.CommandNotFound):
        print(" ")
      else:
        raise error

    @commands.Cog.listener()
    async def on_message(self, message):
      member = message.author
      idk = message.content.lower()
      if idk == self.bot.user.mention:
        if member.bot:
          return
        embed = discord.Embed(description='Hey, My Prefix is `+` | Use `+help` To Get Started')
        await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(errors(bot))