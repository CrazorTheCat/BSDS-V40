from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage


class AskForAllianceDataMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.clubID = self.readLong()
        self.readBoolean()

    def process(self):
        self.player.allianceTry += 1
        AllianceDataMessage(self.client, self.player, self.clubID, self.player.allianceTry).send(self.player.LowID)
        AllianceTeamsMessage(self.client, self.player).send(self.player.LowID)