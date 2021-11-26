import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Settings.Configuration import Configuration

from Messaging.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Messaging.Packets.Server.Alliance.AllianceMemberMessage import AllianceMemberMessage
from Messaging.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Messaging.Packets.Server.Alliance.AllianceStreamEntryMessage import AllianceStreamEntryMessage
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.AllianceTeamsMessage import AllianceTeamsMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Messaging.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage


class SendAllianceMailMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.readInt()
        self.clubMessage = self.readString()

    def process(self):
        if self.clubMessage == b'':
            AllianceResponseMessage(self.client, self.player, 114).send(self.player.LowID)
        else:
            clubdb = ClubManager()
            playerdb = DatabaseManager()
            clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])

            if clubData['Members'][str(self.player.LowID)]['Role'] != 2:
                if clubData['Members'][str(self.player.LowID)]['Role'] != 4:
                    return

            mailData = {
                'Index': (len(Configuration.Inbox) + len(self.player.clubMailInbox)) - 1,
                'ID': 82,
                'Timer': 0,
                'ShowAtLaunch': True,
                'Text': self.clubMessage,
                'Target': {'Name': self.player.Name, 'Thumbnail': self.player.thumbnail, 'NameColor': self.player.nameColor}
            }

            AllianceResponseMessage(self.client, self.player, 113).send(self.player.LowID)

            for i in clubData['Members'].values():
                if i['LowID'] in playerdb.GetAllDb():
                    playerData = json.loads(playerdb.getPlayerWithLowID(i['LowID'])[0][2])
                    playerData['clubMailInbox'].append(mailData)
                    playerdb.updatePlayerData(playerData, i['LowID'])
                    AvailableServerCommandMessage(self.client, self.player, {'CommandID': 206, 'NotificationID': 82, 'MessageContent': self.clubMessage, 'Target': mailData['Target']}).send(i['LowID'])
