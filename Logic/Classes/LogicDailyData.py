from Logic.Helpers.ForcedDrops import ForcedDrops
from Logic.Data.DataManager import Writer


class LogicDailyData:
    def encode(self: Writer):
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(self.player.trophies)
        self.writeVint(self.player.highestTrophies)
        self.writeVint(self.player.highestTrophies)
        self.writeVint(self.player.trophy_road_tier)
        self.writeVint(self.player.experience)
        self.writeDataReference(28, self.player.thumbnail)
        self.writeDataReference(43, self.player.nameColor)

        # Array
        self.writeVint(0)

        # Selected Skins
        skinsList = []
        for v in self.player.selectedSkin.values():
            if v != 0:
                skinsList.append(v)

        self.writeVint(len(skinsList))
        for v in skinsList:
            self.writeDataReference(29, v)  # SkinID

        # Skin Selected For Random Skin
        self.writeVint(len(self.player.allSkins))
        for i in self.player.allSkins:
            self.writeDataReference(29, i)

        # Current Random Skin
        self.writeVint(0)
        for i in range(0):
            self.writeDataReference(29, 0)  # SkinID

        # Unlocked Skin
        self.writeVint(len(self.player.allSkins))
        for i in self.player.allSkins:
            self.writeDataReference(29, i)

        # Unlocked Skin Purchase Option
        self.writeVint(0)
        for i in range(0):
            self.writeDataReference(29, 0)  # SkinID

        # New Item
        self.writeVint(0)
        for i in range(0):
            self.writeDataReference(23, 0)  # ItemID

        self.writeVint(0)  # Leaderboard Region | 0 = Global, 1 = Asia
        self.writeVint(self.player.highestTrophies)  # Trophy Road Highest Trophies
        self.writeVint(0)
        self.writeVint(1)
        self.writeBoolean(True)
        self.writeVint(999999)  # Tokens Doubler
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        ForcedDrops.encode(self)

        self.writeByte(4)  # Shop Token Doubler
        self.writeVint(2)  # Token Doubler New Tag State
        self.writeVint(2)  # Event Tickets New Tag State
        self.writeVint(2)  # Coin Packs New Tag State
        self.writeVint(0)  # Change Name Cost
        self.writeVint(0)  # Timer For the Next Name Change

        self.writeVint(0)  # Shop Offers

        self.writeVint(0)

        self.writeVint(200)  # Available tokens from battles
        self.writeVint(-1)  # Timer for new tokens

        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeDataReference(16, self.player.brawlerID)
        self.writeString(self.player.region)
        self.writeString("Project BSDS")

        self.writeVint(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 0)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        self.writeLong(9, 1)  # ShowStarPoints
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 1)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 1)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 1)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1) # Have already watched club league stupid animation

        self.writeVint(0)

        self.writeVint(9)  # Brawlpass
        for i in range(9):
            self.writeVint(i)
            if i != 0:
                self.writeVint(34500)
            else:
                self.writeVint(28500)
            self.writeBoolean(True)
            self.writeVint(0)

            self.writeByte(2)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVint(0)

        self.writeBoolean(True) # Quest
        self.writeVint(0)

        self.writeBoolean(True)
        self.writeVint(len(self.player.allPins) + len(self.player.allThumbnailsReward))  # Vanity Count
        for i in self.player.allPins:
            self.writeDataReference(52, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        for i in self.player.allThumbnailsReward:
            self.writeDataReference(28, i)
            self.writeVint(1)
            for i in range(1):
                self.writeVint(1)
                self.writeVint(1)

        self.writeBoolean(False)

        self.writeInt(0)