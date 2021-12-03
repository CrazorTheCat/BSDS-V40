from Logic.Data.DataManager import Writer

class BattleEndMessage(Writer):
    def __init__(self, client, player, playersList, info):
        super().__init__(client)
        self.id = 23456
        self.client = client
        self.player = player
        self.allPlayers = playersList
        self.info = info

    def encode(self):
        self.writeLong(0, 1)
        self.writeLong(0, 1)
        self.writeVint(1) # Battle End Game Mode
        self.writeVint(0) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(0) # Tokens Gained
        self.writeVint(1250) # Trophies Result
        self.writeVint(0) # Power Play Points Gained
        self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Double Token Event
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Special Events Level Passed
        self.writeVint(0) # Epic Win Power Play Points Gained
        self.writeVint(0) # Championship Level Reached
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeByte(16)
        self.writeVint(-1)
        self.writeBoolean(False)

        self.writeVint(len(self.allPlayers))  # Players

        for index,playerEntry in self.allPlayers.items():
            if playerEntry["IsPlayer"] == True:
                self.writeByte(1)
            elif playerEntry["Unknown"] == 1:
                self.writeByte(4)
            else:
                self.writeByte(0)
            self.writeDataReference(playerEntry["BrawlerID"][0], playerEntry["BrawlerID"][1])  # BrawlerID
            self.writeDataReference(playerEntry["SkinID"][0], playerEntry["SkinID"][1])  # SkinID
            self.writeVint(1250) # Trophies
            self.writeVint(0)
            self.writeVint(10) # PowerLevel
            self.writeVint(0)
            self.writeBoolean(playerEntry["IsPlayer"])
            if playerEntry["IsPlayer"] == True:
                self.writeLong(self.player.HighID, self.player.LowID)
            self.writeString(playerEntry["Name"])  # PlayerName
            self.writeVint(100)
            self.writeVint(28000000 + self.player.thumbnail)  # PlayerThumbnail
            self.writeVint(43000000 + self.player.nameColor)  # NameColor
            self.writeVint(46000000)

        self.writeVint(0)

        self.writeVint(0)  # XpEntry

        self.writeVint(0)

        self.writeVint(2)  # LogicMilestoneProgress
        self.writeVint(1)
        self.writeVint(1250)
        self.writeVint(1250)
        self.writeVint(5)
        self.writeVint(9999999)
        self.writeVint(9999999)

        self.writeDataReference(28, self.player.thumbnail)

        self.writeBoolean(False)  # PlayAgainStatus

        self.writeBoolean(False)  # LogicQuests

        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # LogicRankedMatchRoundState
        self.writeVint(-1)
        self.writeBoolean(False)  # ChronosTextEntry
