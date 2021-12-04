import json

from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer


class AllianceMemberMessage(Writer):
    def __init__(self, client, player, clubID, memberData):
        super().__init__(client)
        self.id = 24308
        self.client = client
        self.player = player
        self.clubID = clubID
        self.memberData = memberData

    def encode(self):
        playerdb = DatabaseManager()
        playerData = json.loads(playerdb.getPlayerWithLowID(self.memberData['LowID'])[0][2])
        self.writeLong(self.clubID[0], self.clubID[1])

        self.writeLong(self.memberData['HighID'], self.memberData['LowID'])
        self.writeVint(self.memberData['Role'])  # Role
        self.writeVint(playerData['trophies'])  # Trophies
        self.writeVint(0)  # Player State TODO: Members state
        self.writeVint(0)  # State Timer

        # whatIsThat = 5
        whatIsThat = 0
        self.writeVint(whatIsThat)
        # if whatIsThat >= 1:
        #     self.writeVint(1) # idk
        #     self.writeVint(3) # Power League Rank

        self.writeBoolean(False)  # DoNotDisturb TODO: Do not disturb sync

        self.writeString(playerData['name'])  # Player Name
        self.writeVint(100)
        self.writeVint(28000000 + playerData['playericon'])  # Player Thumbnail
        self.writeVint(43000000 + playerData['namecolor'])  # Player Name Color
        self.writeVint(46000000)  # Player Brawlpass Name

        self.writeVint(-1)
        self.writeBoolean(False)

        self.writeVint(0)  # Club League?