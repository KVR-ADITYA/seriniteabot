import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import sys
from feature import ping

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix = '!') 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    emoji = discord.utils.get(message.guild.emojis, name="angy_tubby")
    if message.author ==  bot.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send(f'Kono aida {emoji}')

@bot.command(aliases = ['Ping','PING'])
async def ping(ctx):
    await ctx.send(ping.Ping.ping(bot.latency))

bot.run(TOKEN)
