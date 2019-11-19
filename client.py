import json
from pprint import pprint
import random

from config.message import MessageArgs
from commands.aggregator import CommandAggregator

class Bot:
    def __init__(self, client, discord_token, giphy_token, symbol):
        self.client = client
        self.symbol = symbol
        self.discord_token = discord_token
        self.giphy_token = giphy_token
    
    async def on_message(self, msg):
        # try:
        if msg.content.startswith(self.symbol):
            data = MessageArgs.split_args_and_cmd(msg.content, self.symbol)
            cmd_obj = (self.giphy_token, data.args or data.cmd, msg)
            await CommandAggregator().run(data, *cmd_obj)

    async def on_ready(self):   
        print(
            f'{self.client.user} is connected to the following guilds:\n'
            f'{[guild.name for guild in self.client.guilds]}'
        )

    def run(self):
        self.client.run(self.discord_token)