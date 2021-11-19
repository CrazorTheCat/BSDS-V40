from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Messaging.Packets.Server.Battle.BattleEndMessage import BattleEndMessage
 
class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        self.playersList = {}
        self.readVint()
        self.result = self.readVint()
        self.rank = self.readVint()
        self.mapID = self.readDataReference()
        for i in range(self.readVint()):
            self.playersList[str(i)] = {}
            self.playersList[str(i)]["BrawlerID"] = self.readDataReferenceDouble(True)
            self.playersList[str(i)]["SkinID"] = self.readDataReferenceDouble(True)
            self.readVint()
            self.playersList[str(i)]["IsPlayer"] = self.readBoolean()
            self.playersList[str(i)]["Name"] = self.readString()
            if self.playersList[str(i)]["Name"] == "3" or self.playersList[str(i)]["Name"] == "4" or self.playersList[str(i)]["Name"] == "5":
                self.playersList[str(i)]["Unknown"] = 1
            else:
                self.playersList[str(i)]["Unknown"] = 0

    def process(self):
        self.info = []
        BattleEndMessage(self.client, self.player, self.playersList, self.info).send(self.player.LowID)
