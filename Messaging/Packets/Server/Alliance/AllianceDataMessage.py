from Logic.Data.DataManager import Writer


class AllianceDataMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24301
        self.client = client
        self.player = player

    def encode(self):
        self.writeBoolean(False)