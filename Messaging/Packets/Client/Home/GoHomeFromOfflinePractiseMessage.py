from Messaging.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class GoHomeFromOfflinePractiseMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.readBoolean()

    def process(self):
        OwnHomeDataMessage(self.client, self.player).send(self.player.LowID)