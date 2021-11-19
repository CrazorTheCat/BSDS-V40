from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class BaseNotification:
    def decode(self: Reader):
        self.readInt()
        self.readVint()
        self.readInt()
        self.readString()

    def encode(self: Writer, info):
        self.writeInt(int(info[0]))
        self.writeBoolean(info[1]['ShowAtLaunch'] != True)
        self.writeInt(info[1]['Timer'])
        self.writeString(info[1]['Text'])

