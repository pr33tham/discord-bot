import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!")

@client.event
async def on_member_remove(member):
    print(f"{member} has ;eft the server")


client.run("Nzc3MDM4NTA3ODM0MzQzNDQ1.X69ngA.rG-9rnDMFK2kEMgcnfh0HKzReA8")