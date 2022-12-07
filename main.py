import asyncio
import random 

import discord 
from discord.ext import commands
import json , datetime , pytz , jishaku
import os
# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
intents = discord.Intents.all()
bot = commands.Bot(prefix, intents = intents)
ending_note = """made with "💖" by @n's ishan#0658 """
bdtime = pytz.timezone('Asia/Dhaka')
now = datetime.datetime.now(bdtime)
inow  = datetime.datetime.now()
bot.owner_ids = 638073011236372480 , 699204389805490216 , 728538577520295996 , 161633683177078785 , 156794459797848065
embed = discord.Embed(title= "Online Logs" ,description=f' revivecord is onlinee!' + "" +  "\n" + "Local Time : " +  "  "  f'**`{now}`**' + '\n' + "International Time : " + "  " + f"**`{inow}`**")   
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    channel = bot.get_channel(1044310771456286750)
    await channel.send("<@&1017154426668073070>" ,embed=embed)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
bot.remove_command('help')
bot.case_insensitive = False













@bot.command()
async def bug(ctx , * , report):
    c = bot.get_channel(1038152856366235658) 
    rid = f"{ctx.author}-bug-{report}"
    await ctx.send(f'Report has been send successfully..! | Report Id : {rid} ')
    embed = discord.Embed(description=report, color=0000)
    await c.send(f'<@&1038154571580706858> | Report {report} By {ctx.author} | Report Id : {rid}',embed=embed) 


tick = "<:tickkk:1008067101241647114>"
ownremo = "<:owner:1040202967598518382>"
devemo = "<a:dd_dev:1008011307980701737>"
adminemo = "<:dd_admin:1008014517025919108>"
modemo = "<:dd_mod:1008011512385912938>"
staffemo = "<:dd_staff:1008011398611210270>"
spclemo = "<:dd_spcl:1008012364672671940>"
bugemo = "<:dd_bug:1008013111221026977>"
memo = '<:Wampus:1039932221273952377>'


@bot.command(aliases=['ab','Ab'])
@commands.is_owner()
async def addbadge(ctx, user: discord.Member, *, badge):
    if badge == "owner" or badge == "Owner":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{ownremo} **Owner**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{ownremo} **Owner**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "Dev" or badge == "dev":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{devemo} **Developer**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{devemo} **Developer**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
    
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "manager" or badge == "Manager":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{memo} **Manager**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{memo} **Manager**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)


        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "Admin" or badge == "admin":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{adminemo} **Admin**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{adminemo} **Admin**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "Mod" or badge == "mod":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{modemo} **Moderator**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{modemo} **Moderator**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "Staff" or badge == "Team":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{staffemo} **Staff / Team**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{staffemo} **Staff / Team **")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)
    elif badge == "Bug" or badge == "bug":
        with open("badges.json", "r") as f:
            idk = json.load(f)
        if str(user.id) not in idk:
            idk[str(user.id)] = []
            idk[str(user.id)].append(f"{bugemo} **Bug Hunter**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        elif str(user.id) in idk:
            idk[str(user.id)].append(f"{bugemo} **Bug Hunter**")
            await ctx.reply(f"{tick} | Added badge {badge} to {user}.",
                            mention_author=False)
        with open("badges.json", "w") as f:
            json.dump(idk, f, indent=4)


@bot.command(aliases=["profile"])
async def badges(ctx, member: discord.Member = None):
    user = member or ctx.author
    with open("badges.json", "r") as f:
        idk = json.load(f)
    if str(user.id) not in idk:
        await ctx.reply(f"{user} Have no badges.", mention_author=False)
    elif str(user.id) in idk:
        embed = discord.Embed(color=discord.Colour(0x2f3136),
                              title="Badges:",
                              description="")
        for bd in idk[str(user.id)]:
            embed.description += f"{bd}\n"
        embed.set_author(name=f"{user.name}#{user.discriminator}",
                         icon_url=user.display_avatar.url)
        await ctx.reply(embed=embed, mention_author=False)


@bot.command(aliases=['rbadges'])
@commands.is_owner()
async def removebadge(ctx, user: discord.User = None):
    if user is None:
        await ctx.reply("You must specify a user to remove badge.")
        return
    with open('badges.json', 'r') as f:
        badges = json.load(f)
    try:
        if str(user.id) in badges:
            badges.pop(str(user.id))

            with open('badges.json', 'w') as f:
                json.dump(badges, f, indent=4)

            await ctx.reply(f"Removed badge of {user}")
    except KeyError:
        await ctx.reply("This user has no badge.")


















@bot.command()
async def dbadge(ctx, user: discord.Member):
    hypesquad_class = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()

    
    hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])
    embed = discord.Embed(title=f"{user.name} User's Badges", description=f"{hypesquad_class}", color=0x0000)
    await ctx.channel.send(embed=embed)
    


@bot.command(aliases=['lbadges'])
async def listbadges(ctx):
    listem = discord.Embed(description="""```
- Team
- Mod
- Admin
- Manager
- owner
- Dev
```
""", color=0000 , )
    listem.set_footer(text="Nade With '💖' By Team Alpha", icon_url='https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024')
    listem.set_author(name="list of badges | infinix ",  icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024")
    await ctx.send(embed=listem)


@bot.command(aliases=['nbadges' , 'needbadge'])
async def needbadges(ctx):
    nb = discord.Embed(description="**Need Badges ???** \n      > [Right Here!!](https://discord.gg/7srHc2aqQk) ", color=0000)
    nb.set_footer(text="Nade With '💖' By Team Alpha", icon_url='https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=1024')
    await ctx.send(embed=nb)


@bot.command(aliases=['txt' , 't'])
async def text(ctx,*,t):
    await ctx.message.delete()
    await ctx.send(f'{t} | {ctx.author}')

    













    








@bot.command()
@commands.is_owner()
async def dm(ctx, user: discord.User, *, message):
    message = message 
    await ctx.send('dm message send')
    await user.send(message)






async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(filename + "  loaded")
async def main():
    await load()
    await bot.load_extension('jishaku')
    await bot.start(token)

asyncio.run(main())








