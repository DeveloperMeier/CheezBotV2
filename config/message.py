class MessageArgs:
    @staticmethod
    def split_args_and_cmd(msg, symbol):
        arr = msg.split(' ')
        cmd = arr[0][len(symbol):]
        args = ' '.join(arr[1:])
        return MessageArgs(cmd=cmd, args=args)

    def __init__(self, cmd, args):
        self.cmd = cmd
        self.args = args