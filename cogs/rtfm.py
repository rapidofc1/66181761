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

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"))

@bot.command(pass_context=True)
async def rtfm(ctx, msg : str):
    em=discord.Embed(color=0x6691D9, description="[{}]({})".format(msg, "http://discordpy.readthedocs.io/en/latest/api.html#discord.Client.{}".format(msg)))
    em.set_author(name="Client.{}".format(msg), icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=em)

@bot.command()
async def rtfm_rewrite():
    await bot.say("**:mag_right: | http://discordpy.readthedocs.io/en/rewrite/**")

@bot.command()
async def rtfm_async():
    await bot.say("**:mag_right: | http://discordpy.readthedocs.io/en/async/**")

def setup(bot): 
    bot.add_cog(Rtfm(bot))
