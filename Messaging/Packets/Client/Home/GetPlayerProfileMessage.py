from Messaging.Packets.Server.Home.PlayerProfileMessage import PlayerProfileMessage

from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class GetPlayerProfileMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.playerID = self.readLong()

    def process(self):
        PlayerProfileMessage(self.client, self.player, self.playerID).send(self.player.LowID)