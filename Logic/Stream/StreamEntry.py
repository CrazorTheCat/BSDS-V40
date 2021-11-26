from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class StreamEntry:
    def encode(self: Writer, info):
        self.writeLogicLong(info['StreamID'][0], info['StreamID'][1]) # StreamEntryID
        self.writeLogicLong(info['PlayerID'][0], info['PlayerID'][1]) # TargetID
        self.writeString(info['PlayerName'])
        self.writeVint(info['PlayerRole'])
        self.writeVint(0)
        self.writeBoolean(False)

