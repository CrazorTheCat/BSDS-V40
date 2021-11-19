from Logic.Settings.PrintHandler import PrintManager

from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class AnalyticEventMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        pass