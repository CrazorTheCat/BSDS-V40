from Logic.Data.DataManager import Writer


class MyAllianceMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.client = client
        self.player = player

    def encode(self):
        self.writeVint(0)
        self.writeVint(0)