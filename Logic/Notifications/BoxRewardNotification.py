from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class BoxRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        self.readVint()

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(1) # Unknown
        self.writeVint(info[1]['RewardType']) # Type
        self.writeVint(info[1]['RewardAmount']) # Amount
