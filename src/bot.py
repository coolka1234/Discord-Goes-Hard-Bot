# bot.py
import os
import random
import sys

import discord
from dotenv import load_dotenv
import os
dir2_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
from create_meme import create_meme

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
    if message.author == client.user or message.content.startswith('!') or message.content.startswith('http') or message.content.startswith('https') or message.content.startswith('<'):
        return
    if message.content == 'raise-exception':
        raise discord.DiscordException
    if len(message.content) > 200:
        await message.channel.send('Message is too long')
        return
    if ' ' not in message.content:
        await message.channel.send('Message is too short')
        return
    create_meme('meme1', message.content)
    meme_path=os.path.abspath('./res/smoking_caterpillar_new.jpg')
    await message.channel.send(file=discord.File(meme_path))


if __name__ == '__main__' and __package__ is None:
    client.run(TOKEN)
