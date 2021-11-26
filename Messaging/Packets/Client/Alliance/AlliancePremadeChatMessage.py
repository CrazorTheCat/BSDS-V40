import json

from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage


class AlliancePremadeChatMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.messageID = self.readDataReferenceDouble()[1]
        self.premadeID = self.readVint()

    def process(self):
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])

        while len(clubData['ChatData']) >= 100:
            clubData['ChatData'].pop(0)

        if len(clubData['ChatData']) == 0:
            lastMessageID = 0
        else:
            lastMessageID = clubData['ChatData'][len(clubData['ChatData']) - 1]['StreamID'][1]

        PremadeStreamData = clubdb.getDefaultMessageData(8, -1, [0, lastMessageID + 1], [self.player.HighID, self.player.LowID], self.player.Name, clubData['Members'][str(self.player.LowID)]['Role'], premadeID=self.premadeID, messageDataID=self.messageID)
        clubData['ChatData'].append(PremadeStreamData)
        clubdb.updateClubData(clubData, clubData['LowID'])

        for memberData in clubData['Members'].values():
            AllianceStreamEntryMessage(self.client, self.player, PremadeStreamData).send(memberData['LowID'])