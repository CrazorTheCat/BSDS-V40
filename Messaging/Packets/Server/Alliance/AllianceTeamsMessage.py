from Logic.Data.DataManager import Writer


class AllianceTeamsMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24364
        self.client = client
        self.player = player

    def encode(self):
        self.writeBoolean(True)
        self.writeVint(0) # AllianceTeamEntry