from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class ReplayStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeVint(0)
        self.writeLong(info['ReplayID'][0], info['ReplayID'][1])
        self.writeBoolean(False)
        self.writeString("String1")
        self.writeString("String2")
        self.writeString("String3")
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

