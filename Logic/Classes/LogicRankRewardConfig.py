from Logic.LogicCondition import LogicCondition
from Logic.LogicGemOffer import LogicGemOffer
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicRankRewardConfig:
    def decode(self: Reader):
        self.readVint()
        self.readVint()
