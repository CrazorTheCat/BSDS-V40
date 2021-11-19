from Database.DatabaseManager import DatabaseManager
from Logic.Data.DataManager import Writer
from Logic.Classes.LogicClientAvatar import LogicClientAvatar
from Logic.Classes.LogicClientHome import LogicClientHome


class OwnHomeDataMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.client = client
        self.player = player

    def encode(self):
        self.db = DatabaseManager()
        try:
            self.db.LoadAccount(self.player.LowID, self.player)
        except:
            print("[ERROR] Failed to load player data from database.")

        self.writeVint(0)
        self.writeVint(0)
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)
