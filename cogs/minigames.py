import discord
from discord.ext import commands
openweathermapy.core as weather
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
@commands.cooldown(1, 10, commands.BucketType.user)
async def war(ctx):
    cards = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    member = ctx.message.author.name
    player = random.randint(2, 14)
    dealer = random.randint(2, 14)
    embed = await bot.say(embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...**"))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0x49bcff, description="**:shield: | Shuffling the cards...\nDealing...**"))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0x49bcff, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**'))
    if int(player) > int(dealer):
        await asyncio.sleep(1.0)
        await bot.edit_message(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}-----**\n`Player: ' + cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
    elif int(player) < int(dealer):
        await asyncio.sleep(1.0)
        await bot.edit_message(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`\n`Dealer: ' + cards[dealer] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
    else:
        await asyncio.sleep(1.0)
        player2 = random.randint(2, 14)
        player3 = random.randint(2, 14)
        player4 = random.randint(2, 14)
        dealer2 = random.randint(2, 14)
        dealer3 = random.randint(2, 14)
        dealer4 = random.randint(2, 14)
        if int(player4) > int(dealer4):
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0x84ba74, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' + cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:tada: | You won {}!**'.format(ctx.message.author.name)))
        elif int(player4) < int(dealer4):
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0xde0036, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:skull_crossbones: | You lost {}.**'.format(ctx.message.author.name)))
        else:
            await asyncio.sleep(1.0)
            await bot.edit_message(embed, embed=discord.Embed(color=0xffc627, description=f'**:shield: | Shuffling the cards...\nDealing...\n------{member}------**\n`Player: ' +cards[player] + '`, ' + cards[player2] + ', ' + cards[player3] + ', `**Deciding Card: **' + cards[player4] + '`\nDealer: ' +cards[dealer] + '`, ' + cards[dealer2] + ', ' + cards[dealer3] + ', `**Deciding Card: **' + cards[dealer4] + '`\n**:crossed_swords: | {}, it is a tie!**'.format(ctx.message.author.name)))
            
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    if (a == b ==c):
        message = f':tada: | You won {ctx.message.author.name}!'
    elif (a == b) or (a == c) or (b == c):
        message = f':hotsprings: | {ctx.message.author.name}, you almost won, 2/3!'
    else:
        message = f':flag_white: | You lost {ctx.message.author.name}.'

    embed = await bot.say(embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------**'))
    await asyncio.sleep(1.0)
    await bot.edit_message(embed, embed=discord.Embed(color=0xffffff, description=f'**:slot_machine: | {ctx.message.author.name} rolled the slots...\nSpinning...\n------{ctx.message.author.name}------\n`{a} | {b} | {c}`\n{message}**'))
    
def setup(bot): 
    bot.add_cog(Minigames(bot))
