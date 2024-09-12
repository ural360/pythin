import discord
from discord.ext import commands
import random
import time
from cod import treedetect
import os
       

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send("Привет! Я бот для небольшой помощи и узнавания ооб экологии!")



@bot.command()
async def help1(ctx):
    await ctx.send("!hello\n!repeat (количество) (что повторить)\n!heh\n!add (1 число) (2 число)\n!rand (от какового числа) (до какого числа)\n!timer (время в сек)\n!help1\n!mem\n!rustmem")

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
async def mem(ctx):
    memeses = os.listdir('images') 
    ghi = random.choice(memeses)
    with open(f'images/{ghi}', 'rb') as f:
            grf = discord.File(f)
    await ctx.send(file=grf)
@bot.command()
async def rustmem(ctx):
    rustes = os.listdir('rustmemes') 
    ghii = random.choice(rustes)
    with open(f'rustmemes/{ghii}', 'rb') as f1:
            grff = discord.File(f1)
    await ctx.send(file=grff)


    


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def ecoakum(ctx):
    await ctx.send("Аккумуляторы очень вредят природе во время изготовления, также они огнеопасны и взрывопасны. Аккумуляторы используются чуть ли не везде: в машинах, ноутбуках, телефонах и т. д. По этому не рекомендуется просто выкидывать, лучше их сдать.")

@bot.command()
async def ecoplast(ctx):
    await ctx.send("Пластик очень вредное вещество, он разлагается до 700 лет! Пластик лучше переплавлять и снова его использовать и так по кругу.")

@bot.command()
async def ecoglass(ctx):
    await ctx.send("Стекло тоже очень долго разлагается, к тому же животные когда ищут себе еду на помойке, они могут получить раны от стекла и умереть")

@bot.command()
async def ecoprom(ctx):
    await ctx.send("Промышленность сильно загрезняет среду, по этому надо использовать фильтры для отходов что бы оставить нашу окружающую среду в целости и сохранности") 

@bot.command()
async def ecohowbetter(ctx):
    await ctx.send("1. Старайтесь использовать меньше одноразовых неэкологических вещей.2. Сортируйте отходы по их классам.3. Сдавайте в переработку использованные вещи и которые вам больше не нужны.")


@bot.command()
async def ecophoto(ctx):
    ecoss = os.listdir('ecology') 
    ecom = random.choice(ecoss)
    with open(f'ecology/{ecom}', 'rb') as gh:
        ecor = discord.File(gh)
    await ctx.send(file=ecor)

@bot.command()
async def photodetect(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            atname = attachment.filename
            aturl = attachment.url
            await attachment.save(f"images/{attachment.filename}")
            await ctx.send(f"Сохранена картинка {attachment.filename}")
        res = treedetect(f"images/{attachment.filename}")
        await ctx.send(res)
    else:
        await ctx.send("ошибка 228")



bot.run("")