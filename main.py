import discord
import os
from dotenv import load_dotenv
import sys

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
client = discord.Client()

emoji = discord.utils.get(message.guild.emojis, name="angy_tubby")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author ==  client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send(f'Kono aida {emoji}')
        await channel.send(file=discord.File('./images/angly_tubby.png'))


client.run(TOKEN)
