import discord, os, aiohttp
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(intents=intents,
                    command_prefix='?',
                    enable_debug_events = True)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}') 

@bot.event
async def on_ready():
    bot.session = aiohttp.ClientSession()
    print(f'{bot.user} has connected to Discord!')

bot.run('YOUR BOT TOKEN')