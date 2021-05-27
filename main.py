import discord
import os
from dotenv import load_dotenv
import sys

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    emoji = discord.utils.get(message.guild.emojis, name="angy_tubby")
    if message.author ==  client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send(f'Kono aida {emoji}')


client.run(TOKEN)
