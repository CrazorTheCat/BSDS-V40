from Logic.Data.DataManager import Writer
from Logic.Stream.StreamEntryFactory import StreamEntryFactory


class AllianceStreamEntryMessage(Writer):
    def __init__(self, client, player, stream):
        super().__init__(client)
        self.id = 24312
        self.client = client
        self.player = player
        self.streamData = stream

    def encode(self):
        self.writeVint(self.streamData['StreamType'])
        StreamEntryFactory.encode(self,  self.streamData)