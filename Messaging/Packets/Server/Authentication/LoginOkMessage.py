from Logic.Data.DataManager import Writer

class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20104
        self.client = client
        self.player = player
        self.version = 1

    def encode(self):
        self.writeLong(self.player.HighID, self.player.LowID)
        self.writeLong(self.player.HighID, self.player.LowID)
        self.writeString(self.player.Token)
        self.writeString()
        self.writeString()
        self.writeInt(40)
        self.writeInt(161)
        self.writeInt(1)
        self.writeString('prod')
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString('CA')
        self.writeString()
        self.writeInt(2)
        self.writeString()

        self.writeInt(2)
        self.writeString('https://game-assets.brawlstarsgame.com')
        self.writeString('http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com')

        self.writeInt(2)
        self.writeString('https://event-assets.brawlstars.com')
        self.writeString('https://24b999e6da07674e22b0-8209975788a0f2469e68e84405ae4fcf.ssl.cf2.rackcdn.com/event-assets')

        self.writeVint(0)
        self.writeCompressedString(b'')
        self.writeBoolean(True)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString('https://play.google.com/store/apps/details?id=com.supercell.brawlstars')
        self.writeString()
        self.writeBoolean(False)