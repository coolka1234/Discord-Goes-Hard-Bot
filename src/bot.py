# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv('./env/.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    amogus_quotes = [
        'sus',
        'amogus',
    ]

    if message.content == 'sussy':
        response = random.choice(amogus_quotes)
        await message.channel.send(response)
    else:
        await message.channel.send('sussy')

client.run(TOKEN)