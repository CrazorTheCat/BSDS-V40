from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
 
class AskForAllianceDataMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.ClubID = self.readLong()

    def process(self):
        AllianceDataMessage(self.client, self.player).send(self.player.LowID)
