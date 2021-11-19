from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ChallengeRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(1)
        for i in range(1):
            self.writeVint(1)
            self.writeVint(14)  # ItemType
            self.writeVint(1)
            self.writeVint(0)  # CsvID
            self.writeVint(0)

        self.writeVint(7)
        self.writeVint(3)
        self.writeString('SUMMER SPORTS CHALLENGE!')