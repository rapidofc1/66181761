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
import discord
from discord.ext import commands
#from cogs import admin, fun, dev, utility, misc, core, minigames, rtfm, asynchowto

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"))
bot.remove_command ('help')

#extensions = ["commands.dev", 
#              "commands.fun", 
#              "commands.misc", 
#              "commands.admin",
#              "commands.utility", 
#              "commands.core", 
#              "commands.minigames",
#              "commands.rtfm",
#              "commands.asynchowto"]

@bot.event
async def on_ready():
    print("------------")
    print(" Logged in.")
    print("⭐Bot Ready⭐")
    print("------------")
    
startup_extensions = ["cogs.Dev", "cogs.Fun", "cogs.Misc", "cogs.Admin", "cogs.Utility", "cogs.Core", "cogs.Minigames", "cogs.Rtfm", "cogs.Asynchowto"]
    
for cog in startup_extensions:
        try:
                bot.load_extension(cog)
        except Exception as error:
                print(str(error))
  
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
      await bot.send_message(ctx.message.channel, "**:x: | This command is on cooldown, try again later.**")

#    elif isinstance(error, commands.CommandNotFound):
#      await bot.send_message(ctx.message.channel, "**:x: | That command was not found! Type ?help for a list of commands.（￣～￣;）**")

   # elif isinstance(error, commands.InvalidArgument):
      #await bot.send_message(ctx.message.channel, f'**:x: | Invalid argument in command {ctx.command}. (」ﾟﾛﾟ)｣**')

    print('Ignoring exception in command {}:'.format(ctx.command), file = sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file = sys.stderr)
    
  
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif "cosmos" in message.content:
      await bot.send_message(message.channel, (random.choice(["Yes?", "No", "How is that even possible...", "He's an asshole.","\n😎😎😎😎😎😎😎\n👍   I'm so cool!   👍\n💋😏😏😏😏😏💋\n👌🚀🚀🚀🚀🚀👌\n🚗📷📷📷📷📷🚗\n😈😈😈😈😈😈😈", "Sure, ig", "╮(╯▽╰)╭","IMPOSSIBRUUUUU", "( ˘ ³˘)❤", "(づ￣ ³￣)づ", "(っ˘̩╭╮˘̩)っ", "<(⇀‸↼‶)>", "(〜￣△￣)〜", "Take your question, and shove it up the bumof the guy below. 🔽", "Talk to the hand  ✋", "Last night I held a lovely hand,\nIt was so small and neat,\nI thought my heart withjoy would burst\nSo wild was every beat.\n\nNo other hand unto my heart\nCould greater pleasure bring \nThan the one so dear I heldlast night.\nFour Aces and a King",  "(●__●)",  "Wow",  "WTF",  "w0t",  "😉"])))
    elif "Cosmos" in message.content:
      await bot.send_message(message.channel, (random.choice(["Yes?", "No", "How is that even possible...", "He's an asshole.","\n😎😎😎😎😎😎😎\n👍I'm so cool!👍\n💋😏😏😏😏😏💋\n👌🚀🚀🚀🚀🚀👌\n🚗📷📷📷📷📷🚗\n😈😈😈😈😈😈😈", "Sure, ig", "╮(╯▽╰)╭","IMPOSSIBRUUUUU", "( ˘ ³˘)❤", "(づ￣ ³￣)づ","(っ˘̩╭╮˘̩)っ", "<(⇀‸↼‶)>", "(〜￣△￣)〜", "Take your question, and shove it up the bumof the guy below. 🔽", "Talk to the hand  ✋", "Last night I helda lovely hand,\nIt was so small and neat,\nI thought my heart withjoy would burst\nSo wild was every beat.\n\nNo other hand unto my heart\nCouldgreater pleasure bring \nThan the one so dear I heldlast night.\nFour Aces and a King",  "(●__●)",  "Wow",  "WTF",  "w0t",  "😉"])))
    elif "COSMOS" in message.content:
      await bot.send_message(message.channel, (random.choice(["Yes?", "No", "How is that even possible...", "He's an asshole.","\n😎😎😎😎😎😎😎\n👍I'm so cool!👍\n💋😏😏😏😏😏💋\n👌🚀🚀🚀🚀🚀👌\n🚗📷📷📷📷📷🚗\n😈😈😈😈😈😈😈", "Sure, ig", "╮(╯▽╰)╭","IMPOSSIBRUUUUU", "( ˘ ³˘)❤", "(づ￣ ³￣)づ","(っ˘̩╭╮˘̩)っ", "<(⇀‸↼‶)>", "(〜￣△￣)〜", "Take your question, and shove it up the bumof the guy below. 🔽", "Talk to the hand  ✋", "Last night I helda lovely hand,\nIt was so small and neat,\nI thought my heart withjoy would burst\nSo wild was every beat.\n\nNo other hand unto my heart\nCouldgreater pleasure bring \nThan the one so dear I heldlast night.\nFour Aces and a King",  "(●__●)",  "Wow",  "WTF",  "w0t",  "😉"])))
    elif "Rapid" in message.content:
      msg=await bot.send_message(message.channel, "IS GAY")
      await bot.add_reaction(message, "🙇")
      await asyncio.sleep(0.5)
      await bot.edit_message(msg, "**Wait nvm YOU ARE ƪ(˘ᴗ˘)┐**")
      await bot.add_reaction(msg, "✋🏻")
      await bot.add_reaction(msg,"☝️🏻")
    elif "Poll:" in message.content:
      await bot.add_reaction(message, "👍")
      await bot.add_reaction(message, "🤷")
      await bot.add_reaction(message, "👎")
    elif "poll:" in message.content:
      await bot.add_reaction(message, "👍")
      await bot.add_reaction(message, "🤷")
      await bot.add_reaction(message, "👎")
    elif "sos" in message.content:
      await bot.add_reaction(message, "🆘")
      await bot.send_message(message.channel, "**:white_check_mark: | Dialed 911!**")
      await asyncio.sleep(10)
      await bot.send_message(message.channel, "**:rotating_light: | We're here nubs, watcha need?**")
    elif "Sos" in message.content:
      await bot.add_reaction(message, "🆘")
      await bot.send_message(message.channel, "**:white_check_mark: | Dialed 911!**")
      await asyncio.sleep(10)
      await bot.send_message(message.channel, "**:rotating_light: | We're here nubs, watcha need?**")
    elif "SOS" in message.content:
      await bot.add_reaction(message, "🆘")
      await bot.send_message(message.channel, "**:white_check_mark: | Dialed 911!**")
      await asyncio.sleep(10)
      await bot.send_message(message.channel, "**:rotating_light: | We're here nubs, watcha need?**")
    else:
        await bot.process_commands(message)
    
async def my_background_task():
    await bot.wait_until_ready()
    servs = (len(bot.servers))
    users = (len(set(bot.get_all_members())))
    chans = (len(set(bot.get_all_channels())))
    while not bot.is_closed:
        await bot.change_presence(game=discord.Game(name="with {} servers".format(servs)))
        await asyncio.sleep(11.5)
        await bot.change_presence(game=discord.Game(name="with {} users".format(users)))
        await asyncio.sleep(13.5)
        await bot.change_presence(game=discord.Game(name="say ?help"))
        await asyncio.sleep(15.5)
        await bot.change_presence(game=discord.Game(name="?invite | ?help"))
        await asyncio.sleep(17.5)
        await bot.change_presence(game=discord.Game(name="on {} channels".format(chans)))
        await asyncio.sleep(19.0)
        await bot.change_presence(game=discord.Game(name="Prefix = ?"))
        await asyncio.sleep(21.5)
        
@bot.event
async def on_server_join(server):
    print("I have joined {.name}!".format(server))
    await bot.send_message(server.owner, "Thanks for adding me to you're server! My prefix is `?`, so if you need any help, type `?help` _**Be sure I have all the permissions so that I can function properly!**_\n• Support Server: https://discord.gg/pDvJZEN\n• Owner/Creator: Rapid#0501")
    await bot.send_message(bot.get_channel("379454585808617472"), "**I have just joined a server! :sparkles:\nName: " + server.name + "\nID: " + server.id + "**")

@bot.event
async def on_server_remove(server):
    print("I have left {.name}.".format(server))
    await bot.send_message(bot.get_channel("379454585808617472"), "**I have just left a server. :x:\nName: " + server.name + "\nID: " + server.id + "**")
        
bot.loop.create_task(my_background_task())
if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))
