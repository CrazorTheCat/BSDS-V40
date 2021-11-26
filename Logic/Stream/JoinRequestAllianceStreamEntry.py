from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Helpers.PlayerDisplayData import PlayerDisplayData
from Logic.Stream.StreamEntry import StreamEntry


class JoinRequestAllianceStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeString()
        self.writeString()
        self.writeVint(0)
        PlayerDisplayData.encode(self, info['Target'])

