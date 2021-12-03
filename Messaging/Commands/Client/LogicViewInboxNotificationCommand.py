import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader
from Logic.Settings.Configuration import Configuration


class LogicViewInboxNotificationCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        self.index = self.readVint()
        self.readVint()

    def process(self):
        playerdb = DatabaseManager()
        data = json.loads(playerdb.getPlayerWithLowID(self.player.LowID)[0][2])
        for i in data['clubMailInbox']:
            if i['Index'] == self.index:
                i['ShowAtLaunch'] = False
                break
            playerdb.updatePlayerData(data, self.player.LowID)
