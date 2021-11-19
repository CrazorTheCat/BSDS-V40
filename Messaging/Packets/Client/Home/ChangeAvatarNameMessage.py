from Messaging.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ChangeAvatarNameMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.player.Name = self.readString()
        self.readBoolean()

    def process(self):
        LogicChangeAvatarNameCommand(self.client, self.player).send(self.player.LowID)