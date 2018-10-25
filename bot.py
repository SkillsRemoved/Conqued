import discord
from discord.ext import commands
import asyncio

client= commands.Bot(command_prefix='c!')

@client.event
async def on_ready():
    print('The bot is ready!')
    print(client.user.name)
    print(client.user.id)
    print('----------------------------')

client.run ('NTAyMzE4NzY3NzM3NTM2NTEy.DrLN5g.OsjA1dH_T-82Q-BLDkb2xvy34BY')
