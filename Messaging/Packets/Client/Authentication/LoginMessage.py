import json
import time
import traceback

from Database.ClubManager import ClubManager
from Logic.Client.ClientsManager import ClientsManager
from Logic.Client.PlayerManager import Players
from Database.DatabaseManager import DatabaseManager
from Messaging.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Messaging.Packets.Server.Alliance.UnknownAllianceMessage import UnknownAllianceMessage
from Messaging.Packets.Server.Authentication.LoginFailedMessage import LoginFailedMessage

from Messaging.Packets.Server.Authentication.LoginOkMessage import LoginOkMessage
from Messaging.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Messaging.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage

from Logic.Data.DataManager import Reader


class LoginMessage(Reader):
    def __init__(self, client, player: Players, header_bytes):
        super().__init__(header_bytes)
        self.client = client
        self.player = player
        self.encrypted = False


    def decode(self):
        try:
            self.player.HighID = self.readInt()
            self.player.LowID = self.readInt()
            self.Token = self.readString()

            self.player.device.major = self.readInt()
            self.player.device.minor = self.readInt()
            self.player.device.build = self.readInt()
            if self.player.device.major == 0:
                self.player.device.major = 39
        except:
            self.encrypted = True

        # self.FingerprintSha = self.readString()
        #
        # self.DeviceModel = self.readString()
        # self.IsAndroid = self.readBoolean()
        # self.Unknown = self.readBoolean()
        # self.DeviceLanguage = self.readString()
        #
        # self.OSVersion = self.readString()
        #
        # self.readInt()
        # self.readVint()
        #
        # self.OpenUDID = self.readString()
        #
        # self.readBoolean()
        # self.readInt()
        #
        # self.readInt()
        # self.readVint()
        #
        # self.AppVersion = self.readString()

    def process(self):
        if self.encrypted == False:
            self.db = DatabaseManager()
            try:
                self.AccountCreated = self.db.GetAllDb()
                if self.player.LowID in self.AccountCreated:
                    self.db.LoadAccount(self.player.LowID, self.player)
                    if self.player.Token != self.Token:
                        self.client.close()
                        return

                elif self.player.LowID != 0:
                    data = Players.CreateAccount(self.player, self.player.HighID, self.player.LowID, self.Token, True)
                    self.db.createAccount(self.player.LowID, self.player.Token, data)
                    self.db.LoadAccount(self.player.LowID, self.player)

                else:
                    data = Players.CreateAccount(self.player, self.player.HighID, self.player.LowID, self.Token)
                    self.db.createAccount(self.player.LowID, self.player.Token, data)
                    self.db.LoadAccount(self.player.LowID, self.player)

            except Exception:
                print(traceback.print_exc())
                data = Players.CreateAccount(self.player, self.player.HighID, self.player.LowID, self.Token)
                self.db.createAccount(self.player.LowID, self.player.Token, data)
                self.db.LoadAccount(self.player.LowID, self.player)

            ClientsManager.AddSocket(self.player.LowID, self.client)

            if self.player.device.major == 40:
                LoginOkMessage(self.client, self.player).send(self.player.LowID, 2)
                OwnHomeDataMessage(self.client, self.player).send(self.player.LowID)
                try:
                    clubdb = ClubManager()
                    json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])
                    MyAllianceMessage(self.client, self.player, self.player.allianceID).send(self.player.LowID)
                    if self.player.allianceID[1] != 0:
                        AllianceStreamMessage(self.client, self.player).send(self.player.LowID)
                except IndexError:
                    playerData = json.loads(self.db.getPlayerWithLowID(self.player.LowID)[0][2])
                    playerData['allianceID'] = [0, 0]
                    self.db.updatePlayerData(playerData, self.player.LowID)
                    self.db.LoadAccount(self.player.LowID, self.player)
                    MyAllianceMessage(self.client, self.player, self.player.allianceID).send(self.player.LowID)

                UnknownAllianceMessage(self.client, self.player).send(self.player.LowID)

            else:
                print(f"Not supported version Detected: {self.player.device.major}.{self.player.device.build}.{self.player.device.minor}")