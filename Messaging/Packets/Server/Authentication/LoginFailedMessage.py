from Logic.Data.DataManager import Writer

class LoginFailedMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20103
        self.client = client
        self.player = player

    def encode(self):
        self.writeInt(1)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeBytes(b'')
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeInt(0)
        self.writeByte(3)
        self.writeStringReference()
        self.writeVint(0)
        self.writeStringReference()
        self.writeBoolean(False)