from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class VanityItemRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint("Item")

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(52000000 + info[1]['EmoteID']) # SkinID
