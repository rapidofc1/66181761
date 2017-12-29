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
@commands.cooldown(1, 10, commands.BucketType.user)
async def pick(ctx):
    pick = discord.Embed(color = 0xf3a8bc, description = "**" + ctx.message.author.name + "**, you've picked {} 🌸".format(random.randint(1, 100)))
    await bot.say(embed = pick)

@bot.command(pass_context=True)
async def pun(ctx):
    pun_url = 'http://www.punoftheday.com/cgi-bin/arandompun.pl'
    async with aiohttp.ClientSession() as session:
        async with session.get(pun_url) as data:
            pun_req = await data.text()
    pun_text = pun_req.split('&quot;')[1]
    pun_text = ftfy.fix_text(pun_text)
    embed = discord.Embed(color = 0x02d9ff, description = pun_text)
    embed.set_author(name = "Random pun", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def chucknorris(ctx):
    joke_url = 'https://api.chucknorris.io/jokes/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(joke_url) as data:
            joke_data = await data.read()
            joke_json = json.loads(joke_data)
    joke = joke_json['value']
    embed = discord.Embed(color = 0xff6f02, description = joke)
    embed.set_author(name = "Chuck Norris joke", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def yomomma(ctx):
    resource = 'http://api.yomomma.info/'
    async with aiohttp.ClientSession() as session:
        async with session.get(resource) as data:
            data = await data.read()
            data = json.loads(data)
    joke = data['joke']
    if not joke.endswith('.'):
        joke += '.'
    embed = discord.Embed(color = 0x8805fc, description = joke)
    embed.set_author(name = "Yo momma joke", icon_url = ctx.message.author.avatar_url)
    await bot.say(embed = embed)
    
@bot.command()
async def ping():
    pingtime = time.time()
    pingms = await bot.say("Pinging...")
    ping = time.time() - pingtime
    await bot.edit_message(pingms, "**:ping_pong: | Pong!** (%.01f seconds)" % ping)

@bot.command()
async def pong():
    pongtime = time.time()
    pongms = await bot.say("Ponging...")
    pong = time.time() - pongtime
    await bot.edit_message(pongms, "**:ping_pong: | Ping!** (%.01f seconds)" % pong)
    
@bot.command(pass_context=True)
async def rate(ctx,*, thing : str):
    numbers = random.randint(0, 100)
    decimals = random.randint(0, 9)

    if numbers == 100:
        decimals = 0

    await bot.say(f"**:arrows_clockwise: | I'd rate {thing} a `{numbers}.{decimals}/100`**")
    
@bot.command()
async def count():
    co = await bot.say("Beginning...")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "1")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "2")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "3")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "4")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "5")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "6")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "7")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "8")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "9")
    await asyncio.sleep(1.0)
    await bot.edit_message(co, "10")
    await bot.say("**:white_check_mark: | Done!**")

@bot.command()
async def virus(user: discord.Member):
    v = await bot.say("Initializing...")
    await asyncio.sleep(3.0)
    await bot.edit_message(v, "[▓                         ] / {WiHb}-virus.exe Packing files.")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓                    ] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.7)
    await bot.edit_message(v, "[▓▓▓            ] | {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.0)
    await bot.edit_message(v, "[▓▓▓▓        ] / {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓▓▓▓    ] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(4.0)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.2)
    await bot.edit_message(v, "[▓▓▓▓▓▓] / {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(1.0)
    await bot.edit_message(v, "[▓▓▓▓▓▓] - {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "[▓▓▓▓▓▓] \ {WiHb}-virus.exe Packing files..")
    await asyncio.sleep(0.8)
    await bot.edit_message(v, "Successfully downloaded virus...")
    await asyncio.sleep(0.5)
    await bot.edit_message(v, "Installing 'WiHb.exe'...")
    await asyncio.sleep(2.0)
    await bot.edit_message(v, "Successfully injected WiHb.exe into **{}**!".format(user.name))
    
@bot.command(aliases=["salt"], pass_context=True)
async def salty(ctx):
    embed = discord.Embed(color = 0xffffff, title = "SOMEONE IS SAAALLTYY!")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/385625038444822539/388167280896376836/giphy-1.gif")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/385625038444822539/388167280896376836/giphy-1.gif")
    await bot.say(embed = embed)
    
@bot.command()
async def drake():
    embed = discord.Embed(color = 0x075dba, title = "Hotline bling")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/382331380656242702/382550019711959040/drake.gif")
    embed.set_image(url = "https://cdn.discordapp.com/attachments/382331380656242702/382550019711959040/drake.gif")
    await bot.say(embed = embed)

@bot.command()
async def coinflip():
    choice = random.randint(1,2)
    if choice == 1:
       await bot.say("**:hear_no_evil:  |  Heads!**")
    if choice == 2:
       await bot.say("**:monkey:  |  Tails!**")

@bot.command()
async def potatos():
    embed = discord.Embed(color = 0xffd670, title = "Potatos")
    embed.add_field(name = "Create a password:", value = "potato")
    embed.add_field(name = "Password must be atleast 8 characters long.", value = "boiled potato")
    embed.add_field(name = "Password must have atleast 1 number.", value = "1 boiled potato")
    embed.add_field(name = "Password cannot have a space.", value = "50FUCKINGpotatos")
    embed.add_field(name = "Password cannot have capitals.", value = "IfYouDoNotGiveMeAccess,RightNowIWillShove50FuckingPotatosUpUrAss")
    embed.add_field(name = "Password can only have letters & numbers.", value = "IWillShove50FuckingPotatosUpUrAssRightNowIfYouDontGiveMeAccess")
    embed.add_field(name = "Incorrect Password.", value = "FuckYou")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/382331380656242702/384143018145611777/Potatoes_PNG_Clipart.png")
    await bot.say(embed = embed)
    
@bot.command()
async def choose(*choices : str):
    await bot.say(random.choice(choices))
    
@bot.command()
async def roll():
    await bot.say(random.choice(["**:game_die:  |  You rolled a 1!**", "**:game_die:  |  You rolled a 2!**", "**:game_die:  |  You rolled a 3!**", "**:game_die:  |  You rolled a 4!**", "**:game_die:  |  You rolled a 5!**", "**:game_die:  |  You rolled a 6!**"]))
    
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Call **911,** {} just attempted suicide".format(ctx.message.author.name),
                                                            "{} just tried to kill themself!!!".format(ctx.message.author.name),
                                                            "Prep the stone, {} just died.... :(".format(ctx.message.author.name),
                                                            "WE NEED AN ABULANCE!!! {} MIGHT HAVE JUST DIED".format(ctx.message.author.name),
                                                            "{} decided to leave us, he'll be missed.".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** was killed by **{}** ".format(member.name, ctx.message.author.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["So **sad,** {} just hugged themself lmao".format(ctx.message.author.name),
                                                            "{} just hugged em' self".format(ctx.message.author.name),
                                                            "{} didn't wanna hug anyone else, no love for us... :(".format(ctx.message.author.name),
                                                            "{} looks like a good hugger, hey, could you give us some o' dat? :o".format(ctx.message.author.name),
                                                            "{} hugged no one but his hallow shell".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Adorable, **{}** hugged **{}** ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def kiss(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["AHHAHA {} kissed themself... what a shame".format(ctx.message.author.name),
                                                            "{} just kissed em' self".format(ctx.message.author.name),
                                                            "Kisses! Oh wait nevermind, just for {}".format(ctx.message.author.name),
                                                            "{} kissed\n\n\n\n\n\n\n\n\n\n\n\n\n\n THEMSELF".format(ctx.message.author.name),
                                                            "{} kissed his own body, ew".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** kissed **{}**, aweeeee ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def punch(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Erm {} punched... themself??".format(ctx.message.author.name),
                                                            "{} just flippin' punched em' self".format(ctx.message.author.name),
                                                            "~PUNCH~ watchout, {} is on a punching rampage".format(ctx.message.author.name),
                                                            "{} punched out his eye, physco much".format(ctx.message.author.name),
                                                            "{} just punched themself... lol".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**{}** just punched **{}**, dayuuuumm ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def slap(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["Ouch, {} slapped themself".format(ctx.message.author.name),
                                                            "What in Trap Nation is {} doing?! They slapped themself, lmao".format(ctx.message.author.name),
                                                            "Slaps for everyone! Oh wait, you're all in luck, I guess just {}".format(ctx.message.author.name),
                                                            "{} slapped himself right across his on FaCcEee".format(ctx.message.author.name),
                                                            "{} slapped {}".format(ctx.message.author.name, ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Watchout guys... **{}** slapped **{}** for what appears to be no reason... ouch ".format(ctx.message.author.name, member.name), color = ctx.message.author.color)
        await bot.say(embed = embed)

@bot.command(pass_context=True)
async def beatup(ctx, *, member: discord.Member = None):
    if member.id == ctx.message.author.id:
        embed = discord.Embed(description = (random.choice(["AHHAHA {} beat themself up into a ball... what a shame".format(ctx.message.author.name),
                                                            "{} smh, what a weirdo".format(ctx.message.author.name),
                                                            "{} beat up his own damn body, what is up with his head".format(ctx.message.author.name),
                                                            "{} is your head on right... or?".format(ctx.message.author.name),
                                                            "{} is beating himself ;D".format(ctx.message.author.name)])), color = ctx.message.author.color)
        await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "Damn, **{}** took a hard beating from this dood named **{}**, aweeeee ".format(member.name, ctx.message.author.name), color = ctx.message.author.color)
        await bot.say(embed = embed)
    
@bot.command(name="8ball")
async def _ball():
    await bot.say(random.choice([":8ball:  |  Obviously", ":8ball:  | I'm not sure", ":8ball:  |  Yes", ":8ball:  |  No", ":8ball:  |  It is certain", ":8ball:  |  No shit", ":8ball:  |  Ofcourse", ":8ball:  |  ...", ":8ball:  |  To be honest, who would even know", ":8ball:  |  It is believed so", ":8ball:  |  It's best you do not talk about it"]))

@bot.command()
async def shoot():
    await bot.say(random.choice([":basketball:  |  Wow you got it stuck... you throw a light wrist m8", ":basketball:  |  Dayum you got in... nice", ":basketball:  |  Wow, garbage, you need practice", ":basketball:  |  Toilet spin, close one pal", ":basketball:  |  Good try"]))

@bot.command()
async def dicklength():
    await bot.say(random.choice([":straight_ruler:  |  8==D 3 inches... small asf", ":straight_ruler:  |  8=========D 10 inches... jesus wtf, your definately gettin\' laid", ":straight_ruler:  |  8D bro...", ":straight_ruler:  |  8========================D 27 INCHES....... bro your a GOD", ":straight_ruler:  |  8====D 5 inches... typical asf"]))

@bot.command()
async def amicool():
    await bot.say(random.choice([":wastebasket:  |  Nothing...", ":tada:  |  Cool!", ":skull_crossbones:  |  Your... well um... you ain\'t cool... sorry...", ":hole:  |  No words to describe you"]))
    
@bot.command()
async def starterpack():
    embed = discord.Embed(title = "Look at dis", description = "Here is your starterpack.", color = 0x00ff44)
    embed.set_author(name = "Random starterpack")
    embed.set_image(url = (random.choice(["https://cdn.discordapp.com/attachments/385625038444822539/388911898835288064/126.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916557167984640/2117_ball-is-life.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388912371831406602/images-2.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784686641152/tough-white-guy.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784686641153/5z2vrt8amkpx.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784003100683/slutty-white-girl-starter-pack-pink-victorias-secret-tag-one-15815796.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913784003100682/22-and-date-a-14-year-old.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913783550246912/84588610.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913735864942593/cea.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388913734804045835/Annoyingmiddleschoolerstarterpack_0921e3_6313403.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916555192336384/he-latino-gangster-starter-pack-sc-blsnapz-12339278.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916557662781440/images-6.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916555640995840/4748276d39148c755d7e99f383678dec.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916554022256653/1xuaa2.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916554022256650/Km4Dbjj.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916501425553409/images-4.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916501425553408/1d2d0a1c28aa87b9778348f0b99320f3.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916499965804544/3df9723ebff5d734ec782f422c5e7e0a.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916500502937610/85508353.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916498988662785/Weveallmetthispersonwhenilivedinport_0bd170_5558718.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916498988662784/images-5.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916497575313409/beauty-pageants.png",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916497575313408/435.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916496190930945/3bfff573ef4201b307d66cb33198facf.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711957090306/the-high-school-latina-starter-pack-follow--all-mexicans-8419447.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711126749184/22581923_139077836723395_6788546199054974976_n.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927711957090304/spoton_starter_packs_for_different_types_of_people_640_19.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927710501535744/LedeCoffee_starterKits_JustMoved_wwstaff.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927709696360451/4aa3fe75067c724676044697f577631c--packing-humor-college-memes.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927690322739200/7da4d2987b02dfa987b0f9bbd189e3da.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927689790193665/rich-white-boy-starter-pack-hoodxsavage-if-this-aint-true-11759588.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927689790193664/424_im-a-white-boy-who-thinks-hes-ghetto.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688737292289/images-7.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688196358154/aKgOzob_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927688737292288/funny_starter_packs_21.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927687718338560/female-asian-college-student-starter-pack-5848263.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631812460545/the-school-bus-driver-starter-pack-how-true-is-thistag-9739067.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927632550526976/2016-emo-girl-starter-pack-fuck-me-daddy-american-send-6291714.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927687718338561/azVDwEp_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631812460544/23-8.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927630314962954/Screenshot_20171208-222713.jpg",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927631195635712/the-recently-divorced-middle-class-dad-starter-pack-dark-brown-9980877.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927628452560896/yBjC8VUr.png",
                                          "https://cdn.discordapp.com/attachments/382331380656242702/388927629073580032/aOyMgLR_700b.jpg",
                                          "https://cdn.discordapp.com/attachments/385625038444822539/388916496190930944/starter3.jpg"])))
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def cat():
    r = requests.get('https://random.cat/meow')
    cat = str(r.json()['file'])
    embed = discord.Embed(title = "Meow.", description = "Here is your cat.", color = 0x00ff44)
   # embed.set_thumbnail(url = cat)
    embed.set_author(name = "Random cat")
    embed.set_image(url = cat)
    embed.set_footer(text = "| © Cosmos |")
    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def dog():
    api = "https://api.thedogapi.co.uk/v2/dog.php"
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as r:
            if r.status == 200:
                response = await r.json()
                embed = discord.Embed(title = "Woof.", description = "Here is your dog.", color = 0x00ff44)
                embed.set_author(name = "Random dog")
                embed.set_image(url = response['data'][0]["url"])
                embed.set_footer(text = "| © Cosmos |")
                await bot.say(embed = embed)

@bot.command()
async def neko():
    response = requests.get("http://nekos.life/api/neko")
    neko=discord.Embed(color=0x00ff44, title="Neko", description="Here is your neko.")
    neko.set_author(name="Random neko")
    neko.set_image(url=response.json()["neko"])
    neko.set_footer(text="| © Cosmos |")
    await bot.say(embed=neko)
    
def setup(bot): 
    bot.add_cog(Fun(bot))
