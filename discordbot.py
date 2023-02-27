from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
from nturl2path import url2pathname
from turtle import color, update
import random
from discord.colour import Color
import datetime
import pytz
from discord.ext import tasks
from itertools import cycle
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

status = cycle([".명령어"])

@tasks.loop(seconds=5) 
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    
@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    change_status.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
    if message.content == ".내정보":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id)>>22) + 1420070400000) / 1000)
        embed = discord.Embed(color = 0xffd400)
        embed.add_field(name="이름" , value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임" , value=message.author.display_name, inline=True)
        embed.add_field(name="가입일" , value= str(date.year) + '년' + str(date.month) + '월' + str(date.day) + '일' , inline=True)
        embed.add_field(name="아이디" , value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar)
        embed.set_footer(text="Bot Made by. CSD_KIG#6176")
        await message.channel.send(embed=embed)
        await message.delete()

        
    if message.content.startswith (".청소"):
       
        if  True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="청소 완료", description="디스코드 채팅 {}개가\n {}님의 요청으로 삭제 되었습니다.".format(amount, message.author), color =  0xffd400)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
       
    if message.content == ".명령어":
            embed = discord.Embed(title="명령어를 알려드리겠습니다.", description="명령어는 총 20개입니다.", color = 0xffd400)
            embed.set_footer(text=명령어 + "Bot Made by. CSD_KIG#6176")
            await message.channel.send(embed=embed)   
            await message.delete()


    if message.content == ".봇기능공지":
            embed = discord.Embed(title="KIG(bot) 업데이트 소식", description="역할 해제 기능 추가되었습니다", color = 0xffd400)
            embed.set_footer(text=봇기능공지 + "                Bot Made by. CSD_KIG#6176")
            await message.channel.send(embed=embed)   
            await message.delete()


    if message.content == ".봇기능공지":
        await message.channel.send("@everyone")
        await message.delete()        
     

    if message.content == ".역할 사용법":
            embed = discord.Embed(title="역할 지급 받는방법", description= "Ex (.1역할 @이름 <-- 이렇게 써주시면 역할이 지급됩니다.)", color = 0xffd400)
            embed.set_footer(text = "또한 자신이 해당되는 반에 숫자만 적어주세요." + "                Bot Made by. CSD_KIG#6176")
            await message.channel.send(embed=embed)     
            await message.delete()


    if message.content == ".역할삭제 사용법":
            embed = discord.Embed(title="역할 삭제 받는방법", description= "Ex (.1역할삭제 @이름 <-- 이렇게 써주시면 역할이 삭제됩니다.)", color = 0xffd400)
            embed.set_footer(text = "또한 자신이 해당되는 반에 숫자만 적어주세요." + "                Bot Made by. CSD_KIG#6176")
            await message.channel.send(embed=embed)     
            await message.delete()


    if message.content.startswith (".1역할 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="1반 역할", description="1반 역할 지급이 완료 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="1반 역할을 받는 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="역할 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '1반')
            await user.add_roles(role)


    if message.content.startswith (".2역할 "):
       
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="2반 역할", description="2반 역할 지급이 완료 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="2반 역할을 받는 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="역할 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '2반')
            await user.add_roles(role)

    if message.content.startswith (".3역할 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="3반 역할", description="3반 역할 지급이 완료 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="3반 역할을 받는 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="역할 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '3반')
            await user.add_roles(role)


    if message.content.startswith (".4역할 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="4반 역할", description="4반 역할 지급이 완료 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="4반 역할을 받는 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="역할 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '4반')
            await user.add_roles(role)
  

    if message.content.startswith (".5역할 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="5반 역할", description="5반 역할 지급이 완료 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="5반 역할을 받는 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="역할 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '5반')
            await user.add_roles(role)

    if message.content.startswith (".1역할삭제 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="1반 역할", description="1반 역할 삭제 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="삭제 요망 대상자", value=f"{user.name} ( {user.mention} )", inline=True)
            embed.add_field(name="삭제 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=True)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '1반')
            await user.remove_roles(role)


    if message.content.startswith (".2역할삭제 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="2반 역할", description="2반 역할 삭제 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="삭제 요망 대상자", value=f"{user.name} ( {user.mention} )", inline=True)
            embed.add_field(name="삭제 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=True)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '2반')
            await user.remove_roles(role)


    if message.content.startswith (".3역할삭제 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="3반 역할", description="3반 역할 삭제 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="삭제 요망 대상자", value=f"{user.name} ( {user.mention} )", inline=True)
            embed.add_field(name="삭제 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=True)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '3반')
            await user.remove_roles(role)

                                        
    if message.content.startswith (".4역할삭제 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="4반 역할", description="4반 역할 삭제 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="삭제 요망 대상자", value=f"{user.name} ( {user.mention} )", inline=True)
            embed.add_field(name="삭제 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=True)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '4반')
            await user.remove_roles(role)


    if message.content.startswith (".5역할삭제 "):
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="5반 역할", description="5반 역할 삭제 되었습니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffd400)
            embed.add_field(name="삭제 요망 대상자", value=f"{user.name} ( {user.mention} )", inline=True)
            embed.add_field(name="삭제 명령어 사용자", value=f"{message.author} ( {message.author.mention} )", inline=True)
            embed.set_footer(text="Bot Made by. CSD_KIG#6176")
            await message.channel.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '5반')
            await user.remove_roles(role)  

                
    if message.content ==".매괴고 1":
        embed = discord.Embed(title="2학년 시간표", description="2학년 1반 시간표", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1079774514285654086/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이투)
        await message.channel.send(embed=embed)                     
        await message.delete()

    if message.content ==".매괴고 2":
        embed = discord.Embed(title="2학년 시간표", description="2학년 2반 시간표", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1079775471639740448/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이투)
        await message.channel.send(embed=embed)
        await message.delete()

    if message.content ==".매괴고 3":
        embed = discord.Embed(title="2학년 시간표", description="2학년 3반 시간표", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1079774969157914654/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이투)
        await message.channel.send(embed=embed)  
        await message.delete()

    if message.content ==".매괴고 4":
        embed = discord.Embed(title="2학년 시간표", description="2학년 4반 시간표", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1079775113337114695/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이투)
        await message.channel.send(embed=embed) 
        await message.delete()

    if message.content ==".매괴고 5":
        embed = discord.Embed(title="2학년 시간표", description="2학년 5반 시간표", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1079775181964320848/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이투)
        await message.channel.send(embed=embed)   
        await message.delete()

    if message.content ==".급식":
        embed = discord.Embed(title="매괴고등학교 급식", description="밥 쳐 묵자", color =  0xffd400)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1007612813327470702/1078996724405772309/image.png")
        embed.set_footer(text="Bot Made by. CSD_KIG#6176" + 업데이트)
        await message.channel.send(embed=embed)    
        await message.delete()

    if message.content == ".룰렛":
        ran = random.randint(0,26)
        if ran == 0:
            s = ":heart::heart::heart:"
        if ran == 1:
            s = ":yellow_heart::yellow_heart::yellow_heart:"
        if ran == 2:
            s = ":blue_heart::blue_heart::blue_heart:"
        if ran == 3:
            s = ":heart::yellow_heart::blue_heart:" 
        if ran == 4:
            s = ":heart::blue_heart::yellow_heart:"       
        if ran == 5:
            s = ":yellow_heart::heart::blue_heart:"
        if ran == 6:
            s = ":yellow_heart::blue_heart::heart:"
        if ran == 7:
            s = ":blue_heart::heart::yellow_heart:"
        if ran == 8:
            s = ":blue_heart::yellow_heart::heart:" 
        if ran == 9:
            s = ":heart::heart::yellow_heart:"
        if ran == 10:
            s = ":heart::heart::blue_heart:"
        if ran == 11:
            s= ":yellow_heart::yellow_heart::heart:"
        if ran == 12:
            s = ":yellow_heart::yellow_heart::blue_heart:"    
        if ran == 13:
            s = ":blue_heart::blue_heart::heart:"      
        if ran == 14:
            s = ":blue_heart::blue_heart::yellow_heart:"
        if ran == 15:
            s = ":heart::yellow_heart::yellow_heart:"
        if ran == 16:
            s = ":heart::blue_heart::blue_heart:"
        if ran == 17:
            s = ":yellow_heart::heart::heart:"   
        if ran == 18:
            s = ":yellow_heart::blue_heart::blue_heart:"
        if ran == 19:
            s = ":blue_heart::heart::heart:"
        if ran == 20:
            s = ":blue_heart::yellow_heart::yellow_heart:"                                   
        if ran == 21:
            s = ":heart::yellow_heart::heart:"
        if ran == 22:
            s = ":heart::blue_heart::heart:"
        if ran == 23:
            s = ":yellow_heart::heart::yellow_heart:"
        if ran == 24:
            s = ":yellow_heart::blue_heart::yellow_heart:"
        if ran == 25:
            s = ":blue_heart::heart::blue_heart:"
        if ran == 26:
            s = ":blue_heart::yellow_heart::blue_heart:"             

        await message.channel.send(s)        
    


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
