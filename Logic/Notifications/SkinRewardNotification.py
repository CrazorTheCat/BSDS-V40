from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class SkinRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(29000000 + info[1]['SkinID']) # SkinID
