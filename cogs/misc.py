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

@bot.command()
async def randomcommand():
    rc=discord.Embed(color=0x8f07ff, title="Random Command", description="**?{}**".format(random.choice(tuple(set(command.name for command in bot.commands.values())))))
    rc.add_field(name="About", value="Commands you see here, and not in the **help** command, are for testing.")
    await bot.say(embed=rc)

@bot.command(pass_context=True)
async def widentext(ctx,*, text : str):
    output = ""
    for character in text:
            if '!' <= character <= '~':
                    output += chr(ord(character) + 65248)
            else:
                    output += character
    wt=discord.Embed(color=0xff00aa, description=output)
    await bot.say(embed=wt)

@bot.command(pass_context=True)
async def fingers(ctx,*, text : str):
    fr=discord.Embed(color=0xff00aa, description=":point_right::skin-tone-2: {} :point_left::skin-tone-2:".format(text))
    await bot.say(embed=fr)

@bot.command(pass_context=True)
async def reverse(ctx,*, text : str):
    reverse = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await bot.say(f'{reverse}')
    
@bot.command(pass_context=True)
async def scramble(ctx,*, text : str):
    txtdata = list(' '.join(text))
    random.shuffle(txtdata)
    txt = ''.join(txtdata)
    sc=discord.Embed(color=0xff00aa, description="{}".format(txt))
    await bot.say(embed=sc)
    
@bot.command(pass_context=True)
async def emojify(ctx,*, text : str):
    output = ""
    for character in text:
            if 'a' <= character.lower() <= 'z':
                    output += ":regional_indicator_{}:".format(character.lower())
            elif '0' <= character <= '9':
                    output += ":{}:".format(clients.inflect_engine.number_to_words(int(character)))
            else:
                    output += character
    try:
            emjfy=discord.Embed(color=0xff00aa, description=output)
            await bot.say(embed=emjfy)
    except discord.errors.HTTPException:
            pass
    
@bot.command()
async def add(left,right):
    answer=int(left) + int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def subtract(left,right):
    answer=int(left) - int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def divide(left,right):
    answer=int(left) / int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command()
async def multiply(left,right):
    answer=int(left) * int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))

@bot.command(name='is')
async def _is(left, right):
    left = int(left)
    right = int(right)
    if int(left) > int(right):
        await bot.say("**:ledger: | {} is greater than {}**".format(left, right))
    elif int(left) < int(right):
        await bot.say("**:ledger: | {} is less than {}**".format(left, right))
    
@bot.command()
async def power(left,right):
    answer=int(left) ** int(right)
    await bot.say("**:ledger: | That equals: {}**".format(answer))
    
@bot.command(pass_context=True)
async def say(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(message)

@bot.command(pass_context=True)
async def embedsay(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(color = ctx.message.author.color)
    embed.description = (message)
    await bot.say(embed = embed)
    
@bot.command(aliases=["xmas"], pass_context=True)
async def christmas(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 12, 25)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0x10a542)
    embed.add_field(name = ":christmas_tree: Time left until Christmas :christmas_tree:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Christmas Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)

@bot.command(aliases=["hall"], pass_context=True)
async def halloween(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 10, 31)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xff5405)
    embed.add_field(name = ":candy: Time left until Halloween :lollipop:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Halloween Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)
    
@bot.command(aliases=["eas"], pass_context=True)
async def easter(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 4, 1)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xffe8dd)
    embed.add_field(name = ":chocolate_bar: Time left until Easter :egg:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Easter Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)

@bot.command(aliases=["val"], pass_context=True)
async def valentines(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 2, 14)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0xff0000)
    embed.add_field(name = ":gift_heart: Time left until Valentines Day :ribbon:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Valentines Day Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)
    
@bot.command(aliases=["saint"], pass_context=True)
async def saintpatrick(ctx):
    now = datetime.datetime.utcnow()
    xmas = datetime.datetime(now.year, 3, 17)
    if xmas<now:
        xmas = xmas.replace(year = now.year+1)
    delta=xmas-now
    weeks, remainder = divmod(int(delta.total_seconds()), 604800)
    days, remainder2 = divmod(remainder, 86400)
    hours, remainder3 = divmod(remainder2, 3600)
    minutes, seconds = divmod(remainder3, 60)
    embed = discord.Embed(color = 0x56ff5c)
    embed.add_field(name = ":four_leaf_clover: Time left until Saint Patricks Day :crown:", value = f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    embed.set_author(name = "Saint Patricks Day Countdown!", icon_url = ctx.message.author.avatar_url)
    await bot.say(content = "Requested by **" + ctx.message.author.name + "**", embed = embed)
    
@bot.command(pass_context=True)
async def gamertag(ctx):
    at = ctx.message.author.name
    a = random.randint(1, 20)
    mlg = {1: f"xX{a}Xx",
           2: "MinecraftLegend27",
           3: f"{at}istheG0D",
           4: f"{at}MLGGod69",
           5: f"XxInfamous{at}xX",
           6: f"MATRIX{at}2882",
           7: f"Dank{at}420",
           8: f"W33D.N.{at}",
           9: f"Myst1c{at}",
           10: f"Amazing{at}420blazeIT",
           11: f"▒▒▒{at}▒▒▒",
           12: f"❝{at}❞",
           13: f"{at}؁✍",
           14: f"✦{at}✧",
           15: f"⸻⸻L{at}L⸻⸻",
           16: f"ℳaster{at}69",
           17: f"☞ThisDod{at}",
           18: f"King♔MLG{at}",
           19: f"⚡uper⚡exy{at}",
           20: f"⛤⛤TheOFC{at}⛤"}

    embed=discord.Embed(color=0x8f07ff, title="Super dank gamertag generator", description=":label: | " + mlg[a])
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def story(ctx):
    m=ctx.message.author.name
    st=discord.Embed(color=0x8f07ff, title="Story of a dumb child", description=f"**{m}**\n(╯°□°)╯︵ ┻━┻\n\n**Dad**\nWhat the hell are you doin {m}?\n\n**Dad**\n┻━┻ ︵ ヽ(°□°ヽ)\n\n**Dad**\nSTOP IT NOW\n\n**{m}**\n┻━┻ ﾐヽ(ಠ益ಠ)ノ彡┻━┻\n\n**Dad**\nYOUR GETTING AN ASS BEATING, BEND OVER {m}")
    await bot.say(embed=st)
    
@bot.command()
async def itsrapids():
    rp=discord.Embed(color=0x42b9f4,description="Rapid's sexy color changing color, speaker/clock")
    rp.set_author(name="Rapid's Sexy Speaker/Clock", icon_url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_thumbnail(url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_image(url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    rp.set_footer(text="Sexy Speaker/Clock", icon_url="https://cdn.discordapp.com/attachments/385625038444822539/395092752297099264/20171225_225413.jpg")
    await bot.say(embed=rp)
    
def setup(bot): 
    bot.add_cog(Misc(bot))
