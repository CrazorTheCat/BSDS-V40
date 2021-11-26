from Logic.Data.DataManager import Writer


class AllianceResponseMessage(Writer):
    def __init__(self, client, player, response):
        super().__init__(client)
        self.id = 24333
        self.client = client
        self.player = player
        self.response = response

    def encode(self):
        self.writeVint(self.response)
        self.writeVint(0)