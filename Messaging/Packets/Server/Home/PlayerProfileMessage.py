import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class PlayerProfileMessage(Writer):
    def __init__(self, client, player, playerID):
        super().__init__(client)
        self.id = 24113
        self.client = client
        self.player = player
        self.playerID = playerID

    def encode(self):
        playerdb = DatabaseManager()
        try:
            playerData = json.loads(playerdb.getPlayerWithLowID(self.playerID[1])[0][2])
        except IndexError:
            return

        self.writeLogicLong(self.playerID[0], self.playerID[1])
        self.writeVint(0)

        # Brawlers
        self.writeVint(len(self.player.allBrawlers)) # TODO: Sync player brawlers
        for i in self.player.allBrawlers:
            self.writeDataReference(16, i)
            self.writeDataReference(0, 0)
            self.writeVint(1250)
            self.writeVint(1250)
            self.writeVint(10)

        self.writeVint(16)

        self.writeVint(1)
        self.writeVint(0) # 3v3 Victories

        self.writeVint(2)
        self.writeVint(playerData['experience']) # Experince

        self.writeVint(3)
        self.writeVint(playerData['trophies']) # Current Trophies

        self.writeVint(4)
        self.writeVint(playerData['highestTrophies']) # Highest Trophies

        self.writeVint(5)
        self.writeVint(len(self.player.allBrawlers))

        self.writeVint(8)
        self.writeVint(0) # Solo Victories

        self.writeVint(11)
        self.writeVint(0) # Duo Victories

        self.writeVint(9)
        self.writeVint(0) # Highest Robo Rumble LVL Passed

        self.writeVint(12)
        self.writeVint(0) # Highest Boss Fight LVL Passed

        self.writeVint(13)
        self.writeVint(100)

        self.writeVint(14)
        self.writeVint(0)

        self.writeVint(15)
        self.writeVint(0) # Most Challenge Wins

        self.writeVint(16)
        self.writeVint(0) # Highest Rampage LVL Passed

        self.writeVint(17)
        self.writeVint(0) # Highest Team League

        self.writeVint(18)
        self.writeVint(0) # Highest Solo League

        self.writeVint(19)
        self.writeVint(0)  # Highest club league

        self.writeString(playerData['name'])
        self.writeVint(100)
        self.writeVint(28000000 + playerData['playericon'])
        self.writeVint(43000000 + playerData['namecolor'])
        self.writeVint(46000000)

        self.writeBoolean(playerData['allianceID'] != [0, 0])

        if playerData['allianceID'] != [0, 0]:
            clubdb = ClubManager()
            clubData = json.loads(clubdb.getClubWithLowID(playerData['allianceID'][1])[0][1])
            localMemberData = clubdb.getMemberWithLowID(clubData, self.playerID[1])
            self.writeLong(clubData['HighID'], clubData['LowID'])
            self.writeString(clubData['Name'])
            self.writeDataReference(8, clubData['BadgeID'])
            self.writeVint(clubData['Type']) # Type
            self.writeVint(len(clubData['Members'])) # Total Members
            self.writeVint(clubdb.getTotalTrophies(clubData)) # Total Trophies
            self.writeVint(clubData['TrophiesRequired']) # Trophies Required
            self.writeDataReference(0)
            self.writeString(Regions.getRegionByID(self, clubData['RegionID'])) # Region
            self.writeVint(0)
            self.writeBoolean(clubData['FamilyFriendly']) # Family Friendly
            self.writeVint(0)

            self.writeDataReference(25, localMemberData['Role'])

        else:
            self.writeDataReference(0, 0)