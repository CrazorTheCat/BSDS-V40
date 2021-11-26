from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

class LogicClientAvatar:
    def decode(self: Reader):
        pass

    def encode(self: Writer):
        self.writeLogicLong(self.player.HighID, self.player.LowID)  # PlayerID
        self.writeLogicLong(self.player.HighID, self.player.LowID)
        self.writeLogicLong(self.player.HighID, self.player.LowID)

        self.writeString(self.player.Name)  # PlayerName
        self.writeBoolean(self.player.isRegistred)  # isRegistred

        self.writeString()

        self.writeVint(15) # Commodity Count

        # Array
        brawlersUnlock = self.player.allBrawlersUnlock
        brawlers = self.player.allBrawlers
        brawlersCount = len(brawlers)

        # Unlocked Brawlers and Resources Array
        self.writeVint(5 + len(brawlersUnlock))  # Count
        for i in brawlersUnlock:
            self.writeDataReference(23, i)
            self.writeVint(1)


        self.writeDataReference(5, 1)
        self.writeVint(1)

        self.writeDataReference(5, 8)
        self.writeVint(self.player.coins)  # Coins

        self.writeDataReference(5, 9)
        self.writeVint(3)

        self.writeDataReference(5, 10)
        self.writeVint(self.player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVint(125)

        # Brawlers Trophies Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(1250)
        # Brawlers Trophies Array End

        # Brawlers Trophies for Rank Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(1250)
        # Brawlers Trophies for Rank Array End

        # Unknown Brawlers Array
        self.writeVint(0)  # Count
        # Unknown Brawlers Array End

        # Brawlers Power Points Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(1410)
        # Brawlers Power Points Array End

        # Brawlers Power Level Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(10)
        # Brawlers Power Level Array End

        # Array
        allStarpowers = self.player.allStarpowers
        self.writeVint(len(allStarpowers))  # Count
        for x in allStarpowers:
            self.writeDataReference(23, x)  # Cards ID
            self.writeVint(1)  # Star Power Unlocked State
        # Brawlers Star Powers Array End

        # Array
        self.writeVint(len(self.player.brawlerState))  # HeroSeenState
        for i,v in self.player.brawlerState.items():
            self.writeDataReference(16, int(i))  # Brawler ID
            self.writeVint(v)  # 18 = randomSkin Activated

        # Selected Gear Slot1 Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(62000000)

        # Selected Gear Slot2 Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(62000001)

        # Gears Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(3)

        # Gears Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(3)

        # Gears Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(3)

        # Gears Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(3)

        # Gears Array
        self.writeVint(brawlersCount)  # Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVint(3)

        self.writeVint(self.player.gems)  # Diamonds
        self.writeVint(self.player.gems)  # Free Diamonds
        self.writeVint(self.player.level)  # Player Level
        self.writeVint(100)
        self.writeVint(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVint(0)  # Battle Count
        self.writeVint(0)  # WinCount
        self.writeVint(0)  # LoseCount
        self.writeVint(0)  # WinLooseStreak
        self.writeVint(0)  # NpcWinCount
        self.writeVint(0)  # NpcLoseCount
        self.writeVint(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVint(0)