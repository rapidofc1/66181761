import discord
from discord.ext import commands
import unicodedata
import youtube_dl
import pyowm
import traceback
import os
import sys
import sqlite3
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

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"))

@bot.command(pass_context=True)
async def message(ctx, user : discord.Member, *, message: str):
    if ctx.message.author.id == "371001497342836737":
      await bot.send_message(user, "{}".format(message))
      await bot.delete_message(ctx.message)
      await bot.send_message(ctx.message.author, f"**:white_check_mark: | Message sent to {user.name}!**")
      
@bot.command(pass_context=True)
async def dm(ctx, user : discord.Member, *, message: str):
    if ctx.message.author.id == "371001497342836737":
      embed = discord.Embed(color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Message: {}".format(message))
      embed.set_author(name = "Message from Rapid#0501")
      embed.set_footer(text = "| Rapid#0501 ")
      await bot.send_message(destination = user, embed = embed)
      await bot.say("**:white_check_mark: | Message sent to user!**")
      
@bot.command(pass_context=True, aliases=["setl", "sl"])
async def setlistening(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 2))
      await bot.say("**:white_check_mark: | Done!**")

@bot.command(pass_context=True, aliases=["setw", "sw"])
async def setwatching(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 3))
      await bot.say("**:white_check_mark: | Done!**")

@bot.command(pass_context=True, aliases=["sets", "ss"])
async def setstream(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      await bot.change_presence(game = discord.Game(name="%s"% text, type = 1, url = "https://www.twitch.tv/"))
      await bot.say("**:white_check_mark: | Done!**")
      
@bot.command(pass_context=True, aliases=["setg", "sg"])
async def setgame(ctx, *, text):
    if ctx.message.author.id == "371001497342836737":
      game = discord.Game(name="%s"% text)
      await bot.change_status(game)
      await bot.say("**:ballot_box_with_check:  |  Done!**")
      
@bot.command(pass_context=True)
async def stop(ctx):
    if ctx.message.author.id == "371001497342836737":
      await bot.say("**:white_check_mark: | Shutting down**")
      await asyncio.sleep(1)
      await bot.close()
      
@bot.command(pass_context=True)
async def servers(ctx):
    if ctx.message.author.id == "371001497342836737":
      x = ', '.join([str(server) for server in bot.servers])
      y = len(bot.servers)
      embed = discord.Embed(description = "```json\n" + x + "```", color = 0xff0000, timestamp = datetime.datetime.utcnow())
      embed.set_author(name = "All the servers I'm in: " + str(y), icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
      embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
      await bot.say(embed = embed) 
       
def setup(bot): 
        bot.add_cog(Dev(bot))
