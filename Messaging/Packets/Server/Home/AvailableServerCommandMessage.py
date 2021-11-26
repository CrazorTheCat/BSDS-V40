from Logic.Data.DataManager import Writer
from Logic.Client.ClientsManager import ClientsManager
from Logic.Helpers.PlayerDisplayData import PlayerDisplayData
from Logic.Settings.Configuration import Configuration


class AvailableServerCommandMessage(Writer):
    def __init__(self, client, player, info):
        super().__init__(client)
        self.id = 24111
        self.client = client
        self.player = player
        self.info = info

    def encode(self):
        self.writeVint(self.info['CommandID'])
        self.writeVint(1)
        if self.info['CommandID'] == 206:
            self.writeVint(self.info['NotificationID'])
            self.writeInt((len(Configuration.Inbox) + len(self.player.clubMailInbox)) - 1)
            self.writeBoolean(False)
            self.writeInt(0)
            self.writeString(self.info["MessageContent"])

            PlayerDisplayData.encode(self, self.info['Target'])

            self.writeVint(3)
            self.writeVint(-1)
            self.writeVint(-1)
            self.writeVint(0)
            self.writeVint(0)