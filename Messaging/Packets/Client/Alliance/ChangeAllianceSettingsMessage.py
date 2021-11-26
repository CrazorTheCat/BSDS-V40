import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage
from Messaging.Packets.Server.Alliance.ChangeAllianceSettingsOkMessage import ChangeAllianceSettingsOkMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage


class ChangeAllianceSettingsMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
        self.clubInfo = {}
 
    def decode(self):
        self.clubInfo['Description'] = self.readString()
        self.clubInfo['Badge'] = self.readDataReferenceDouble()
        self.clubInfo['Region'] = self.readDataReferenceDouble()
        self.clubInfo['Type'] = self.readVint()
        self.clubInfo['RequiredTrophies'] = self.readVint()
        self.clubInfo['FamilyFriendly'] = self.readBoolean()

    def process(self):
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])
        if clubData['Members'][str(self.player.LowID)]['Role'] == 2:
            clubData['Description'] = self.clubInfo['Description']
            clubData['BadgeID'] = self.clubInfo['Badge'][1]
            clubData['RegionID'] = self.clubInfo['Region'][1]
            clubData['Type'] = self.clubInfo['Type']
            clubData['TrophiesRequired'] = self.clubInfo['RequiredTrophies']
            clubData['FamilyFriendly'] = self.clubInfo['FamilyFriendly']
            clubdb.updateClubData(clubData, clubData['LowID'])

            MyAllianceMessage(self.client, self.player, self.player.allianceID).send(self.player.LowID)
            ChangeAllianceSettingsOkMessage(self.client, self.player, self.player.allianceID).send(self.player.LowID)
            AllianceResponseMessage(self.client, self.player, 10).send(self.player.LowID)

        else:
            MyAllianceMessage(self.client, self.player, self.player.allianceID).send(self.player.LowID)
            AllianceResponseMessage(self.client, self.player, 95).send(self.player.LowID)