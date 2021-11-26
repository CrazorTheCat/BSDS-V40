from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class TeamCreatedStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeLong(info['TargetID'][0], info['TargetID'][1])
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
