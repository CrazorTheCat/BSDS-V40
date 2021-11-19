from Logic.Classes.LogicDataTables import LogicDataTables
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class PlayerDisplayData:
    Checksum = 0
    AccountBoundFlags = 0
    LogicBattleMode = "LogicBattleModeClient"
    LogicHomeMode = "LogicHomeMode"

    def decode(self: Reader):
        self.readString("PlayerName")
        self.readVint()
        self.readVint("PlayerThumbnail")
        self.readVint("NameColor")
        self.readVint()

    def encode(self: Writer, info):
        self.writeString(info[1]['Sender']['Name'])
        self.writeVint(100)
        self.writeVint(28000000 + info[1]['Sender']['Thumbnail'])
        self.writeVint(43000000 + info[1]['Sender']['NameColor'])
        self.writeVint(-1)

    def getNameColor(self, globalId):
        LogicDataTables.getDataById(globalId)

    def getPlayerThumbnail(self, globalId):
        LogicDataTables.getDataById(globalId)