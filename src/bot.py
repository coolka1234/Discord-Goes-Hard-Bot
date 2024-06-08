# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv('./env/.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents=discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True
intents.reactions = True
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

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
        print(f'{message.author} said: {message.content}')
        await message.channel.send('sussy')

client.run(TOKEN)