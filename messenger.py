
class Messenger():
    def __init__(self) -> None:
        self.cmd = None
        self.target = None

    def send(self, target, cmd):
        self.cmd = cmd
        self.target = target

    def recv(self):

        packet = {
                'target' : self.target,
                'cmd' : self.cmd }

        # Reset packet
        self.cmd = None
        self.target = None

        return packet


messenger = Messenger()
