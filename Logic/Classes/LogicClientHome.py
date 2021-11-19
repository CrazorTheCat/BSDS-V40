from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Classes.LogicConfData import LogicConfData
from Logic.Classes.LogicDailyData import LogicDailyData
from Logic.Notifications.NotificationFactory import NotificationFactory
from Logic.Settings.Configuration import Configuration


class LogicClientHome:
    def decode(self: Reader):
        pass

    def encode(self: Writer):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        self.writeLong(self.player.HighID, self.player.LowID)  # PlayerID

        self.writeVint(len(Configuration.Inbox)) # Notification Factory
        for notifInfo in Configuration.Inbox:
            NotificationFactory.encode(self, (Configuration.Inbox.index(notifInfo), notifInfo))

        self.writeVint(-1)  # VideoAdStarted
        self.writeBoolean(False)
        self.writeVint(0)  # GatchaDrop
        self.writeVint(0)  # FriendlyStarPower
        self.writeVint(0)