# bot.py
import os
import random
import sys

import discord
from dotenv import load_dotenv
import os
from classificator.predict import predict_if_hard
dir2_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
from create_meme import create_meme
import constants as const

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
    if predict_if_hard(message.content):
        chosen_template=random.randint(0, len(const.image_path)-1)
        create_meme(chosen_template, message.content)
        meme_path=os.path.abspath(const.name_to_save)
        await message.channel.send(file=discord.File(meme_path))


if __name__ == '__main__' and __package__ is None:
    client.run(TOKEN)
