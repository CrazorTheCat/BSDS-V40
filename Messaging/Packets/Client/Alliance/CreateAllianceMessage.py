import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Utility.Utils import Utils
from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage


class CreateAllianceMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
        self.clubInfo = {}

    def decode(self):
        self.clubInfo['Name'] = self.readString()
        self.clubInfo['Description'] = self.readString()
        self.clubInfo['Badge'] = self.readDataReferenceDouble()
        self.clubInfo['Region'] = self.readDataReferenceDouble()
        self.clubInfo['Type'] = self.readVint()
        self.clubInfo['RequiredTrophies'] = self.readVint()
        self.clubInfo['FamilyFriendly'] = self.readBoolean()

    def process(self):
        playerdb = DatabaseManager()
        clubdb = ClubManager()

        self.clubID = Utils.getRandomID()

        clubdb.createClub(self.clubID[1], self.createClubData())
        playerData = json.loads(playerdb.getPlayerWithLowID(self.player.LowID)[0][2])
        playerData['allianceID'] = self.clubID
        playerdb.updatePlayerData(playerData, self.player.LowID)
        playerdb.LoadAccount(self.player.LowID, self.player)
        AllianceResponseMessage(self.client, self.player, 20).send(self.player.LowID)
        AllianceStreamMessage(self.client, self.player).send(self.player.LowID)
        MyAllianceMessage(self.client, self.player, self.clubID).send(self.player.LowID)

    def createClubData(self):
        DBData = {
            'HighID': self.clubID[0],
            'LowID': self.clubID[1],
            'Name': self.clubInfo['Name'],
            'Members': {str(self.player.LowID): {'HighID': self.player.HighID, 'LowID': self.player.LowID, 'Name': self.player.Name, 'Role': 2, 'Trophies': self.player.trophies, 'NameColor': self.player.nameColor, 'Thumbnail': self.player.thumbnail}},
            'Description': self.clubInfo['Description'],
            'BadgeID': self.clubInfo['Badge'][1],
            'RegionID': self.clubInfo['Region'][1],
            'Type': self.clubInfo['Type'],
            'TrophiesRequired': self.clubInfo['RequiredTrophies'],
            'FamilyFriendly': self.clubInfo['FamilyFriendly'],
            'ChatData': []
        }
        return DBData