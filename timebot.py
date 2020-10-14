import discord
from discord.ext import commands
from datetime import datetime
import asyncio

TOKEN = 'NzY1NjY5ODM3NTM1NzA3MTM2.X4YLmg.tRuG1VeZ4B5fSlnd2U7h09yrM4g'
bot = commands.Bot(command_prefix='/')   

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=datetime.strftime(datetime.now(),"%H:%M:%S")))
        await asyncio.sleep(1)

@bot.command(pass_context=True)
async def time(ctx):
    await ctx.send(datetime.strftime(datetime.now(),"%H:%M:%S"))

bot.run(TOKEN)
