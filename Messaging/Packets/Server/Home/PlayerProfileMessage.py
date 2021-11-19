from Logic.Data.DataManager import Writer


class PlayerProfileMessage(Writer):
    def __init__(self, client, player, entry):
        super().__init__(client)
        self.id = 24113
        self.client = client
        self.player = player
        self.info = entry

    def encode(self):
        self.writeVLong(self.info.playerID[0], self.info.playerID[1])
        self.writeVint(0)

        # Brawlers
        self.writeVint(len(self.player.allBrawlers))
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
        self.writeVint(self.player.experience) # Experince

        self.writeVint(3)
        self.writeVint(self.player.trophies) # Current Trophies

        self.writeVint(4)
        self.writeVint(self.player.highestTrophies) # Highest Trophies

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

        self.writeString(self.player.Name)
        self.writeVint(100)
        self.writeVint(28000000 + self.player.thumbnails)
        self.writeVint(43000000 + self.player.nameColor)
        self.writeVint(-1)

        self.writeVint(0)
        self.writeVint(0)