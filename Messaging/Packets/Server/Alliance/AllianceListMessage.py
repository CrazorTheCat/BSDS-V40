import json

from Database.ClubManager import ClubManager
from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class AllianceListMessage(Writer):
    def __init__(self, client, player, searchInfo):
        super().__init__(client)
        self.id = 24310
        self.client = client
        self.player = player
        self.searchInfo = searchInfo

    def encode(self):
        clubdb = ClubManager()
        allClubs = clubdb.getAllClub()
        finalList = []

        found = 0
        for i in allClubs:
            if found == 100: return
            elif i['Name'].lower().startswith(self.searchInfo['SearchString']):
                finalList.append(i)
                found += 1

        self.writeString(self.searchInfo['SearchString'])

        self.writeVint(len(finalList))

        for clubData in finalList:
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