from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ForcedDrops:
    def decode(self: Reader):
        self.readVint()
        self.readVint()
        for i in range(self.readVint()):
            self.readVint()

    def encode(self: Writer):
        self.writeVint(0) # Starpower Drop
        self.writeVint(0) # Gadget Drop

        self.writeVint(5) # Rarity Count
        self.writeVint(0) # Rare Drop
        self.writeVint(0) # Super Rare Drop
        self.writeVint(0) # Epic Drop
        self.writeVint(0) # Mythic Drop
        self.writeVint(0) # Legendary Drop