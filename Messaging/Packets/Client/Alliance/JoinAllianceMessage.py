import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceMemberMessage import AllianceMemberMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage


class JoinAllianceMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.clubID = self.readLong()

    def process(self):
        clubdb = ClubManager()
        playerdb = DatabaseManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.clubID[1])[0][1])
        playerData = json.loads(playerdb.getPlayerWithLowID(self.player.LowID)[0][2])

        if len(clubData['ChatData']) == 0:
            lastMessageID = 0
        else:
            lastMessageID = clubData['ChatData'][len(clubData['ChatData']) - 1]['StreamID'][1]

        clubData['Members'][str(self.player.LowID)] = clubdb.getDefaultMembersData(self.player, 1)
        JoinStreamData = clubdb.getDefaultMessageData(4, 3, [0, lastMessageID + 1], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'], target={'ID': [self.player.HighID, self.player.LowID], 'Name': self.player.Name, 'Thumbnail': self.player.thumbnail, 'NameColor': self.player.nameColor})
        clubData['ChatData'].append(JoinStreamData)
        clubdb.updateClubData(clubData, clubData['LowID'])

        playerData['allianceID'] = self.clubID
        playerdb.updatePlayerData(playerData, self.player.LowID)
        playerdb.LoadAccount(self.player.LowID, self.player)

        AllianceResponseMessage(self.client, self.player, 40).send(self.player.LowID)
        AllianceTeamsMessage(self.client, self.player).send(self.player.LowID)
        MyAllianceMessage(self.client, self.player, self.clubID).send(self.player.LowID)
        AllianceStreamMessage(self.client, self.player).send(self.player.LowID)

        for membersData in clubData['Members'].values():
            if membersData['LowID'] != self.player.LowID:
                AllianceMemberMessage(self.client, self.player, self.clubID, clubData['Members'][str(self.player.LowID)]).send(membersData['LowID'])
                AllianceStreamEntryMessage(self.client, self.player, JoinStreamData).send(membersData['LowID'])

