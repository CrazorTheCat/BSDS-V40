from Messaging.Packets.Server.Socket.KeepAliveServerMessage import KeepAliveServerMessage


from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class KeepAliveMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        KeepAliveServerMessage(self.client, self.player).send(self.player.LowID)