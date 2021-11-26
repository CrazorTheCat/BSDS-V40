import json

from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class MyAllianceMessage(Writer):
    def __init__(self, client, player, clubID):
        super().__init__(client)
        self.id = 24399
        self.client = client
        self.player = player
        self.ClubID = clubID

    def encode(self):
        clubdb = ClubManager()
        if self.ClubID[1] != 0:
            clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])
            localMemberData = clubdb.getMemberWithLowID(clubData, self.player.LowID)
            self.writeVint(1) # Onlines Members TODO: members state
            self.writeBoolean(True)
            self.writeDataReference(25, localMemberData['Role']) # Role

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

            self.writeBoolean(False)

        else:
            self.writeVint(0)
            self.writeVint(0)