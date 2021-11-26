from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.JoinableAllianceListMessage import JoinableAllianceListMessage


class AskForJoinableAlliancesListMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        pass

    def process(self):
        JoinableAllianceListMessage(self.client, self.player).send(self.player.LowID)
