from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.UnknownLeaderboardAllianceMessage import UnknownLeaderboardAllianceMessage


class UnknownAskMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        pass

    def process(self):
        pass
        # UnknownLeaderboardAllianceMessage(self.client, self.player).send(self.player.LowID)
