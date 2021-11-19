from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicGemOffer:
    def decode(self: Reader):
        type = self.readBytePeek(self.peek(1))
        self.readVint("ItemType")
        self.readVint()
        self.readDataReference("CsvID")
        self.readVint()

    def encode(self: Writer):
        self.writeVint(0)
        self.writeVint(0)