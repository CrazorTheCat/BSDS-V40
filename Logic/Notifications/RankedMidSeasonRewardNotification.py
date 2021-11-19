from Logic.Classes.LogicRewardConfig import LogicRewardConfig
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class RankedMidSeasonRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        LogicRewardConfig.decode(self)

    def encode(self: Writer, info): # TODO
        BaseNotification.encode(self, info)
        self.writeVint(1)
        self.writeByte(3)

        self.writeByte(3)  # LogicRewardConfig

        self.writeVint(30)
        self.writeVint(1)

        self.writeVint(26)  # ItemType
        self.writeVint(1)
        self.writeVint(0)  # CsvID
        self.writeVint(357)