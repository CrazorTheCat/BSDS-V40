from Logic.Data.DataManager import Writer


class KeepAliveServerMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20108
        self.client = client
        self.player = player

    def encode(self):
        pass