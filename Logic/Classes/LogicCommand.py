from Logic.Classes.LogicCondition import LogicCondition
from Logic.Classes.LogicGemOffer import LogicGemOffer
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicCommand:
    def encode(self):
        self.writeVint(0)
        self.writeVint(0)
        self.writeLogicLong(self.player.HighID, self.player.LowID)
