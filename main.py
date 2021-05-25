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
    if message.author ==  client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Kono aida @here')
        await channel.send(file=discord.File('./images/angly_tubby.png'))


client.run(TOKEN)
