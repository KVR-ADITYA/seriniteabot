import discord

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

client.run('ODQ2NzE0MDMwNzM1MjI4OTY4.YKzh5A.VDYg8lQckA1TobHrwjlox-98lP'+'Y')
