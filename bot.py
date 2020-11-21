import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('Nzc3MDM4NTA3ODM0MzQzNDQ1.X69ngA.rG-9rnDMFK2kEMgcnfh0HKzReA8')