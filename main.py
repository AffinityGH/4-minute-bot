import discord
from discord.ext import commands
from async_timeout import timeout
import youtube_dl
import asyncio
import functools
import itertools
import math
import random
from random import randint
import aiohttp
import json
import random
import keep_alive

client = commands.Bot(description='A bot made in 3 minutes', command_prefix=commands.when_mentioned_or("!")) #you can set client to whatever name you'd like, however you must change it for the rest of the code

@client.command() #ping command
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency *1000)} ms')

@client.event
async def on_member_join(member): 
    guild = member.guild #gets the discord server object
    channel = discord.utils.get(guild.text_channels, name='welcome') #retrieves channel object to send message in using the "welcome" name
    await ctx.send(f'{member} has joined the server!') #sends the message to the appropriate channel

@client.event
async def on_member_remove(member): 
    guild = member.guild #gets the discord server object
    channel = discord.utils.get(guild.text_channels, name='welcome') #retrieves channel object to send message in using the "welcome" name
    await ctx.send(f'{member} has left the server!') #sends the message to the appropriate channel

keep_alive.keep_alive()

@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a bot made in 3 minutes")) #put your status here

TOKEN = 'NzA4NTIxMjM1MTA1MTg1Nzky.Xreo1A.5ABgxjXA5XqJji8ks2INKWTbrlE' #write your token here

client.run(TOKEN)