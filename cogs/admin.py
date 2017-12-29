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
async def nick(ctx, member : discord.Member, *,  name : str):
    if not ctx.message.author.server_permissions.manage_nicknames:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.change_nickname(member, name)
    await bot.say("**:white_check_mark: | Changed {}'s nickname to: `{}`**".format(member.name, name))
    

@bot.command(pass_context=True)
async def kick(ctx, member : discord.Member, *,  reason: str = ""):
    if not ctx.message.author.server_permissions.kick_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.kick(member)
    await bot.send_message(member, "**You were kicked from {}!\nReason: {}\nAction by: {}**".format(ctx.message.server.name, reason, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Kicked {}, reason: `{}`**".format(member.name, reason))

@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member, purge: int = 7):
    if not ctx.message.author.server_permissions.ban_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.ban(member, purge)
    await bot.send_message(member, "**You were banned from {}!\nAction by: {}**".format(ctx.message.server.name, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Banned {}.**".format(member.name))
    
@bot.command(pass_context=True)
async def softban(ctx, member : discord.Member, purge: int = 1):
    if not ctx.message.author.server_permissions.ban_members:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.ban(member, purge)
    await bot.unban(member.server, member)
    await bot.send_message(member, "**You were soft-banned from {}!\nAction by: {}**".format(ctx.message.server.name, ctx.message.author.name))
    await bot.say("**:white_check_mark: | Banned, then un-banned {}.**".format(member.name))

@bot.command(pass_context=True)
async def warn(ctx, member : discord.Member, *, reason: str):
    if not ctx.message.author.server_permissions.kick_members:
        return await bot.say("**:x: | You cannot to do that.**\nReason: **Insufficient Permissions(KickMembers)**")
#    if not user:
#        return await bot.say(ctx.message.author.mention + " Specify a user to warn!")
    await bot.send_message(member, "**You have been warned in {}!\nReason: {}**".format(ctx.message.server.name, reason))
    await bot.say("**:white_check_mark: | Warned {}.**".format(member.name))
    
@bot.command(pass_context=True)
async def addrole(ctx, member : discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.add_roles(member, role_name)
    await bot.say("**:white_check_mark: | Added the role {} to {}.**".format(role_name, member.name))

@bot.command(pass_context=True)
async def removerole(ctx, member : discord.Member, *, role_name: discord.Role):
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.remove_roles(member, role_name)
    await bot.say("**:white_check_mark: | Removed the role {} from {}.**".format(role_name, member.name))
    
@bot.command(pass_context=True)
async def createrole(ctx,*, name : str):
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    await bot.create_role(ctx.message.server, name=name, reason=f"Created by {ctx.message.author.name}", permissions=ctx.message.server.default_role.permissions)
    await bot.say("**:white_check_mark: | I've created the role `{}`.**".format(name))

@bot.command(pass_context=True)
async def deleterole(ctx,*, name : str):
    role = discord.utils.get(ctx.message.server.roles, name=name)
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    if role is None:
        await bot.say("**:x: | That role doesn't exist.**")
        return
    await bot.delete_role(ctx.message.server, role)
    await bot.say("**:white_check_mark: | I've deleted the role `{}`.**".format(name))
    
@bot.command(pass_context=True)
async def renamerole(ctx, name : str,*, newname : str):
    role = discord.utils.get(ctx.message.server.roles, name=name)
    if not ctx.message.author.server_permissions.manage_roles:
      return await bot.say("**:x: | Insufficient permissions.**")
    if role is None:
        await bot.say("**:x: | That role doesn't exist.**")
        return
    await bot.edit_role(ctx.message.server, role, name=newname)
    await bot.say("**:white_check_mark: | I've renamed the role `{}` to `{}`.**".format(name, newname))
    
@bot.command(pass_context=True)
async def clear(ctx, number):
    if not ctx.message.author.server_permissions.manage_messages:
      return await bot.say("**:x: | Insufficient permissions.**")
    elif int(number) > 100:
      return await bot.say("**:x: | Cannot clear more than 100 messages.**")
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    await bot.say("**:white_check_mark: | Cleared `{}` messages.**".format(number))
    
@bot.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def massnick(ctx,*, message : str):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | Insufficient permissions.**")
    try:
        for member in ctx.message.server.members:
            if member is not ctx.message.server.owner:
                if member.nick is not None:
                    await bot.change_nickname(member, "{}".format(message))
                else:
                    name = member.name
                    await bot.change_nickname(member, "{}".format(message))
        await bot.say("**:white_check_mark: | Mass nicked everyone to `{}`.**".format(message))
    except Exception as e:
        if 'Privellage is too low' in str(e):
            pass


@bot.command(pass_context=True)
async def clearnicks(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | Insufficient permissions.**")
    try:
        for member in ctx.message.server.members:
            if member is not ctx.message.server.owner:
                name = member.name
                await bot.change_nickname(member, name)
        await bot.say("**:white_check_mark: | Cleared all nicknames.**")
    except Exception as e:
        if 'Privellage is too low' in str(e):
            pass
        
@bot.command(pass_context=True)
async def setup_starboard(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | You cannot do that, get the owner or administrator to do this.**")
    await bot.create_channel(ctx.message.server, 'starboard', type=discord.ChannelType.text)
    await bot.say("**:white_check_mark: | I've made the channel, now IN THAT CHANNEL type `?config_starboardid`**")
    
@bot.command(pass_context=True)
async def config_starboardid(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | You cannot do that, get the owner or administrator to do this.**")
    embed = discord.Embed(color = 0xffffff, title = "Starboard Request!") #, description = "Starboard ID: {}".format(message))
    embed.add_field(name = "Server", value = ctx.message.server.name)
    embed.add_field(name = "Server ID", value = ctx.message.server.id)
    embed.add_field(name = "Server User Count", value = ctx.message.server.member_count)
    embed.add_field(name = "Server Owner", value = ctx.message.server.owner)
    embed.add_field(name = "Channel Name", value = ctx.message.channel.name)
    embed.add_field(name = "Channel ID", value = ctx.message.channel.id)
    embed.add_field(name = "Requester", value = ctx.message.author.name)
    embed.set_thumbnail(url = ctx.message.server.icon_url)
    await bot.send_message(bot.get_channel("379454585808617472"), content = "**Channel ID: " + ctx.message.channel.id + "**", embed = embed)
    await bot.say("**:white_check_mark: | Starboard request sent, now make sure no one can actually type in this channel.\nREMINDER:  I will only accept this request if the channel name is 'starboard'**")
        
@bot.command(aliases=["getbans", "bans"], pass_context=True)
async def gbans(ctx):
    if not ctx.message.author.server_permissions.administrator:
      return await bot.say("**:x: | Insufficient permissions.**")
    x = await bot.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    if x == None:
      embed = discord.Embed(title = "Banned Members for {}".format(ctx.message.server.name), description = "No bans, squeeky clean! ;)", color = 0x596ff)
      await bot.say(embed = embed)
    else:
        embed = discord.Embed(title = "Banned Members for {}".format(ctx.message.server.name), description = x, color = 0x596ff)
        await bot.say(embed = embed)
        
def setup(bot): 
        bot.add_cog(Admin(bot))
