import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer, Reader


class LogicSelectStarPowerCommand(Reader):
    def __init__(self, client, player, data):
        super().__init__(data)
        self.client = client
        self.player = player

    def decode(self):
        print()
        self.readDataReferenceDouble()

    def process(self):
        pass