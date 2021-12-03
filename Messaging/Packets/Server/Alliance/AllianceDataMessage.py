import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class AllianceDataMessage(Writer):
    def __init__(self, client, player, clubID, sentTry=0):
        super().__init__(client)
        self.id = 24301
        self.client = client
        self.player = player
        self.clubID = clubID
        self.sentTry = sentTry

    def encode(self):
        playerdb = DatabaseManager()
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.clubID[1])[0][1])
        playerdb.LoadAccount(self.player.LowID, self.player)

        '''if self.sentTry == 1:
            if clubData['Members'][str(self.player.LowID)]['Role'] == 2:
                self.writeBoolean(True)
            elif clubData['Members'][str(self.player.LowID)]['Role'] == 4:
                self.writeBoolean(True)
            else:
                self.writeBoolean(False)
        elif self.sentTry == 2 and clubData['LowID'] == self.player.allianceID[1]:
            self.writeBoolean(False)
            self.sentTry = 0
        else:
            self.writeBoolean(False)
            self.sentTry = 0
        '''

        self.writeBoolean(False)

        self.writeLong(clubData['HighID'], clubData['LowID'])
        self.writeString(clubData['Name'])
        self.writeDataReference(8, clubData['BadgeID'])
        self.writeVint(clubData['Type']) # Type
        self.writeVint(len(clubData['Members']))  # Total Members
        self.writeVint(clubdb.getTotalTrophies(clubData))  # Total Trophies
        self.writeVint(clubData['TrophiesRequired'])  # Trophies Required
        self.writeDataReference(0)
        self.writeString(Regions.getRegionByID(self, clubData['RegionID']))  # Region
        self.writeVint(0)
        self.writeBoolean(clubData['FamilyFriendly'])  # Family Friendly
        self.writeVint(0)

        self.writeString(clubData['Description']) # Description

        self.writeVint(len(clubData['Members'])) # Members Count

        for i in clubdb.getMembersSorted(clubData):
            memberData = i[1]
            playerData = json.loads(playerdb.getPlayerWithLowID(memberData['LowID'])[0][2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVint(memberData['Role']) # Role
            self.writeVint(playerData['trophies']) # Trophies
            self.writeVint(0) # Player State TODO: Members state
            self.writeVint(0) # State Timer

            # whatIsThat = 5
            whatIsThat = 0
            self.writeVint(whatIsThat)
            # if whatIsThat >= 1:
            #     self.writeVint(1) # idk
            #     self.writeVint(3) # Power League Rank

            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(playerData['name']) # Player Name
            self.writeVint(100)
            self.writeVint(28000000 + playerData['playericon']) # Player Thumbnail
            self.writeVint(43000000 + playerData['namecolor']) # Player Name Color
            self.writeVint(46000000) # Color Gradients

            self.writeVint(-1)
            self.writeBoolean(False)

            self.writeVint(0) # Club Leauge?