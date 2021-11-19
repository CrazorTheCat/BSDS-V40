from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ScoreEntry:
    def decode(self: Reader):
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()

    def encode(self: Writer, brawler):
        self.writeVint(16000000 + brawler[0]) # BrawlerID
        self.writeVint(brawler[1]) # Brawler Trophies
        self.writeVint(brawler[2]) # Trophies Lost
        self.writeVint(brawler[3]) # Starpoints Gained