from Logic.Classes.LogicCondition import LogicCondition
from Logic.Classes.LogicGemOffer import LogicGemOffer
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicRewardConfig:
    def decode(self: Reader):
        if self.readBoolean() == True:
            LogicCondition.decode(self)
        if self.readBoolean() == True:
            LogicGemOffer.decode(self)

    def encode(self: Writer, info): # TODO
        if self.writeBoolean() == True:
            LogicCondition.decode(self)
        if self.readBoolean() == True:
            LogicGemOffer.decode(self)
