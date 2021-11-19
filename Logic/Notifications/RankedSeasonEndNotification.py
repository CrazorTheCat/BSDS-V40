from Logic.Classes.LogicGemOffer import LogicGemOffer
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class RankedSeasonEndNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        self.readVint()
        if self.readVint() == 1:
            LogicGemOffer.decode(self)

    def encode(self: Writer, info): # TODO
        BaseNotification.encode(self, info)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        # for i in range(0):
        #     LogicGemOffer.encode(self)