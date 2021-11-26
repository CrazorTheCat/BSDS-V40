from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class QuickChatStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeDataReference(40, info['MessageDataID'])
        self.writeBoolean(False)
        self.writeString()
        self.writeVint(0)
        self.writeVint(info['PremadeID'])