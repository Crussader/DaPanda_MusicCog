import discord, os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(intents=intents,
                    command_prefix='?',
                    case_insensitive=True,
                    enable_debug_events = True)

bot.user_id = int('YOUR BOT\'S ID')
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}') 

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run('YOUR BOT\'S TOKEN')