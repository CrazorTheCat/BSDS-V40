from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class ChatStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeString(info['Message'])