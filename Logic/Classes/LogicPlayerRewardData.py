from Logic.LogicRewardConfig import LogicRewardConfig
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicPlayerRewardData:
    def decode(self: Reader):
        if self.readBoolean() == True:
            LogicRewardConfig.decode(self)
        self.readVint()
        self.readBoolean()
