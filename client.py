from config.message import MessageArgs

class Bot:
    def __init__(self, client, token, symbol):
        self.client = client
        self.symbol = symbol
        self.token = token
    
    async def on_message(self, msg):
        if msg.content.startswith(self.symbol):
            data = MessageArgs.split_args_and_cmd(msg.content, self.symbol)
            await msg.channel.send(f"You used `{data.cmd}` command with arguments `{data.args.split(' ')}`")

    async def on_ready(self):
        print(
            f'{self.client.user} is connected to the following guilds:\n'
            f'{[guild.name for guild in self.client.guilds]}'
        )

    def run(self):
        self.client.run(self.token)