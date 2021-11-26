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

        self.writeVint(len(Configuration.Inbox) + len(self.player.clubMailInbox)) # Notification Factory
        for notifInfo in Configuration.Inbox:
            NotificationFactory.encode(self, (Configuration.Inbox.index(notifInfo), notifInfo))

        for notifInfo2 in self.player.clubMailInbox:
            NotificationFactory.encode(self, (notifInfo2['Index'], notifInfo2))

        # TODO
        # self.writeVint(58) # New Club For Club League
        # self.writeInt(10)
        # self.writeBoolean(True)
        # self.writeInt(9999)
        # self.writeString("BSDS")
        # self.writeLogicLong(0, 1)
        # self.writeDataReference(0)
        # self.writeString("BSDS HACC")
        #
        # self.writeVint(59)
        # self.writeInt(11)
        # self.writeBoolean(False)
        # self.writeInt(9999)
        # self.writeString("BSDS")
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeLogicLong(0, 1)
        # self.writeLogicLong(0, 1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        #
        # self.writeVint(61) # Event Day Ended
        # self.writeInt(12)
        # self.writeBoolean(True)
        # self.writeInt(9999)
        # self.writeString("BSDS")
        # self.writeVint(1)
        # self.writeLogicLong(0, 1)
        # self.writeLogicLong(0, 1)
        # self.writeDataReference(0, 0)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)
        # self.writeVint(1)


        self.writeVint(-1)  # VideoAdStarted
        self.writeBoolean(False)
        self.writeVint(0)  # GatchaDrop
        self.writeVint(0)  # FriendlyStarPower
        self.writeVint(0)