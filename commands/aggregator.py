from commands.gif.gif import Giffer

class CommandAggregator(Giffer):
    async def run(self, data, *cmd_obj):
        try:
            if data.cmd == '420' or data.cmd == 420:
                await CommandAggregator().four_twenty(*cmd_obj)
            else:
                await getattr(self, 'gif')(*cmd_obj)
        except Exception as e:
            print(e)