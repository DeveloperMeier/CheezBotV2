import os

import discord
from dotenv import load_dotenv

from client import Bot


BOT_SYMBOL = '//'
CLIENT = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = Bot(symbol=BOT_SYMBOL, client=CLIENT, token=TOKEN)

@CLIENT.event
async def on_ready(): await bot.on_ready()
@CLIENT.event
async def on_message(msg): await bot.on_message(msg)

bot.run()
    


