import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import sys
from feature import pong

print(pong.Pong.pong(1000))

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
description = 'Angry Tubby'

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name="angy_tubby")
    await ctx.send(f'Kono aida {emoji}')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(pong.Pong.pong(int(bot.latency)))

bot.run(TOKEN)
