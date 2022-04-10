# bot.py
import os
import user
import asyncio

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )



@client.event
async def on_message(message):

    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    if message.content.startswith('duckConnect'):

        member_names = []
        y = 0
        for members in guild.members:
            if y < len(guild.members):
                names = user.User(members)
                member_names.append(names)
                print(f'Guild Members:\n - {members}')
                y += 1


        Dict = {}
        me = message.author
        for x in me.roles:
            for y in member_names:
                for z in y.roles:
                    if x == z:                       
                        y.counter += 1
                        Dict[y] = y.counter

        # sort Dict 
        sorted_d = {}
        sorted_keys=sorted(Dict,key=Dict.get)

        p = str(me)
        count = 0
        for o in sorted_keys:
            t = str(o)
            if t == p:
                del sorted_keys[count]
            else:
                count +=1
        print(sorted_keys)

        for w in sorted_keys:
            sorted_d[w] = Dict[w]


        if len(sorted_d) < 5:
            msg = 'e'
            await message.channel.send(msg)
            
        else:
            key1 = list(sorted_d.keys())
            msg = 'Hey' + f'{message.author.mention}'', we noticed that these 5 people have a lot in common with you \n'+ '$$$ '+ key1[-1].name + '\n' + '$$$ ' + key1[-2].name + '\n' + '$$$ ' + key1[-3].name + '\n' + '$$$ ' + key1[-4].name + '\n' + '$$$ ' + key1[-5].name 
            await message.channel.send(msg)




client.run(TOKEN)
