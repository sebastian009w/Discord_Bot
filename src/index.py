import discord
import os
import datetime
from dotenv import load_dotenv
from discord.ext import commands

# Read variable
load_dotenv()

token: str = os.getenv('TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$ ', description='Bot Helper Bot',intents=intents)

@bot.command()
async def init(ctx):
    await ctx.send('Hola En que puedo ayudarte :) ?')


@bot.command()
async def sum(ctx, number_one: int, number_two: int):
    await ctx.send(number_one + number_two)

@bot.command()
async def stats(ctx):
    embed = discord.Embed(
        title='Gy', 
        description='7cero3 Bot', 
        timestamp=datetime.datetime.utcnow(), 
        color=discord.Color.blue()
    )

    embed.add_field(name='Server Created At', value=f"{ctx.guild.created_at}")
    embed.add_field(name='Server Owner', value=f"{ctx.guild.owner}")
    embed.add_field(name='Server ID', value=f"{ctx.guild.id}")
    embed.set_image(url=f"{ctx.guild.icon}")
    
    await ctx.send(embed=embed)

# Event

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Mousak', url='http://www.twitch.tv/mousak'))
    print('My Bot On ready')

try:
    bot.run(token)
    print("Hello World Discord !")
except discord.errors.LoginFailure as error:
    print(error)   

