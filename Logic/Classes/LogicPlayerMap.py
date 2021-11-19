from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicPlayerMap:
    def decode(self: Reader):
        self.readVLong("MapID")
        self.readString("MapName")
        self.readVint("GameModeVariation")
        self.readDataReference("MapEnvironmentData")
        self.readCompressedString("MapData")
        self.readVLong("AccountID")
        self.readString("AvatarName")
        self.readVint("State")
        self.readLong("LastUpdateTimeSecondsSinceEpoch")
        self.readVint("FriendlyParticipantCount")
        self.readVint("FriendlySignoffCount")
        self.readVint("Dislikes")
        self.readVint("Likes")
        self.readVint("Battles")