import json

from Database.ClubManager import ClubManager
from Logic.Data.DataManager import Writer
from Logic.Stream.StreamEntryFactory import StreamEntryFactory


class AllianceStreamMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24311
        self.client = client
        self.player = player

    def encode(self):
        clubdb = ClubManager()
        clubData = json.loads(clubdb.getClubWithLowID(self.player.allianceID[1])[0][1])
        self.writeVint(len(clubData['ChatData']))

        for i in clubData['ChatData']:
            self.writeVint(i['StreamType'])
            StreamEntryFactory.encode(self, i)