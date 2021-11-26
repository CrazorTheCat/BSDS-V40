from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class LogicPlayerMap:
    def decode(self: Reader):
        self.readLogicLong("MapID")
        self.readString("MapName")
        self.readVint("GameModeVariation")
        self.readDataReference("MapEnvironmentData")
        self.readCompressedString("MapData")
        self.readLogicLong("AccountID")
        self.readString("AvatarName")
        self.readVint("State")
        self.readLong("LastUpdateTimeSecondsSinceEpoch")
        self.readVint("FriendlyParticipantCount")
        self.readVint("FriendlySignoffCount")
        self.readVint("Dislikes")
        self.readVint("Likes")
        self.readVint("Battles")