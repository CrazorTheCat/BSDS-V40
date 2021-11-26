import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader


class LogicSelectCharacterCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        print()
        self.brawlerData = self.readDataReferenceDouble()

    def process(self):
        self.db = DatabaseManager()
        self.database = json.loads(self.db.getPlayerWithLowID(self.player.LowID)[0][2])
        self.database['brawlerID'] = self.brawlerData[1]
        self.db.updatePlayerData(self.database, self.player.LowID)