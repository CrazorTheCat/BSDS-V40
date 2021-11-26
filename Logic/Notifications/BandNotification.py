from Logic.Helpers.PlayerDisplayData import PlayerDisplayData
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class BandNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        PlayerDisplayData.decode(self)

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        PlayerDisplayData.encode(self, info[1]['Target'])
