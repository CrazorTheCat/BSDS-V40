from Logic.Data.DataManager import Writer


class AllianceMemberRemovedMessage(Writer):
    def __init__(self, client, player, clubID, playerID):
        super().__init__(client)
        self.id = 24309
        self.client = client
        self.player = player
        self.clubID = clubID
        self.playerID = playerID

    def encode(self):
        self.writeLong(self.clubID[0], self.clubID[1])
        self.writeLong(self.playerID[0], self.playerID[1])