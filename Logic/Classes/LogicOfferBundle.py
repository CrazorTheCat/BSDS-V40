from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from LogicGemOffer import LogicGemOffer


class LogicOfferBundle:
    def decode(self: Reader):
        type = self.readBytePeek(self.peek(1))
        self.readVint("ItemType")
        self.readVint()
        self.readDataReference("CsvID")
        self.readVint()

    def encode(self: Writer):
        self.writeVint(1)
        print()
        for i in range(1):
            print()
            LogicGemOffer.encode(self)
            print()