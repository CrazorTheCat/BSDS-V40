import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader
from Logic.Settings.Configuration import Configuration


class LogicSetPlayerNameColorCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        self.player.nameColor = self.readDataReferenceDouble()[1]

    def process(self):
        playerdb = DatabaseManager()
        data = json.loads(playerdb.getPlayerWithLowID(self.player.LowID)[0][2])
        data['namecolor'] = self.player.nameColor
        playerdb.updatePlayerData(data, self.player.LowID)
