from Logic.Data.DataManager import Writer


class UnknownAllianceMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 22161
        self.client = client
        self.player = player

    def encode(self):
        self.writeByte(31)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(9999999)
        self.writeVint(4)
        self.writeVint(3)

        self.writeVint(1)
        self.writeVint(4)
        self.writeDataReference(15, 7)
        self.writeVint(0)

        self.writeVint(2)
        self.writeVint(4)
        self.writeDataReference(15, 25)
        self.writeVint(0)

        self.writeVint(3)
        self.writeVint(4)
        self.writeDataReference(15, 5)
        self.writeVint(0)

        self.writeBoolean(True)

        self.writeLogicLong(0, 1) # LeagueID
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeLogicLong(0, 1)
        self.writeVint(1) # Day number
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(9999) # Season score
        self.writeVint(1) # Season leaderboard place
        self.writeVint(0)

        self.writeBoolean(True)

        self.writeLogicLong(0, 1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0) # Used normal tickets
        self.writeVint(4) # Max golden tickets
        self.writeVint(0) # Used golden tickets

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(999999)
        self.writeVint(4)
        self.writeVint(3)

        self.writeVint(1)
        self.writeVint(4)
        self.writeDataReference(15, 7)
        self.writeVint(0)

        self.writeVint(2)
        self.writeVint(4)
        self.writeDataReference(15, 25)
        self.writeVint(0)

        self.writeVint(3)
        self.writeVint(4)
        self.writeDataReference(15, 5)
        self.writeVint(0)

