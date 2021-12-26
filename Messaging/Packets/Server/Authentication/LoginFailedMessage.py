import json
import socket

from Logic.Data.DataManager import Writer

class LoginFailedMessage(Writer):
    def __init__(self, client, player, errorInfo, fingerprint=None):
        super().__init__(client)
        self.id = 20103
        self.client = client
        self.player = player
        self.errorInfo = errorInfo
        self.fingerprint = fingerprint
        if fingerprint != None:
            self.cndUrl = f'http://{socket.gethostbyname(socket.gethostname())}:8080'
        else:
            self.cndUrl = None

    def encode(self):
        self.writeInt(self.errorInfo['ErrorID'])
        self.writeString(self.fingerprint)
        self.writeString()
        self.writeString(self.cndUrl)
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