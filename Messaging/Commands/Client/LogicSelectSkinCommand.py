import json

from Logic.Files.Classes.Skins import Skins
from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader


class LogicSelectSkinCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        print()
        self.skinData = self.readDataReferenceDouble()
        self.readVint()

    def process(self):
        self.db = DatabaseManager()
        self.database = json.loads(self.db.getPlayerWithLowID(self.player.LowID)[0][2])
        if self.skinData != 0:
            self.database['skinID'] = self.skinData[1]
            self.database['selectedSkin'][Skins.getBrawlerBySkin(self, self.skinData[1])] = self.skinData[1]
        elif self.randomSkinData != 0:
            self.database['selectedRandomSkin'].append(self.randomSkinData[1])
        self.db.updatePlayerData(self.database, self.player.LowID)