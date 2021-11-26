from Logic.Data.DataManager import Writer

class LoginFailedMessage(Writer):
    def __init__(self, client, player, errorInfo):
        super().__init__(client)
        self.id = 20103
        self.client = client
        self.player = player
        self.errorInfo = errorInfo

    def encode(self):
        self.writeInt(self.errorInfo['ErrorID'])
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString(self.errorInfo['Message'])
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