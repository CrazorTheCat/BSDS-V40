from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicCondition:
    def decode(self: Reader):
        self.readVint()
        self.readVint()

    def encode(self: Writer):
        self.writeVint(0)
        self.writeVint(0)