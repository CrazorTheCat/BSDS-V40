import json

from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Utility.Utils import Utils

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceMemberMessage import AllianceMemberMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage


class ChangeAllianceMemberRoleMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.targetID = self.readLong()
        self.targetRole = self.readVint()

    def process(self):
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])

        if clubData['Members'][str(self.player.LowID)]['Role'] != 2:
            if clubData['Members'][str(self.player.LowID)]['Role'] != 4:
                return

        while len(clubData['ChatData']) >= 100:
            clubData['ChatData'].pop(0)

        if len(clubData['ChatData']) == 0:
            lastMessageID = 0
        else:
            lastMessageID = clubData['ChatData'][len(clubData['ChatData']) - 1]['StreamID'][1]

        isPromotingRole = Utils.isPromoting(clubData['Members'][str(self.targetID[1])]['Role'], self.targetRole)

        if isPromotingRole:
            PromoteStreamData = clubdb.getDefaultMessageData(4, 5, [0, lastMessageID + 1], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'], target={'ID': self.targetID, 'Name': clubData['Members'][str(self.targetID[1])]['Name']})
        else:
            PromoteStreamData = clubdb.getDefaultMessageData(4, 6, [0, lastMessageID + 1], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'], target={'ID': self.targetID, 'Name': clubData['Members'][str(self.targetID[1])]['Name']})

        clubData['ChatData'].append(PromoteStreamData)

        if self.targetRole == 2:
            DemotedStreamData = clubdb.getDefaultMessageData(4, 6, [0, lastMessageID + 2], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'], target={'ID': [self.player.HighID, self.player.LowID], 'Name': self.player.Name})
            clubData['ChatData'].append(DemotedStreamData)
            clubData['Members'][str(self.player.LowID)]['Role'] = 4

        clubData['Members'][str(self.targetID[1])]['Role'] = self.targetRole
        clubdb.updateClubData(clubData, clubData['LowID'])

        for memberData in clubData['Members'].values():
            AllianceMemberMessage(self.client, self.player, self.player.allianceID, clubData['Members'][str(self.targetID[1])]).send(memberData['LowID'])
            AllianceStreamEntryMessage(self.client, self.player, PromoteStreamData).send(memberData['LowID'])
            if self.targetRole == 2:
                AllianceStreamEntryMessage(self.client, self.player, DemotedStreamData).send(memberData['LowID'])

        if isPromotingRole:
            AllianceResponseMessage(self.client, self.player, 81).send(self.player.LowID)
        else:
            AllianceResponseMessage(self.client, self.player, 82).send(self.player.LowID)