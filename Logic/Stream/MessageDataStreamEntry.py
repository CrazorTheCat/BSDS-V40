from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class MessageDataStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeDataReference(0, info['MessageID'])

