import json
import random

from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Files.Classes.Regions import Regions


class JoinableAllianceListMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24304
        self.client = client
        self.player = player

    def encode(self):
        clubdb = ClubManager()
        allClubs = clubdb.getAllClubByRegion(self.player.region)
        if len(allClubs) >= 50:
            maxClub = 50
            self.writeVint(50)
        else:
            maxClub = len(allClubs)
            self.writeVint(len(allClubs))

        if maxClub != 1:
            found = 0
            randomClubList = []
            while found != maxClub:
                randomEntry = random.choice(allClubs)
                if randomEntry not in randomClubList:
                    randomClubList.append(randomEntry)
                    found += 1

        for clubData in allClubs:
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
