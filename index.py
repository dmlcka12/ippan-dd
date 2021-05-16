import discord
import asyncio
import random
import os
from discord.ext import commands
client  = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료")
    print(client.user)
    print("=========================")

@client.event
async def on_message(message): 
    if message.content == "!IPPAN":
        await message.channel.send("안녕하십니까 저는 이빤님의 충신 IPPAN봇 입니다")

    if message.content == "!test":
        await message.channel.send(":green_circle:  Online - IPPAN봇 정상 작동 중 입니다.")
    
    if message.content == "!초대":
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=843449362180997150&permissions=8&scope=bot")
    
    
    if message.content == "!랜덤":
        await message.channel.send(random.randint(1, 10))
    
    if message.content == "!타이머":
        await message.channel.send("10초 타이머가 시작됩니다")
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났습니다")
    
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 매세지가 삭제되었습니다.")

    if message.content == "!help":
        embed=discord.Embed(title="IPPAN BOT", description="made by euicham", color=0x62c1cc)
    embed.add_field(name="since", value="2021.5.16", inline=True)
    embed.add_field(name="!청소", value="매세지를 삭제합니다", inline=True)
    embed.add_field(name="!타이머", value="10초 타이머입니다!", inline=True)
    embed.add_field(name="!test", value="이빤봇의 상태를 확인시켜드립니다", inline=True)
    embed.add_field(name="!IPPAN", value="이빤의 인사말이 나와요", inline=True)
    embed.add_field(name="!랜덤", value="1~10 중에 아무숫자나 일단 틀어", inline=True)
    embed.add_field(name="!초대", value="IPPAN봇의 초대링크를 출력합니다", inline=True)
    embed.set_footer(text="with Strange Code")
    await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


