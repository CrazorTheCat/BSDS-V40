import json

from Database.DatabaseManager import DatabaseManager

from Logic.Data.DataManager import Writer


class LogicChangeAvatarNameCommand(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.client = client
        self.player = player

    def encode(self):
        self.db = DatabaseManager()
        self.database = json.loads(self.db.getPlayerWithLowID(self.player.LowID)[0][2])
        self.database['name'] = self.player.Name
        self.database['IsRegistred'] = True
        self.db.updatePlayerData(self.database, self.player.LowID)

        self.writeVint(201)
        self.writeString(self.player.Name)
        self.writeVint(0)

        self.writeVint(1)

        self.writeVint(2)
        self.writeVint(3)

        self.writeVint(4)
        self.writeVint(5)