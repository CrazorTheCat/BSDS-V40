from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class TicketCompensationNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()

    def encode(self: Writer, info):
        BaseNotification.encode(self, info)
        self.writeVint(info[1]['Tickets'])
        self.writeVint(info[1]['Gems'])
