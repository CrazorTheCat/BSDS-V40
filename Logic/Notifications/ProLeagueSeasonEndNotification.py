from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ProLeagueSeasonEndNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)