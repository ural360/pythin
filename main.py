import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def botinfo(ctx):
    await ctx.send("Привет я бот для узнавания как правильно следить за экологией!")
    
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


bot.run(morning flower")
