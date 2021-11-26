import json
import random

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceMemberMessage import AllianceMemberMessage
from Messaging.Packets.Server.Alliance.AllianceMemberRemovedMessage import AllianceMemberRemovedMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage


class LeaveAllianceMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        pass

    def process(self):
        presidentLeft = False
        clubdb = ClubManager()
        playerdb = DatabaseManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])
        playerData = json.loads(playerdb.getPlayerWithLowID(self.player.LowID)[0][2])
        if len(clubData['Members']) - 1 > 0:
            if len(clubData['ChatData']) == 0:
                lastMessageID = 0
            else:
                lastMessageID = clubData['ChatData'][len(clubData['ChatData']) - 1]['StreamID'][1]

            LeaveStreamData = clubdb.getDefaultMessageData(4, 4, [0, lastMessageID + 1], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'])
            AllianceStreamEntryMessage(self.client, self.player, LeaveStreamData).send(self.player.LowID)

            if clubData['Members'][str(self.player.LowID)]['Role'] == 2:
                acceptedMembers = []
                for i, v in clubData['Members'].items():
                    if v['Role'] == 4:
                        acceptedMembers.append(v)

                if len(acceptedMembers) == 0:
                    for i, v in clubData['Members'].items():
                        if v['Role'] == 3:
                            acceptedMembers.append(v)

                if len(acceptedMembers) == 0:
                    for i, v in clubData['Members'].items():
                        if v['Role'] == 1:
                            acceptedMembers.append(v)

                chosenMember = random.choice(acceptedMembers)
                clubData['Members'][str(chosenMember['LowID'])]['Role'] = 2
                presidentLeft = True

            clubData['Members'].pop(str(self.player.LowID))
            clubData['ChatData'].append(LeaveStreamData)
            clubdb.updateClubData(clubData, clubData['LowID'])

            for memberData in clubData['Members'].values():
                if memberData['LowID'] != self.player.LowID:
                    AllianceStreamEntryMessage(self.client, self.player, LeaveStreamData).send(memberData['LowID'])
                    AllianceMemberRemovedMessage(self.client, self.player, [clubData['HighID'], clubData['LowID']], [self.player.HighID, self.player.LowID]).send(memberData['LowID'])
                    if presidentLeft:
                        AllianceMemberMessage(self.client, self.player, [clubData['HighID'], clubData['LowID']], clubData['Members'][str(chosenMember['LowID'])]).send(memberData['LowID'])

        else:
            clubdb.deleteClub(clubData['LowID'])

        playerData['allianceID'] = [0, 0]
        playerdb.updatePlayerData(playerData, self.player.LowID)
        playerdb.LoadAccount(self.player.LowID, self.player)

        MyAllianceMessage(self.client, self.player, [0, 0]).send(self.player.LowID)
        AllianceResponseMessage(self.client, self.player, 80).send(self.player.LowID)
        AllianceTeamsMessage(self.client, self.player).send(self.player.LowID)