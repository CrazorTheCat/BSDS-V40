from Logic.Classes.LogicDataTables import LogicDataTables
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ChronosTextEntry:
    def decode(self: Reader):
        self.readInt()
        self.readString()

    def encode(self: Writer):
        self.writeInt(0)
        self.writeString("BSDS is catly hacc")
