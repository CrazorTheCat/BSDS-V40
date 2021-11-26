from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Stream.StreamEntry import StreamEntry


class AllianceEventStreamEntry:
    def encode(self: Writer, info):
        StreamEntry.encode(self, info)
        self.writeVint(info['EventType'])
        self.writeBoolean(info['Target'] != {})
        if info['Target'] != {}:
            self.writeLogicLong(info['Target']['ID'][0], info['Target']['ID'][1])
            self.writeString(info['Target']['Name'])

