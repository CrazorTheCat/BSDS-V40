from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceListMessage import AllianceListMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage


class SearchAlliancesMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
        self.info = {}
 
    def decode(self):
        self.info['SearchString'] = self.readString()
        self.readInt()
        self.info['MinMembers'] = self.readInt()
        self.info['MaxMembers'] = self.readInt()
        self.info['MinTrophies'] = self.readInt()
        self.info['FindOnlyJoinableClans'] = self.readBoolean()
        self.info['Score'] = self.readInt()
        self.readInt() # MinLevel


    def process(self):
        AllianceListMessage(self.client, self.player, self.info).send(self.player.LowID)