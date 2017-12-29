import discord
from discord.ext import commands
import openweathermapy.core as weather
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

@bot.command(pass_context=True, aliases=["feedback", "messsgedev", "fb"])
@commands.cooldown(1, 120, commands.BucketType.user)
async def msgdev(ctx, *, pmessage : str = None):
    invite = await bot.create_invite(ctx.message.channel, max_uses = 0)
    bot_owner = 371001497342836737
    dev = bot.get_user_info(bot_owner)

    if pmessage == None:
         await bot.say("**:x: | Provide a message. ヽ( ´¬`)ノ")
    else:
            msg = "User: {}\nServer: {}\nFeedBack: {}\nServer Invite: {}".format(ctx.message.author, ctx.message.server, pmessage, invite.url)
            embed = discord.Embed(title = "Invite to {} server!".format(ctx.message.server), color = ctx.message.author.color, url = "{}".format(invite.url), description = "Feedback: {}".format(pmessage), timestamp = datetime.datetime.utcnow())
            embed.set_thumbnail(url = "{}".format(ctx.message.author.avatar_url))
            embed.set_author(name = "{} sent:".format(ctx.message.author), icon_url = "{}".format(ctx.message.author.avatar_url))
            await bot.send_message(bot.get_channel("379454585808617472"), embed = embed)
            embed = discord.Embed(description = "I have sent **Rapid#0501** your message!", color = 0x00ff00)
            embed.set_footer(text = "| © Origami Tobiichi |")
            await bot.say(content = "**:green_book: | {}**".format(ctx.message.server), embed = embed)

@bot.command()
async def info():
    unique_members = set(bot.get_all_members())
    embed = discord.Embed(color = 0x6691D9, timestamp = datetime.datetime.utcnow(), title = "Cosmos Info", description = "Cosmos is a bot made only by Rapid, no more than a bit of help and some command examples from others. It is coded on an Android S7 on an application called Termux, by Rapid")
    embed.set_author(name = "All bot info and statistics", icon_url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/379454585808617472/389255356636987394/20171206_140705.jpg")
    embed.add_field(name = "Owner/Creator :spy:", value = "Rapid#0501")
    embed.add_field(name = "Made with <:Python:390560559113961472>", value = "Python Discord.py\nUsing Termux")
    embed.add_field(name = "Population :star:", value = "Servers: **{}".format(len(bot.servers)) + "**\n" + "Unique Members: **{}".format(len(set(bot.get_all_members()))) + "**\n" + "Unique Online: **{}".format(sum(1 for m in unique_members if m.status != discord.Status.offline)) + "**\n" + "Total Members: **{}".format(sum(len(s.members) for s in bot.servers)) + "**\n" + "Members Online:  **{}".format(sum(1 for m in bot.get_all_members() if m.status != discord.Status.offline)) + "**\n" + "Channels: **{}".format(len(set(bot.get_all_channels()))) + "**\n" + "Emojis: **{}".format(len(set(bot.get_all_emojis()))) + "**\n" + "Total Commands: **105**")
    embed.add_field(name = "Links :link:", value = "[Support Server]({})" .format("https://discord.gg/pDvJZEN") + "\n" + "[Invite Me]({})".format("https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591") + "\n" + "[DiscordBots.org]({})".format("https://discordbots.org/bot/385622427977121813"))
    embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
    await bot.say(embed = embed)
            
@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("**:link: | https://discordapp.com/oauth2/authorize?client_id=385622427977121813&scope=bot&permissions=2146958591**")
    print(ctx.message.author.name + " did invite")
        
@bot.command()
async def faq():
    em = discord.Embed(color = 0x8f07ff, title = "Frequently Asked Questions")
    em.add_field(name = "What is the starboard?", value = "My starboard is different, it is a command that allows you to send and view messages from/to any accepted starboard channel. Basically a global chat through Cosmos. Want it in your server? Type `?setup_starboard` to get started!")
    em.add_field(name = "How do you code on mobile?", value = "I code on my Android S7, using an application called Termux, with the editor Nano. Type `?tutTERMUX` on how to do this all yourself.")
    em.add_field(name = "Can I have your code?", value = "No, make your own, and besides, there are many `tut` commands with my bot.")
    em.add_field(name = "How come commands wont work after I use it?", value = "Either insufficient permissions for you or cosmos, or the command is on cooldown.")
    await bot.say(embed = em)
        
@bot.command(aliases=["suggest", "sug", "sugg"], pass_context=True)
async def suggestion(ctx,*, message: str):
    await bot.delete_message(ctx.message)
    embed = discord.Embed(color = 0xffa92a, description = "" + message + "")
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    react2 = await bot.send_message(bot.get_channel("392789385386655754"), content = "**Suggestion from " + ctx.message.server.name + " ID: " + ctx.message.server.id + "**", embed = embed)
    await bot.add_reaction(react2, "✅")
    await bot.add_reaction(react2, "❌")
    await bot.say("**:white_check_mark: | " + ctx.message.author.name + ", I've sent your suggestion!**\n __{}__".format(message))
        
@bot.command()
async def betatesters():
    em = discord.Embed(color = 0x0596ff, title = "Beta Testers", description = "**Rapid#0501\nDankXXlol#6659**")
    await bot.say(embed = em)
    
#Help command(s)
cmds = "105"
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
   user2send = ctx.message.author
   embed = discord.Embed(title = "Cosmos Commands", color = 0x6691D9, timestamp = datetime.datetime.utcnow(), description = "Cosmos's prefix is `?` If you need specific help on a command type `?help_<command>`")
   embed.set_author(name = '{} total commands'.format(cmds), icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.add_field(name = "Core Commands", value = "`help` | `info` | `invite` |  `msgdev` | `faq` | `betatesters` | `suggestion`")
   embed.add_field(name = "Utility Commands", value = "`messagessent` | `mail` | `invitegenerator` | `charinfo` | `starboard` | `poll` | `serverinfo` | `channelinfo` | `userinfo` | `emojiinfo` | `roleinfo` | `avatar` | `servericon` | `urband` | `timer`")
   embed.add_field(name = "Developer Commands", value = "`dm` | `announce` | `stop` | `servers` | `setwatching` | `setgame` | `setlistening` | `setstream`")
   embed.add_field(name = "Administrative Commands", value = "`setup_starboard` | `config_starboardid` | `nick` | `massnick` | `clearnicks` | `kick` | `ban` | `softban` | `warn` | `gbans` | `addrole` | `removerole` | `createrole` | `deleterole` | `renamerole` | `clear`")
   embed.add_field(name = "Fun Commands", value = "`virus` | `ping` | `pong` | `rate` | `starterpack` | `coinflip` | `roll` | `choose` | `8ball` | `kill` | `hug` | `kiss` | `punch` | `slap` | `beatup` | `shoot` | `dicklength` | `amicool` | `dog` | `cat` | `neko` | `drake` | `salty` | `pun` | `yomomma` | `chucknorris` | `count` | `potatos` | `pick`")
   embed.add_field(name = "Miscellaneous Commands", value ="`embedsay` | `say` | `emojify` | `scramble` | `widentext` | `fingers` | `randomcommand` | `gamertag` | `story` | `itsrapids` | `is` | `add` | `divide` | `multiply` | `subtract` | `power` |  `christmas` | `halloween` | `easter` | `saintpatrick` | `valentines`")
   embed.add_field(name = "MiniGame Commands", value = "`war` | `slots`")
   embed.add_field(name = "Read the manual Commands", value = "`rtfm` | `rtfm_async` | `rtfm_rewrite`")
   embed.add_field(name = "Discord.py Async HowTo's", value = "`tutBASICBOT` | `tutPING` | `tutSAY` | `tutCOINFLIP` | `tutTYPES` | `tutSERVERS` | `tutMEMBERS` | `tutCHANNELS` | `tutEMOJIS` | `tutERRORHANDLER` | `tutSETGAME` | `tutTERMUX`")
   embed.set_footer(text = "| © Cosmos ", icon_url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388086240538525696/20171206_140705.jpg")
   await bot.send_message(user2send, embed = embed)
   await bot.say("**:white_check_mark: | I've sent you all my commands!**")
        
@bot.command()
async def help_rtfm():
    h = discord.Embed(title = "Rtfm Command", color = 0x6691D9, description = "Sends the corrosponding link to your message")
    h.add_field(name = "Usage", value = "`?rtfm <event_message>`")
    h.add_field(name = "Note", value = "I don't allow spaces for this because they're not needed, like `rtfm wait_for_message`, pease don't requests fake/dumb links")
    await bot.say(embed = h)
    
@bot.command()
async def help_mail():
    h = discord.Embed(title = "Mail Command", color = 0x6691D9, description = "Sends a message to the given user through the bot")
    h.add_field(name = "Usage", value = "`?mail <@user> or <username> then <message> (rest is interactive setup)`")
    h.add_field(name = "Note", value = "Dont't overuse this, this command has a 1 minute cooldown to prevent idioticy")
    await bot.say(embed = h)
    
@bot.command()
async def help_virus():
    h = discord.Embed(title = "Virus Command", color = 0x6691D9, description = "Inject a virus into someone")
    h.add_field(name = "Usage", value = "`?virus <@user>`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)
        
@bot.command()
async def help_add():
    h = discord.Embed(title = "Add Command", color = 0x6691D9, description = "Adds 2 values together")
    h.add_field(name = "Usage", value = "`?add <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_subtract():
    h = discord.Embed(title = "Subtract Command", color = 0x6691D9, description = "Subtract a value from another")
    h.add_field(name = "Usage", value = "`?subtract <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_divide():
    h = discord.Embed(title = "Divide Command", color = 0x6691D9, description = "Groups a value into another")
    h.add_field(name = "Usage", value = "`?divide <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
        
@bot.command()
async def help_multiply():
    h = discord.Embed(title = "Multiply Command", color = 0x6691D9, description = "Multiplies a value by another")
    h.add_field(name = "Usage", value = "`?multiply <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_is():
    h = discord.Embed(title = "Is Command", color = 0x6691D9, description = "Determines if a value is or is not greater than another")
    h.add_field(name = "Usage", value = "`?is <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_power():
    h = discord.Embed(title = "Power Command", color = 0x6691D9, description = "Multiplies the value by the amount of the second value")
    h.add_field(name = "Usage", value = "`?power <number1> <number2>`")
    h.add_field(name = "Note", value = "Empty...")
        
@bot.command()
async def help_rate():
    h = discord.Embed(title = "Rate Command", color = 0x6691D9, description = "Rates your message out of 100")
    h.add_field(name = "Usage", value = "`?rate <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_war():
    h = discord.Embed(title = "War Command", color = 0x6691D9, description = "Begin a simple card game")
    h.add_field(name = "Usage", value = "`?war`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)
    
@bot.command()
async def help_invitegenerator():
    h = discord.Embed(title = "Invite Generator Command", color = 0x6691D9, description = "Create an instant bot authorization link")
    h.add_field(name = "Usage", value = "`?invitegenerator <client id>`")
    h.add_field(name = "Note", value = "Avoid this command if the server doesn't allow advertisements/links/invites")
    await bot.say(embed = h)
        

@bot.command()
async def help_slots():
    h = discord.Embed(title = "Slots Command", color = 0x6691D9, description = "Spins the slot machine")
    h.add_field(name = "Usage", value = "`?slots`")
    h.add_field(name = "Note", value = "Don't overuse this")
    await bot.say(embed = h)
    
@bot.command()
async def help_timer():
    h = discord.Embed(title = "Timer Command", color = 0x6691D9, description = "Sets a timer for you")
    h.add_field(name = "Usage", value = "`?timer <seconds>`")
    h.add_field(name = "Note", value = "This command has a cooldown of a minute to prevent spam")
    await bot.say(embed = h)
    
@bot.command()
async def help_setup_starboard():
    h = discord.Embed(title = "Setup_starboard Command", color = 0x6691D9, description = "Begins a setup wizard for the beta starboard")
    h.add_field(name = "Usage", value = "`?setup_starboard <the rest is interactive setup>`")
    h.add_field(name = "Note", value = "PLEASE make sure you follow all steps correctly")
    await bot.say(embed = h)
        
@bot.command()
async def help_msgdev():
    h = discord.Embed(title = "Msgdev Command", color = 0x6691D9, description = "Sends your message to Rapid")
    h.add_field(name = "Usage", value = "`?msgdev <message>`")
    h.add_field(name = "Note", value = "This command has a 2 minute cooldown")
    await bot.say(embed = h)
    
@bot.command()
async def help_suggestion():
    h = discord.Embed(title = "Suggestion Command", color = 0x6691D9, description = "Sends your suggestion to Cosmos's Hub")
    h.add_field(name = "Usage", value = "`?suggestion <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_charinfo():
    h = discord.Embed(title = "Charinfo Command", color = 0x6691D9, description = "Displays info on any character")
    h.add_field(name = "Usage", value = "`?charinfo <emoji> or <character>`")
    h.add_field(name = "Note", value = "Custom emotes are not supported, max of 10 characters p/c")
    await bot.say(embed = h)

@bot.command()
async def help_starboard():
    h = discord.Embed(title = "Starboard Command", color = 0x6691D9, description = "Posts a message in any starboard channel that Rapid sets (ask Rapid#0501 for more info)")
    h.add_field(name = "Usage", value = "`?starboard <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
        
@bot.command()
async def help_poll():
    h = discord.Embed(title = "Poll Command", color = 0x6691D9, description = "Begins a simple poll, embeds your message and adds 3 reactions")
    h.add_field(name = "Usage", value = "`?poll <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_serverinfo():
    h = discord.Embed(title = "Serverinfo Command", color = 0x6691D9, description = "Displays info on the server")
    h.add_field(name = "Usage", value = "`?serverinfo`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_channelinfo():
    h = discord.Embed(title = "Channelinfo Command", color = 0x6691D9, description = "Displays info on the given channel")
    h.add_field(name = "Usage", value = "`?channelinfo <#channel>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
       
 @bot.command()
async def help_userinfo():
    h = discord.Embed(title = "Userinfo Command", color = 0x6691D9, description = "Displays info on the given user")
    h.add_field(name = "Usage", value = "`?userinfo <@user>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_emojiinfo():
    h = discord.Embed(title = "Emojiinfo Command", color = 0x6691D9, description = "Displays info on the given emoji")
    h.add_field(name = "Usage", value = "`?emojiinfo <:emote:> or <name> or <just the emoji>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_roleinfo():
    h = discord.Embed(title = "Roleinfo Command", color = 0x6691D9, description = "Displays info on the given role")
    h.add_field(name = "Usage", value = "`?roleinfo <@role> or <name>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
       
@bot.command()
async def help_say():
    h = discord.Embed(title = "Say Command", color = 0x6691D9, description = "Makes the bot repeat your message")
    h.add_field(name = "Usage", value = "`?say <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_embedsay():
    h = discord.Embed(title = "Embedsay Command", color = 0x6691D9, description = "Makes the bot repeat your message in an embed")
    h.add_field(name = "Usage", value = "`?embedsay <message>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_urband():
    h = discord.Embed(title = "Urband Command", color = 0x6691D9, description = "Defines the given word with the Urban Dictionary API")
    h.add_field(name = "Usage", value = "`?urband <word>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_kick():
    h = discord.Embed(title = "Kick Command", color = 0x6691D9, description = "Kicks the given user")
    h.add_field(name = "Usage", value = "`?kick <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_ban():
    h = discord.Embed(title = "Ban Command", color = 0x6691D9, description = "Bans the given user")
    h.add_field(name = "Usage", value = "`?ban <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)

@bot.command()
async def help_warn():
    h = discord.Embed(title = "Say Command", color = 0x6691D9, description = "Warns the given user with a reason")
    h.add_field(name = "Usage", value = "`?warn <@user> <reason>`")
    h.add_field(name = "Note", value = "Disabled (WIP)")
    await bot.say(embed = h)
    
@bot.command()
async def help_gbans():
    h = discord.Embed(title = "Gbans Command", color = 0x6691D9, description = "Fetches all banned members in the server")
    h.add_field(name = "Usage", value = "`?gbans`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
        
@bot.command()
async def help_softban():
    h = discord.Embed(title = "Mute Command", color = 0x6691D9, description = "Bans, then unbans the member")
    h.add_field(name = "Usage", value = "`?softban <@user> or <username>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_addrole():
    h = discord.Embed(title = "Addrole Command", color = 0x6691D9, description = "Adds the given role to a member")
    h.add_field(name = "Usage", value = "`?addrole <@user> or <username> then <@role> or <rolename>`")
    h.add_field(name = "Note", value = "No mentions needed")
    await bot.say(embed = h)
    
@bot.command()
async def help_removerole():
    h = discord.Embed(title = "Removerole Command", color = 0x6691D9, description = "Removes the given role from a member")
    h.add_field(name = "Usage", value = "`?removerole <@user> or <username> then <@role> or <rolename>`")
    h.add_field(name = "Note", value = "No mentions needed")
    await bot.say(embed = h)
    
@bot.command()
async def help_createrole():
    h = discord.Embed(title = "Createrole Command", color = 0x6691D9, description = "Creates a role on command by the given name")
    h.add_field(name = "Usage", value = "`?createrole <rolename>`")
    h.add_field(name = "Note", value = "Default permissions are assigned")
    await bot.say(embed = h)
    
@bot.command()
async def help_deleterole():
    h = discord.Embed(title = "Deleterole Command", color = 0x6691D9, description = "Deletes a role on command by the given name")
    h.add_field(name = "Usage", value = "`?deleterole <rolename>`")
    h.add_field(name = "Note", value = "Don't mention, this method does not support the role ID")
    await bot.say(embed = h)
    
@bot.command()
async def help_renamerole():
    h = discord.Embed(title = "Renamerole Command", color = 0x6691D9, description = "Deletes a role on command by the given name")
    h.add_field(name = "Usage", value = "`?renamerole <rolename> then <newname>`")
    h.add_field(name = "Note", value = "Don't mention, this method does not support the role ID, you cannot edit a role that has spaces, you can only rename the role to have spaces")
    await bot.say(embed = h)
    
@bot.command()
async def help_clearnicks():
    h = discord.Embed(title = "Clearnicks Command", color = 0x6691D9, description = "Clears every nickname in the server")
    h.add_field(name = "Usage", value = "`?clearnicks`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
    
@bot.command()
async def help_massnick():
    h = discord.Embed(title = "Massnick Command", color = 0x6691D9, description = "Nicknames everyone in the server on command")
    h.add_field(name = "Usage", value = "`?massnick <nickname>`")
    h.add_field(name = "Note", value = "Does not always work, and don't overuse")
    await bot.say(embed = h)
    
@bot.command()
async def help_nick():
    h = discord.Embed(title = "Nick Command", color = 0x6691D9, description = "Nicknames given user on command")
    h.add_field(name = "Usage", value = "`?nick <@user> or <username> then <nickname>`")
    h.add_field(name = "Note", value = "No mentions needed")
    await bot.say(embed = h)
    
@bot.command()
async def help_clear():
    h = discord.Embed(title = "Clear Command", color = 0x6691D9, description = "Removes messages by the given amount")
    h.add_field(name = "Usage", value = "`?clear 50`")
    
@bot.command()
async def help_choose():
    h = discord.Embed(title = "Choose Command", color = 0x6691D9, description = "Makes the bot choose between any options")
    h.add_field(name = "Usage", value = "`?choose <option1> | <option2> | <option3>`")
    h.add_field(name = "Note", value = "The bot will sometimes choose the seperator")
    await bot.say(embed = h)

@bot.command()
async def help_8ball():
    h = discord.Embed(title = "8ball Command", color = 0x6691D9, description = "Ask the bot a question for an answer")
    h.add_field(name = "Usage", value = "`?8ball <question>`")
    h.add_field(name = "Note", value = "Empty...")
    await bot.say(embed = h)
        
def setup(bot): 
    bot.add_cog(Core(bot))
