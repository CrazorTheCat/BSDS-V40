from Logic.Classes.LogicDataTables import LogicDataTables
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ChronosFileEntry:
    def decode(self: Reader):
        self.readString()
        self.readString()

    def encode(self: Writer):
        self.writeString("Cats are very nice")
        self.writeString("BSDS is catly hacc")
