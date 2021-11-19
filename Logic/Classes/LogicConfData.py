from Logic.Data.DataManager import Reader
from Logic.Data.DataManager import Writer


class LogicConfData:
    def decode(self: Reader):
        pass

    def encode(self: Writer):
        self.writeVint(0)

        # Event Slots IDs Array
        self.writeVint(22)  # Count
        self.writeVint(1)  # Gem Grab
        self.writeVint(2)  # Showdown
        self.writeVint(3)  # Daily Events
        self.writeVint(4)  # Team Events
        self.writeVint(5)  # Duo Showdown
        self.writeVint(6)  # Team Events 2
        self.writeVint(7)  # Special Events
        self.writeVint(8)  # Solo Events
        self.writeVint(9)  # Power Play
        self.writeVint(10)  # Seasonal Events
        self.writeVint(11)  # Seasonal Events 2
        self.writeVint(12)  # Candidates of The Day
        self.writeVint(13)  # Winner of The Day
        self.writeVint(14)  # Solo Mode Power League
        self.writeVint(15)  # Team Mode Power League
        self.writeVint(16)  # Club league
        self.writeVint(17)  # Club league
        self.writeVint(20)  # Championship Challenge (Stage 1)
        self.writeVint(21)  # Championship Challenge (Stage 2)
        self.writeVint(22)  # Championship Challenge (Stage 3)
        self.writeVint(23)  # Championship Challenge (Stage 4)
        self.writeVint(24)  # Championship Challenge (Stage 5)
        # Event Slots IDs Array End

        self.writeVint(len(self.player.allMaps) + 2)  # Events Count

        eventIndex = 1
        for i in self.player.allMaps:
            self.writeVint(0)
            self.writeVint(eventIndex)  # EventType
            self.writeVint(0)  # EventsBeginCountdown
            self.writeVint(99999)  # Timer
            self.writeVint(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVint(-64)  # GameModeVariation
            self.writeVint(2)  # State
            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)  # Modifiers
            self.writeVint(0)
            self.writeVint(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVint(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)  # ChronosTextEntry
            self.writeVint(-64)
            self.writeBoolean(False)
            eventIndex += 1

        self.writeVint(0)
        self.writeVint(16)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(99999)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(2)  # State
        self.writeString()
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # Modifiers
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # ChronosTextEntry
        self.writeVint(-64)
        self.writeBoolean(False)

        self.writeVint(0)
        self.writeVint(17)  # EventType
        self.writeVint(0)  # EventsBeginCountdown
        self.writeVint(99999)  # Timer
        self.writeVint(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVint(-64)  # GameModeVariation
        self.writeVint(2)  # State
        self.writeString()
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # Modifiers
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVint(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # ChronosTextEntry
        self.writeVint(-64)
        self.writeBoolean(False)

        self.writeVint(0)  # Coming Up Events Count

        self.writeVint(10)  # Brawler Upgrade Cost
        self.writeVint(20)
        self.writeVint(35)
        self.writeVint(75)
        self.writeVint(140)
        self.writeVint(290)
        self.writeVint(480)
        self.writeVint(800)
        self.writeVint(1250)
        self.writeVint(1875)
        self.writeVint(2800)

        self.writeVint(4)  # Shop Coins Price
        self.writeVint(20)
        self.writeVint(50)
        self.writeVint(140)
        self.writeVint(280)

        self.writeVint(4)  # Shop Coins Amount
        self.writeVint(150)
        self.writeVint(400)
        self.writeVint(1200)
        self.writeVint(2600)

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVint(0)  # Release Entry

        self.writeVint(21)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000034) # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270) # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, 0) # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 0) # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0) # Double Token Event
        self.writeLong(31, 0) # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(10046, 1)

        self.writeVint(2)  # Timed Int Value Entry

        # Double tokens event
        self.writeVint(14)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(700000) # Time left

        # Gold rush event
        self.writeVint(31)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(700000) # Time left

        self.writeVint(0)  # Custom Event

        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(0)