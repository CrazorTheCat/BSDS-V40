from Logic.Data.DataManager import Writer
from Logic.Client.ClientsManager import ClientsManager

class LobbyInfoMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23457
        self.client = client
        self.player = player

    def encode(self):
        self.writeVint(ClientsManager.GetCount())
        self.writeString("Project BSDS\n"f"Version: {self.player.device.major}.{self.player.device.build}.{self.player.device.minor}")
        self.writeVint(0)