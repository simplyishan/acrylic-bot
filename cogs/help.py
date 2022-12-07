import discord
from discord.ui import View , Select 
from discord.ext import commands


class xd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(invoke_without_command=True , aliases=["Help" , 'h' ])
    async def help(self , ctx):
        embed = discord.Embed(color=0000, description=f"""
**• Global Prefix: +
• Total Cmd(s): 75+ | Guild(s): {len(self.bot.guilds)}
• use help <module>  to get more info
• Get [Acrylic](https://discord.com/api/oauth2/authorize?client_id=934760667234336798&permissions=8&scope=bot) | Support Soon | Vote Soon**
**
<:reply3:1003377442553081887> Modules
 <:reply:1003377407144759347><:dd_staff:1008011398611210270>  : Moderation
 <:reply:1003377407144759347><:Funny:1039949561847889962>  : Fun
 <:reply:1003377407144759347><:music:1038111736349335662>  : Music
 <:reply:1003377407144759347><:dd_spcl:1008012364672671940>  : Utilities 
 <:reply:1003377407144759347><:badgesupport:1040209478294978560>  : Badge
 <:reply:1003377407144759347><:games:1039938559878107178>  : Games
 <:reply:1003377407144759347><:calculator:1040294499215212544>  : Calculator
 <:reply:1003377407144759347><:Flantic_oki_oki:1039940119072866346>  : AutoResponder** """ , title='Arylic Help Menu.')
        # embed.add_field(name="<:reply3:1003377442553081887> help moderation", value="<:reply:1003377407144759347> shows moderation commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help fun ", value="<:reply:1003377407144759347> shows fun commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help music ", value="<:reply:1003377407144759347> shows music commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help utilities ", value="<:reply:1003377407144759347> shows utilities commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help badge ", value="<:reply:1003377407144759347> shows badges commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help games ", value="<:reply:1003377407144759347> shows games commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help calculator ", value="<:reply:1003377407144759347> shows calc commands", inline=False)
        # embed.add_field(name="<:reply3:1003377442553081887> help autoresponder ", value="<:reply:1003377407144759347> shows ar commands", inline=False)
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/ogejA4OsyABuwbvb2T-H6C0CIPtkpuT2DClZBrpPwqU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1039203095722348604/b572c4fa1e0cd559644741cb03e46813.png?width=598&height=598")
        # embed.set_author(name="Acrylic Commands", url="https://discord.gg/7srHc2aqQk", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        embed.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        select = Select(placeholder='help menu!',options=[
                discord.SelectOption(label='Moderation ' , value=1, description='mod commands' , emoji='<:dd_staff:1008011398611210270>'),
                discord.SelectOption(label='Fun' , value=2, description='fun commands' , emoji='<:Funny:1039949561847889962>'),
                discord.SelectOption(label='Music' , value=3, description='music commands', emoji='<:music:1038111736349335662>'),
                discord.SelectOption(label='Utilities' , value=4, description='utilities commands', emoji='<:dd_spcl:1008012364672671940>'),
                discord.SelectOption(label='Badge' , value=5, description='badges commands', emoji='<:badgesupport:1040209478294978560>'),
                discord.SelectOption(label='Games' , value=6, description='games commands', emoji='<:games:1040216158521008128>'),
                discord.SelectOption(label='Calulator' , value=7, description='calculator commands', emoji='<:calculator:1040294499215212544>'),
                discord.SelectOption(label='AutoResponder' , value=8, description='AutoResponder commands', emoji='<:Flantic_oki_oki:1039940119072866346>')
                ])
                
                

        async def mycallback(interaction):
            if select.values[0] == "1":
                feembedd = discord.Embed(color=0000 , description='''```clone | unban | unblock | block | ban | steal | delemoji | warn | removeallhumans | removeallbots mute | timeout | unmute | kick | enlarge | giveallhumans | giveallbots | softban 
        purge - 
	        startswith
	        endswith
	        contains
	        user
	        invites 
    ```''')
                feembedd.set_author(name="Moderation Commands", icon_url="https://cdn.discordapp.com/emojis/1008011398611210270.webp?size=128&quality=lossless")
                feembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=feembedd,  ephemeral=True)
            elif select.values[0] == "2":
                eembedd = discord.Embed(color=0000 , description='```fban | avatar | avatar server | text | quote | code | gender | bold | censor | underline ```')
                eembedd.set_author(name="Fun Commands", icon_url="https://cdn.discordapp.com/emojis/1038111929517998201.webp?size=56&quality=lossless")
                eembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=eembedd,  ephemeral=True)
            elif select.values[0] == "3":
                membedd = discord.Embed(color=0000 , description='``` join | play | stop | volume | loop | skip | queue | leave |  pause | resume ```')
                membedd.set_author(name="Music Commands", icon_url="https://cdn.discordapp.com/emojis/1038111736349335662.webp?size=56&quality=lossless")
                membedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=membedd,  ephemeral=True)    
            elif select.values[0] == "4":
                w = discord.Embed(color=0000 , description='``` bug | status | user | role | channel | boosts | userinfo | servericon | membercount | invite | serverinfo ```')
                w.set_author(name="utilities Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
                w.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=w,  ephemeral=True)    
            elif select.values[0] == "5":
                b = discord.Embed(color=0000 , description='``` listbadges | badges | dbadges | addbadge | removebadge | needbadges ```')
                b.set_author(name="badges Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
                b.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=b,  ephemeral=True)
            elif select.values[0] == "6":
                btng = discord.Embed(color=0000 , description='``` tnd | Tictactoe | rps```')
                btng.set_author(name="games Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
                btng.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=btng,  ephemeral=True)       
            elif select.values[0] == "7":
                clem = discord.Embed(color=0000 , description='``` add | sub | div | multi ```')
                clem.set_author(name="Calculator Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
                clem.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=clem,  ephemeral=True)         
            elif select.values[0] == "8":
                eclem = discord.Embed(color=0000 , description='``` autoresponder create | autorespondercreate edit | autorespondercreate list | autorespondercreate delete ```\n`*`**ALIAS FOR "AUTORESPONDOR" IS "A"**')
                eclem.set_author(name="Calculator Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
                eclem.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
                await interaction.response.send_message(embed=eclem,  ephemeral=True)                 
        select.callback = mycallback
        view = View()
        view.add_item(select)        
        await ctx.send(embed=embed, view=view)

    @help.command(aliases=["f" , 'fn' ])
    async def fun(self , ctx):
        fembedd = discord.Embed(color=0000 , description='```fban | avatar | avatar server | text | quote | code | gender | bold | censor | underline```')
        fembedd.set_author(name="Fun Commands", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        fembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=fembedd)
    @help.command(aliases=["md" , 'mod' ])
    async def moderation(self , ctx):
        fembedd = discord.Embed(color=0000 , description='''```clone | unban | unblock | block | ban | steal | delemoji | warn | removeallhumans | removeallbots mute | timeout | unmute | kick | enlarge | giveallhumans | giveallbots | softban 
        purge - 
	        startswith
	        endswith
	        contains
	        user
	        invites
    ```''')
        fembedd.set_author(name="Moderation Commands", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        fembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=fembedd)  
    
    @help.command(aliases=["ms" , 'Musics' ])
    async def music(self , ctx):
        fembedd = discord.Embed(color=0000 , description='``` join | play | stop | volume | loop | skip | queue | leave |  pause | resume ```')
        fembedd.set_author(name="Music Commands", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        fembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=fembedd)  
    @help.command(aliases=["ut" , 'Utilities' ])
    async def utilities(self , ctx):
        fembedd = discord.Embed(color=0000 , description='``` bug | status | user | role | channel | boosts | userinfo | servericon | membercount | invite | serverinfo ```')
        fembedd.set_author(name="Music Commands", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        fembedd.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=fembedd)  


    @help.command(aliases=['b' , 'profile'])
    async def badge(self,ctx):
        bb = discord.Embed(color=0000 , description='``` listbadges | badges | dbadges | addbadge | removebadge | needbadges ```')
        bb.set_author(name="badges Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
        bb.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=bb)
#  ------------------------



    @help.command(aliases=['game'])
    async def games(self,ctx):
        btnn = discord.Embed(color=0000,title='Games(6/8)',description='` +Tictactoe <player1> <player2>`\narrange a tictactoe match for both players\n\n` +TnD `\nLets you play truth and dare\n\n` +rps `\nlets you play rock paper scissors with ai')
        btnn.set_footer(text="Acrylic • Page 1/1", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=btnn)


    # @help.command(aliases=['game'])
    # async def games(self,ctx):
    #     btnn = discord.Embed(description='```TnD | Tictactoe | rps ```')
    #     btnn.set_author(name="games Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
    #     btnn.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
    #     await ctx.send(embed=btnn)

#  ------------------------


    @help.command(aliases=['calc' , 'cal' , 'm' , 'math'])
    async def calculator(self,ctx):
        clem = discord.Embed(color=0000 , description='` +add <no1> <no2> `\nadds two number also decimals\n\n` +sub <no1> <no2> `\nsubs two numbers\n\n` +div <no1> <no2> `\ndivides two numbers\n\n` +multi <no1> <n2? `\nMultiplies two number',title='Calculator/Math(7/8)')
        clem.set_footer(text="Acrylic • Page 1/1", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=clem) 



    # @help.command(aliases=['calc' , 'cal' , 'm' , 'math'])
    # async def calculator(self,ctx):
    #     clem = discord.Embed(color=0000 , description='``` add | sub | div | multi ```')
    #     clem.set_author(name="Calculator Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
    #     clem.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
    #     await ctx.send(embed=clem) 





#  ------------------------
    # @help.command(aliases=['arr' , 'Arr'])
    # async def autoresponder(self,ctx):
    #     clem = discord.Embed(color=0000 , description='``` autoresponder create | autorespondercreate edit | autorespondercreate list | autorespondercreate delete ```\n`*`**ALIAS FOR "AUTORESPONDOR" IS "A"**')
    #     clem.set_author(name="AutoResponder Commands", icon_url="https://cdn.discordapp.com/emojis/1008012364672671940.webp?size=128&quality=lossless")
    #     clem.set_footer(text="Made With `💖` By Team Celestials", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
    #     await ctx.send(embed=clem)      



    @help.command(aliases=['arr' , 'Arr'])
    async def autoresponder(self,ctx):
        clem = discord.Embed(color=0000,description="""
        `+autoresponder/ar create <name> <subject>`
makes/create a autoresponder\n
`+autoresponder/ar edit <name> <newsubject>`
recreate/edit a autoresponder\n
`+autoresponder/ar list `
show list of all autoresponder\n
`+autoresponder/ar delete <name> `
remove/deletes a autoresponder\n
""", title='AutoResponder(8/8)')
        clem.set_footer(text="Acrylic • Page 1/1", icon_url="https://cdn.discordapp.com/avatars/638073011236372480/49cf9dfd06e02aa93b1a829f85002c1d.png?size=256")
        await ctx.send(embed=clem)  


async def setup(bot):
    await bot.add_cog(xd(bot))
