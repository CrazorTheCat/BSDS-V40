import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class ChangeAllianceSettingsOkMessage(Writer):
    def __init__(self, client, player, clubid):
        super().__init__(client)
        self.id = 24313
        self.client = client
        self.player = player
        self.clubID = clubid

    def encode(self):
        playerdb = DatabaseManager()
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.clubID[1])[0][1])
        playerdb.LoadAccount(self.player.LowID, self.player)

        self.writeLong(clubData['HighID'], clubData['LowID'])
        self.writeString(clubData['Name'])
        self.writeDataReference(8, clubData['BadgeID'])
        self.writeVint(clubData['Type'])  # Type
        self.writeVint(len(clubData['Members']))  # Total Members
        self.writeVint(clubdb.getTotalTrophies(clubData))  # Total Trophies
        self.writeVint(clubData['TrophiesRequired'])  # Trophies Required
        self.writeDataReference(0)
        self.writeString(Regions.getRegionByID(self, clubData['RegionID']))  # Region
        self.writeVint(0)
        self.writeBoolean(clubData['FamilyFriendly'])  # Family Friendly
        self.writeVint(0)

        self.writeString(clubData['Description'])  # Description

        self.writeVint(len(clubData['Members']))  # Members Count

        for i in clubdb.getMembersSorted(clubData):
            memberData = i[1]
            playerData = json.loads(playerdb.getPlayerWithLowID(memberData['LowID'])[0][2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVint(memberData['Role'])  # Role
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

            self.writeVint(0)  # Club Leauge?