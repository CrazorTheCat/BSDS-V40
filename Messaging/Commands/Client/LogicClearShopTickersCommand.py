import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader


class LogicClearShopTickersCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        # print()
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()

    def process(self):
        pass