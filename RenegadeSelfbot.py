import asyncio,uuid, pyfiglet, psutil, json, os, pyPrivnote, aiohttp, asyncio, base64, codecs, ctypes, datetime, discord, io,re,random, requests,string, sys, time, urllib, urllib.parse, urllib.request, os
from discord.ext import commands
from colorama import *
from discord.ext.commands import * 
import requests
from requests.sessions import Session
from discord import Webhook, AsyncWebhookAdapter
from pypresence import Presence
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import base64 as base64imp
from win10toast import ToastNotifier
import urllib.parse
from urllib import parse, request
from urllib.parse import quote as urlquote
import discord.guild
from colorama import Fore, init
from urllib.parse import quote as urlquote
from utils import *
from colour import Color

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

nitro_sniper = config.get('nitro_sniper')

intents = discord.Intents.all()
Renegade = discord.Client()
Renegade = commands.Bot(command_prefix=prefix,self_bot=True,intents=intents)
Renegade.copycat = None
Renegade.deletesniperid=None
Renegade.sniped_message = {}
Renegade.sniped_message_author = {}
Renegade.sniped_message_avatar = {}
Renegade.edited_message = {}
Renegade.edited_message_author = {}
Renegade.edited_message_avatar = {}
Renegade.remove_command('help')

def startPrint():
    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Disabled"
    print(f'''{Fore.RED}
                
                
                ██████╗░███████╗███╗░░██╗███████╗░██████╗░░█████╗░██████╗░███████╗
                ██╔══██╗██╔════╝████╗░██║██╔════╝██╔════╝░██╔══██╗██╔══██╗██╔════╝
                ██████╔╝█████╗░░██╔██╗██║█████╗░░██║░░██╗░███████║██║░░██║█████╗░░
                ██╔══██╗██╔══╝░░██║╚████║██╔══╝░░██║░░╚██╗██╔══██║██║░░██║██╔══╝░░
                ██║░░██║███████╗██║░╚███║███████╗╚██████╔╝██║░░██║██████╔╝███████╗
                ╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝
                 
                {Fore.CYAN}User: {Fore.GREEN}{Renegade.user.name}#{Renegade.user.discriminator}
                {Fore.CYAN}ID: {Fore.GREEN}{Renegade.user.id}   
                {Fore.CYAN}Prefix: {Fore.GREEN}{Renegade.}
command_prefix
                {Fore.CYAN}made by allah developers $$
    ''' + Fore.RESET)

os.system('cls')
print('Loading Renegade Selfbot...')

@Renegade.event
async def on_connect():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'Renegade Selfbot | Logged in as {Renegade.user.name}#{Renegade.user.discriminator}')
    startPrint()

@Renegade.event
async def on_message(message):
    if Renegade.copycat is not None and Renegade.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)
    await Renegade.process_commands(message)

@Renegade.event
async def on_message_delete(message):
    if message.author.id is not Renegade.user.id:
        channel_id = message.channel.id
        if Renegade.deletesniperid is not None and channel_id==Renegade.deletesniperid:
            embed = discord.Embed(color=0x279fd3,title=message.content)
            embed.set_footer(text="Renegade Selfbot")
            embed.set_author(name=message.author.name+" tried to delete a message!",icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
    if len(Renegade.sniped_message) > 1000:
        Renegade.sniped_message.clear()
    if len(Renegade.sniped_message_author) > 1000:
        Renegade.sniped_message_author.clear()
    if len(Renegade.sniped_message_avatar) > 1000:
        Renegade.sniped_message_avatar.clear()
    channel_id = message.channel.id
    Renegade.sniped_message.update({channel_id: message.content})
    Renegade.sniped_message_author.update({channel_id: message.author.name})
    Renegade.sniped_message_avatar.update({channel_id: message.author.avatar_url})

@Renegade.event
async def on_message_edit(before,after):
    if len(Renegade.edited_message) > 1000:
        Renegade.edited_message.clear()
    if len(Renegade.edited_message_author) > 1000:
        Renegade.sniped_message_author.clear()
    if len(Renegade.edited_message_avatar) > 1000:
        Renegade.edited_message_avatar.clear()
    channel_id = before.channel.id
    Renegade.edited_message.update({channel_id: before.content})
    Renegade.edited_message_author.update({channel_id: before.author.name})
    Renegade.edited_message_avatar.update({channel_id: before.author.avatar_url})    

@Renegade.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        return
    errorstr = str(error)
    embed = discord.Embed(color=0x279fd3,title="Error",description=errorstr)
    embed.set_footer(text="Renegade Selfbot")
    try:
        await ctx.message.delete()
        await ctx.send(embed=embed,delete_after=2)
    except:
        await ctx.send(embed=embed,delete_after=2)

@Renegade.command(aliases=["sigmaclient","sigmajello","jelloforsigma"])
async def sigma(ctx):
    await ctx.send("Sigma balls")

@Renegade.command()
async def logout(ctx):
    await ctx.message.delete()
    await Renegade.logout()

@Renegade.command()
async def say(ctx, *, messages):
    await ctx.message.delete()
    await ctx.send(messages)

@Renegade.command()
async def spam(ctx,amount:int,delay:float=None, *, messages):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(messages)
        await asyncio.sleep(delay)

@Renegade.command()
async def spamwebhook(ctx,webhook,amount:int,delay:float,*,message):
    await ctx.message.delete()
    for _i in range(amount):
        requests.post(webhook, json={'content': message})
        await asyncio.sleep(delay)

@Renegade.command()
async def deletewebhook(ctx,webhook):
    await ctx.message.delete()
    embed = discord.Embed(color=0x279fd3,title=webhook)
    embed.set_footer(text="Renegade Selfbot")
    embed.set_author(name="Deleted Webhook!",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed,delete_after=3)
    requests.delete(webhook)

@Renegade.command()
async def invischar(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@Renegade.command()
async def clear(ctx,amount:int):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * amount + 'ﾠﾠ')

@Renegade.command()
async def embed(ctx,*,msg):
    await ctx.message.delete()
    embed = discord.Embed(color=0x279fd3,title=msg)
    await ctx.send(embed=embed)

@Renegade.command()
async def tweet(ctx, username, *, message):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"renegade_tweet.png"))
            except:
                await ctx.send(res['message'])

@Renegade.command()
async def trumptweet(ctx, *,msg):
    await ctx.message.delete()
    img = Image.open("assets/trumptweet.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('assets/roboto.ttf', 30)
    draw.text((39, 123),f"{msg}",(0,0,0),font=font)
    randomnum = random.randint(1000, 9999)
    img.save(f'assets/{randomnum}.png')
    await ctx.send(file=discord.File(f'assets/{randomnum}.png'))
    os.remove(f'assets/{randomnum}.png')

@Renegade.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Renegade.command()
async def deletesniper(ctx):
    await ctx.message.delete()
    Renegade.deletesniperid=ctx.channel.id
    embed = discord.Embed(color=0x279fd3,title="Started sniping deleted messages in #"+ctx.channel.name)
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed,delete_after=3)

@Renegade.command()
async def stopdeletesniper(ctx):
    Renegade.deletesniperid=None
    embed = discord.Embed(color=0x279fd3,title="Delete Sniper is disabled!")
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed,delete_after=3)

@Renegade.command()
async def snipe(ctx):
    currentChannel = ctx.channel.id
    if currentChannel in Renegade.sniped_message:
        embed = discord.Embed(color=0x279fd3,title=Renegade.sniped_message[currentChannel])
        embed.set_author(name=Renegade.sniped_message_author[currentChannel],icon_url=Renegade.sniped_message_avatar[currentChannel])
        embed.set_footer(text="Renegade Selfbot")
        await ctx.send(embed=embed)
    else:
        await ctx.send("No message to snipe!", delete_after=3)
    await ctx.message.delete()

@Renegade.command()
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Renegade.sniped_message:
        embed = discord.Embed(color=0x279fd3,title=Renegade.edited_message[currentChannel])
        embed.set_author(name=Renegade.edited_message_author[currentChannel],icon_url=Renegade.edited_message_avatar[currentChannel])
        embed.set_footer(text="Renegade Selfbot")
        await ctx.send(embed=embed)
    else:
        await ctx.send("No message to snipe!", delete_after=3)

@Renegade.command()
async def read(ctx):
    await ctx.message.delete()
    for guild in Renegade.guilds:
        await guild.ack()     

@Renegade.command()
async def massreact(ctx,amount:int, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=amount).flatten()
    for message in messages:
        await message.add_reaction(emote)

@Renegade.command()
async def massdelete(ctx,amount:int):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=100).flatten()
    counter = 0
    for message in messages:
        if message.author == Renegade.user:
            await message.delete()
            counter += 1
        if counter == amount:
            break

@Renegade.command()
async def massmention(ctx):
    await ctx.message.delete()
    if len(ctx.guild.members) >= 50:
        userList = ctx.guild.members
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        post_message = ""
        for user in sampling:
            post_message += user.mention
        await ctx.send(post_message,delete_after=1)
    else:
        post_message = ""
        for user in ctx.guild.members:
            post_message += user.mention
        await ctx.send(post_message,delete_after=1)

@Renegade.command()
async def spamcreatechannel(ctx,amount:int,name):
    await ctx.message.delete()
    for _i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
        except:
            return


@Renegade.command()
async def spamdelchannel(ctx,amount:int=None):
    await ctx.message.delete()
    if amount is None:
        amount = len(ctx.guild.channels)
    for channel in ctx.guild.channels[:amount]:
        try:
            await channel.delete()
        except:
            return

@Renegade.command(aliases=["copy"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Renegade.copycat = user
    embed = discord.Embed(color=0x279fd3,title=f'Started copying {str(Renegade.copycat)}!')
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed,delete_after=3)

@Renegade.command(aliases=["stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Renegade.copycat is None:
        embed = discord.Embed(color=0x279fd3,title=" You weren't copying anyone!")
        embed.set_footer(text="Renegade Selfbot")
        await ctx.send(embed=embed,delete_after=3)
        return
    embed = discord.Embed(color=0x279fd3,title=f' Stopped copying {str(Renegade.copycat)}!')
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed,delete_after=3)
    Renegade.copycat = None
       
@Renegade.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Renegade.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{ctx.guild.member_count} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=0x279fd3)
    embed.set_footer(text="Renegade Selfbot")
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@Renegade.command(name='1337speak')
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '1').replace('I', '1') \
        .replace('o', '0').replace('O', '0').replace('s','5').replace('S','5')
    await ctx.send(f'{text}')

@Renegade.command()
async def randomgift(ctx):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send(f'https://discord.gift/{code}')

@Renegade.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Renegade.command()
async def ghostping(ctx,user:discord.User,*,message):
    await ctx.message.delete()
    await ctx.send(f"{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||{user.mention}")

@Renegade.command()
async def ghosteveryone(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(f"{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||@everyone")

@Renegade.command()
async def ghosthere(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(f"{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||@here")    

@Renegade.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`Pong! {int(ping)} ms`")

@Renegade.command()
async def useravatar(ctx,user:discord.User):
    await ctx.message.delete()
    embed = discord.Embed(color=0x279fd3)
    embed.set_footer(text="Renegade Selfbot")
    embed.set_author(name=f'{user.name}#{user.discriminator}',icon_url=user.avatar_url)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
        
        
@Renegade.command()
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.8)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@Renegade.command()
async def sunglase(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/attachments/764465337688129546/802657317194956860/sunglase.png")

@Renegade.command()
async def hahasex(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/emojis/734174032345170010.gif?v=1")

@Renegade.command()
async def virus(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/emojis/803956986503757824.png?v=1")

@Renegade.command()
async def howskid(ctx,*,user):
    await ctx.message.delete()
    howskid=str(random.randint(1,100))
    if user.lower() == "chocopie" or user.lower() == "omikron" or user.lower() == "choco pie":
        howskid="100"
    embed = discord.Embed(color=0x279fd3,title="Skid Detection Machine",description=f"{user} is {howskid}% skid!")
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed)

@Renegade.command()
async def ppsize(ctx,*,user):
    await ctx.message.delete()
    size = random.randint(1,10)
    embed = discord.Embed(color=0x279fd3,title=f" :eggplant: {user}'s penis size:",description="8"+"="*size+"D")
    embed.set_footer(text="Renegade Selfbot")
    await ctx.send(embed=embed)

@Renegade.command()
async def cat(ctx):
    await ctx.message.delete()
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(title=":cat: Cat picture!", color=0x279fd3)
    embed.set_footer(text="Renegade Selfbot")
    embed.set_image(url=data['file'])
    await ctx.send(embed=embed)

@Renegade.command()
async def dog(ctx):
    await ctx.message.delete()
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    embed = discord.Embed(title=":dog: Dog picture!", color=0x279fd3)
    embed.set_footer(text="Renegade Selfbot")
    embed.set_image(url=data['message'])
    await ctx.send(embed=embed)

def Init():
    try:
        Renegade.run(token, bot=False)
    except discord.errors.LoginFailure:
        print("[ERROR] Invalid token!") 
        os.system('pause >NUL')

if __name__ == '__main__':
    Init()