import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader


class LogicClearShopTickersCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        print()
        print(self.readVint())
        print(self.readVint())
        print(self.readVint())
        print(self.readVint())

    def process(self):
        pass