import os

import discord
from dotenv import load_dotenv

from client import Bot


BOT_SYMBOL = '//'
CLIENT = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GIPHY_TOKEN = os.getenv('GIPHY_TOKEN')
bot = Bot(symbol=BOT_SYMBOL, client=CLIENT, discord_token=DISCORD_TOKEN, giphy_token=GIPHY_TOKEN)

@CLIENT.event
async def on_ready(): await bot.on_ready()
@CLIENT.event
async def on_message(msg): await bot.on_message(msg)

bot.run()
    


