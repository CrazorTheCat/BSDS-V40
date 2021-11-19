import json
import sqlite3
import traceback


class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect("player.sqlite")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE main (LowID integer, Token text, Data json)""")
        except:
            pass

    def createAccount(self, lowID, token, data):
        try:
            self.cursor.execute("INSERT INTO main (LowID, Token, Data) VALUES (?, ?, ?)",
                                (lowID, token, json.dumps(data, ensure_ascii=0)))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())

    def GetAllDb(self, low_id):
        self.playersId = []
        try:
            self.cursor.execute("SELECT * from main")
            self.db = self.cursor.fetchall()
            for i in range(len(self.db)):
                self.playersId.append(self.db[i][0])
            return self.playersId
        except Exception:
            print(traceback.format_exc())

    def getPlayerWithLowID(self, low):
        try:
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            return self.cursor.fetchall()
        except Exception:
            print(traceback.format_exc())

    def LoadAccount(self, low, player):
        try:
            self.player = player
            self.cursor.execute("SELECT * from main where LowID=?", (low,))
            self.players = self.cursor.fetchall()
            self.players = json.loads(self.players[0][2])
            self.player.Name = self.players['name']
            self.player.isRegistred = self.players['IsRegistred']
            self.player.level = self.players['level']
            self.player.doNotDisturb = self.players['DoNotDisturb']
            self.player.friends = self.players['friend']
            self.player.highestTrophies = self.players['highestTrophies']
            self.player.brawlerID = self.players['brawlerID']
            self.player.skinID = self.players['skinID']
            self.player.selectedSkin = self.players['selectedSkin']
            self.player.brawlerState = self.players['brawlerState']
            self.player.brawlersTrophies = self.players['brawlersTrophies']
            self.player.selectedRandomSkin = self.players['selectedRandomSkin']
            self.player.starpowerID = self.players['starpowerID']
            self.player.thumbnails = self.players['playericon']
            self.player.nameColor = self.players['namecolor']
            self.player.trophies = self.players['trophies']
            self.player.experience = self.players['experience']
            self.player.room_id = self.players['gameroomID']
            self.player.roomInfo = self.players['roomInfo']
            self.player.alliance_id = self.players['allianceID']
            self.player.isBanned = self.players['isBanned']
            self.player.gems = self.players['gems']
            self.player.coins = self.players['coins']

        except Exception:
            print(traceback.format_exc())

    def update_player_data(self, data, lowID):
        try:
            self.cursor.execute("UPDATE main SET Data=? WHERE LowID=?", (json.dumps(data, ensure_ascii=0), lowID))
            self.conn.commit()
        except Exception:
            print(traceback.format_exc())

    def getPlayerDB(self, token):
        try:
            self.cursor.execute("SELECT * from main where Token=?", (token,))
            return self.cursor.fetchall()
        except Exception:
            print(traceback.format_exc())
