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

@bot.command(pass_context=True, aliases=["ms", "messages"])
async def messagessent(ctx):
    counter = 0
    tmp = await bot.say("Calculating messages...")
    async for log in bot.logs_from(ctx.message.channel, limit=1000):
        if log.author == ctx.message.author:
            counter += 1
    await bot.edit_message(tmp, "**:speech_left: | You've sent {} messages in this channel, {}.**".format(counter, ctx.message.author.name))
    
@bot.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def mail(ctx, member : discord.Member, *, message : str):
    sender=ctx.message.author.name
    await bot.say("Provide a title. (NA if none)`30s`")
    title = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    m=discord.Embed(color=0x42b6f4, title="{}".format(title.content), description="{}".format(message), timestamp=datetime.datetime.utcnow())
    m.set_author(name="New mail from {}!".format(sender))
    m.set_thumbnail(url="{}".format(image.content))
    m.set_footer(text="{}#{} ".format(sender, ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
    await bot.send_message(member, embed=m)
    await bot.say("**:white_check_mark: | Message sent to {}#{}.**".format(member.name, member.discriminator))
       
@bot.command(aliases=["s", "st", "star"], pass_context=True)
async def starboard(ctx,*, message: str):
#    await bot.delete_message(ctx.message) (This is optional. It'll delete the command message if the hash, aswell as this message is removed.)
    embed = discord.Embed(color = 0xffa92a, description = "" + message + "")
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    msg2send = await bot.say(content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("392833879104290827"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393094161764581399"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393209121928642563"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393821239032152079"), content = "**:star: " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    react2 = await bot.send_message(bot.get_channel("393819606344663049"), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#More possible channels    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#More possible channels    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
#More possible channels    react2 = await bot.send_message(bot.get_channel(""), content = "**:star: " + ctx.message.server.name + " ID: "+ ctx.message.server.id + "**", embed = embed)
    await bot.add_reaction(msg2send, "⭐")
#    await bot.add_reaction(react2, "⭐")
    await bot.say("**:white_check_mark: | " + ctx.message.author.name + ", I've published your message!**")
    
@bot.command(pass_context=True)
async def charinfo(ctx, *, characters: str):
    if len(characters) > 10:
        return await bot.say(f"**:x:  |  To many characters. ({len(characters)}/10)**")

    def to_string(c):
        digit = f'{ord(c):x}'
        name = unicodedata.name(c, "**:x:  |  Emoji name not found.**")
        return f'`\\U{digit:>08}`: {name} - {c} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{digit}>'

    await bot.say("\n".join(map(to_string, characters)))
    
@bot.command(pass_context=True)
async def poll(ctx,*, message: str):
    embed = discord.Embed(color = ctx.message.author.color, timestamp = datetime.datetime.utcnow())
    embed.set_author(name = "Poll", icon_url = ctx.message.author.avatar_url)
    embed.description = (message)
    embed.set_footer(text = ctx.message.author.name)
    x = await bot.say(embed = embed)
    await bot.add_reaction(x, "👍")
    await bot.add_reaction(x, "\U0001f937")
    await bot.add_reaction(x, "👎")
    
@bot.command(pass_context=True)
async def avatar(ctx, member : discord.Member):
    av=discord.Embed(color=member.color)
    av.set_author(icon_url=member.avatar_url, name="Avatar for {}".format(member.name))
    av.set_image(url=member.avatar_url)
    await bot.say(content="Requested by **{}**".format(ctx.message.author.name), embed=av)
    
@bot.command(pass_context=True)
async def servericon(ctx):
    av=discord.Embed(color=ctx.message.author.color)
    av.set_author(icon_url=ctx.message.server.icon_url, name="Server icon for {}".format(ctx.message.server.name))
    av.set_image(url=ctx.message.server.icon_url)
    await bot.say(content="Requested by **{}**".format(ctx.message.author.name), embed=av)
    
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(color = user.color, description = "Game Status: {}".format(user.game))
    embed.set_author(name=user.name, icon_url = user.avatar_url)
    embed.add_field(name = "Name", value = user.name)
    embed.add_field(name = "Discord ID", value = format(user.id))
    embed.add_field(name = "Status", value = format(user.status))
    embed.add_field(name = "Account Made At", value = formst(user.created_at))
    embed.set_thumbnail(url = format(user.avatar_url))
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(color = 0xffffff)
    embed.set_author(name = ctx.message.server.name, icon_url = ctx.message.server.icon_url)
    embed.add_field(name = "Server Name", value = ctx.message.server.name)
    embed.add_field(name = "Server ID", value = ctx.message.server.id)
    embed.add_field(name = "Owner", value = ctx.message.server.owner)
    embed.add_field(name = "Server Size (Big)", value = ctx.message.server.large)
    embed.add_field(name = "Verification Level", value = ctx.message.server.verification_level)
    embed.add_field(name = "Region", value = ctx.message.server.region)
    embed.add_field(name = "Members", value = ctx.message.server.member_count)
    embed.add_field(name = "Server Made At", value = ctx.message.server.created_at)
    embed.set_thumbnail(url = ctx.message.server.icon_url)
    await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def roleinfo(ctx, *,role: discord.Role):
    embed = discord.Embed(color = role.color)
    embed.set_author(name = role.name)
    embed.add_field(name = "Role Nsme", value = format(role.name))
    embed.add_field(name = "Role ID", value = format(role.id))
    embed.add_field(name = "Hoist", value = format(role.hoist))
    embed.add_field(name = "Role Position", value = format(role.position))
    embed.add_field(name = "Is Mentionable", value = format(role.mentionable))
    embed.add_field(name = "Role Made At", value = format(role.created_at))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def channelinfo(ctx, *,channel: discord.Channel):
    embed = discord.Embed(color = ctx.message.author.color)
    embed.set_author(name = channel.name)
    embed.add_field(name = "Channel Name", value = format(channel.name))
    embed.add_field(name = "Channel ID", value = format(channel.id))
    embed.add_field(name = "Topic", value = format(channel.topic))
    embed.add_field(name = "Channel Position", value = (channel.position))
    embed.add_field(name = "Channel Type", value = format(channel.type))
    embed.add_field(name = "Channel Made At", value = format(channel.created_at))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def emojiinfo(ctx, *,emoji: discord.Emoji):
    embed = discord.Embed(color = ctx.message.author.color)
    embed.set_author(name = emoji.name, icon_url = emoji.url)
    embed.add_field(name = "Emoji Name", value = format(emoji.name))
    embed.add_field(name = "Emoji ID", value = format(emoji.id))
    embed.add_field(name = "Require Colons", value = format(emoji.require_colons))
    embed.add_field(name = "Emoji URL", value = format(emoji.url))
    embed.add_field(name = "Emoji Made At", value = format(emoji.created_at))
    embed.set_thumbnail(url = emoji.url)
    await bot.say(embed = embed)
    
@bot.command()
async def urband(*msg):

    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    async with aiohttp.ClientSession() as session:
        async with session.get(api, params={'term': word}) as r:
            response = await r.json()
        if len(response["list"]) == 0:
            await bot.say(":x: | **Could not find that word.**")            
        else:
                embed = discord.Embed(title = 'Urban Dictionary - ' + word, color = ctx.message.author.color)
                embed.description = response['list'][0]['definition']
                embed.set_author(name = word, icon_url = ctx.message.author.avatar_url)
                embed.add_field(name = "Examples:", value = response['list'][0]["example"][:1000])
                embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
                await bot.say(embed = embed)

def setup(bot): 
        bot.add_cog(Utility(bot))
