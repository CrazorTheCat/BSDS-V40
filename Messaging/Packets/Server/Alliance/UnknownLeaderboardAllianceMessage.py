from Logic.Data.DataManager import Writer


class UnknownLeaderboardAllianceMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 22160
        self.client = client
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeLogicLong(0, 1)
        self.writeVint(1)
        self.writeVint(1)

        self.writeVint(1)

        self.writeLogicLong(0, 1)
        self.writeLong(0, 1)
        self.writeDataReference(8, 16)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)

