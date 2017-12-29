import openweathermapy.core as weather
import unicodedata
import youtube_dl
import pyowm
import traceback
import os
import sys
import sqlite3
import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime
import aiohttp
import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
import ftfy
#You don't need all these imports for this file, just was lazy ;p

@bot.command(pass_context=True)
async def tutinfo(ctx):
    embed = discord.Embed(title = "Cosmos Commands", color = 0xfffa02, timestamp = datetime.datetime.utcnow())
    embed.set_author(name = "Information on Cosmos Examples", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    embed.add_field(name = "What is it?", value = "Cosmos examples are simple pieces of code that are made by Rapid(me), and set as a command, for people that need help, examples or ideas of commands/code.")
    embed.add_field(name = "What kind of code/language is it?", value = "The code is using the Async library of the language Python, discord.py.")
    embed.add_field(name = "Can I request my code to be here?", value = "Soon, Rapid will be working on a command that allows you to direct message him, for any purposes. Following, a system for your code sent to Rapid to be debated on, and published to a command similar to 'tut', but more so like 'communitytut'.")
    embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    await bot.say(embed = embed)

oo = 14
@bot.command()
async def tutPING():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Ping** command.\n```@bot.command()\nasync def ping():\n    await bot.say('Pong!')```")
    embed.set_author(name = "Example 1 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutBASICBOT():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description ="Simple **Bot setup.**\n```import discord\n\nbot = commands.Bot(command_prefix='PREFIX')\n\n@bot.event\nasync def on_ready():\n    print('I'm Ready!')\n\n@bot.command()\nasync def ping():\n    await bot.say('Pong!')\n\nbot.run('TOKEN')```")
    embed.set_author(name = "Example 2 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutCOINFLIP():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Coinflip** command.```@bot.command()\nasync def coinflip():\n    choice = random.randint(1,2)\n    if choice == 1:\n       await bot.say('**:hear_no_evil:  |  Heads!**')\n    if choice == 2:\n       await bot.say('**:monkey:  |  Tails!**')```")
    embed.set_author(name = "Example 3 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command()
async def tutSAY():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **Say** command, deletes your command message, and the bot repeats your message.```@bot.command(pass_context=True)\nasync def say(ctx,*, message: str):\n    await bot.delete_message(ctx.message)\n    await bot.say(message)```")
    embed.set_author(name = "Example 4 of {}".format(oo))
    await bot.say(embed = embed)
   
@bot.command()
async def tutTYPES():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "All of the presence types you can set for different status types.\nType 0: `Game (playing)`\nType 1: `Stream (streaming)`\nType 2: `Listen (listening to)`\nType 3: `Watch (watching)`")
    embed.set_author(name = "Example 7 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutSERVERS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing how many servers thr bot is on.```@bot.command()\nasync def servercount():\n    await bot.say(len(bot.servers))```")
    embed.set_author(name = "Example 8 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command()
async def tutCHANNELS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all the channels the bot can see.```@bot.command()\nasync def channelcount():\n    await bot.say(len(bot.servers))```")
    embed.set_author(name = "Example 9 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command()
async def tutMEMBERS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all members the bot can see.```@bot.command()\nasync def membercount():\n    await bot.say(len(set(bot.get_all_members())))```")
    embed.set_author(name = "Example 10 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutEMOJIS():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command showing all the custom emojis the bot can see.```@bot.command()\nasync def emojicount():\n    await bot.say(len(set(bot.get_all_emojis())))```")
    embed.set_author(name = "Example 11 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutERRORHANDLER():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple **command error handler**```@bot.event\nasync def on_command_error(error, ctx):\n    if isinstance(error, commands.CommandOnCooldown):\n      await bot.send_message(ctx.message.channel, 'This command is on cooldown.')\n\n    elif isinstance(error, commands.CommandNotFound):\n      await bot.send_message(ctx.message.channel, 'This command was not found.')```\nMake the **cooldown** command```@bot.command()\n@commands.cooldown(1, 30, commands.BucketType.user)\nasync def blah():\n    await bot.say('Wasgud :D')```\n__**Definitions**__:book:\n`1, 30` - **1** command every **30** seconds.")
    embed.set_author(name = "Example 12 of {}".format(oo))
    await bot.say(embed = embed)
    
@bot.command()
async def tutSETGAME():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple command for setting the bots **playing status** on command```@bot.command(pass_context=True, aliases=['setg', 'sg'])\nasync def setgame(ctx, *, text):\n    if ctx.message.author.id == 'YOUR ID': < this will make the command only accessible by you.\n      game = discord.Game(name='%s'% text)\n      await bot.change_status(game)\n      await bot.say('Done!')```")
    embed.set_author(name = "Example 13 of {}".format(oo))
    await bot.say(embed = embed)

@bot.command()
async def tutTERMUX():
    embed = discord.Embed(title = "Cosmos Examples", color = 0xfffa02, description = "Simple setup for coding on Android, with Termux.\n\nPart 1\nWhen you first open Termux, you need to do a few things:\n1. `pkg install nano`\n2. `pkg install python or nodejs`\n3. `pkg install git`\n4. `pip install discord`\n`Nano` let's you edit or create files. `Python` or `NodeJS`  determines a what languages you can use to code. You can use as many as you want, but each file can obviously only use 1. Now, install `Hackers Keyabord` app from the playstore so you can use specific functions to actually code.\n\nPart 2\nNow, to begin coding type, `nano (filename).py` or `nano bot.js` e.g. `nano bot.py`. Now, you can import discord with `import discord` and begin your code! If you need an example for starters, type **?tutBASICBOT**, and I'll send some code;)\n\nPart 3\nTo use functions and save, etc...\nWhen your in your code open `Hackers Keyboard`, Then press `ctrl` > `x` `(savename)` > `y`\nTo cut text(by lines) do `ctrl` > `k`\nTo show line numbers do `esc` > `ctrl` > `#`\n\n(PYTHON) - To run your bot type `python (filename).py`\n(NODE) - To run your bot type `node (filename).js`")
    embed.set_author(name = "Example 14 of {}".format(oo))
    await bot.say(embed = embed)
    
def setup(bot): 
    bot.add_cog(Asynchowto(bot))
