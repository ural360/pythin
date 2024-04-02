import discord
from discord.ext import commands
import random
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send("!hello\n!repeat (количество) (что повторить)\n!heh\n!add (1 число) (2 число)\n!rand (от какового числа) (до какого числа)\n!timer (время в сек)\n!help")


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def rand(ctx, left: int, right: int):
    await ctx.send(random.randint(left,right))

@bot.command()
async def timer(ctx, left: int):
    time.sleep(left)
    await ctx.send("Время вышло")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run(":)")
